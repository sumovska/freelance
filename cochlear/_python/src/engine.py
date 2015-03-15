import constants
import logging
import analyzer
import database
import time

from serials import AsyncSerials
from report import Report

CAN_NEW = ['clinic_options', 'surgery_options', 'surgeon_options']

log = logging.getLogger(__name__)

class JavascriptCallbackSupport(object):
    """
    JavascriptCallbackSupport is a helper mixin that maintains the callbacks provided by the HTML view layer.
    
    Under typical use:
    
    HTML View will set various javascript callbacks, usually during the <body onload> event.
    HTML view then responds to various javascript events, ultimately invoking the window.magichat methods.
     - These methods will be exposed in the ExposedMethods class, and implemented in python.
     - And these may, in turn, need to invoke the previously-set javascript callbacks.
    """
    def __init__(self):
        self.__js_callbacks = {}
        
    def set_callback(self, name, cb):
        log.info("Adding new callback: %s", name)
        self.__js_callbacks[name] = cb
        
    def invoke_callback(self, name, *args):
        if name in self.__js_callbacks:
            self.__js_callbacks[name].Call(*args)
        else:
            log.info("No callback found! Skipping");
            
    def contains_callback(self, name):
        return name in self.__js_callbacks

            
class DeviceManagerController(object):
    """
    Contains methods associated with the physical device.
    """
    def __init__(self, deviceManager, status_listener, on_error, save_log):
        self.__dm = deviceManager
        self.__stuck = None
        self.__percentage = None
        self.__save_log = save_log
        self.__on_error = on_error
        self.__status_listener = status_listener

    def _dm_status_change(self, stuck, percentage):
        percentage = int(percentage)
        if (self.__stuck, self.__percentage) != (stuck, percentage):
            log.info("Device Manager Status Change (Stuck: %s, Percentage: %s)", stuck, percentage)

            if stuck:
                self.__status_listener("stuck", 0)
            else:
                self.__status_listener("connected" if percentage != 0.0 else "disconnected", percentage)
            self.__stuck = stuck
            self.__percentage = percentage
            
    def poll(self):
        self._dm_status_change(self.__dm.stuck, self.__dm.last_percentage)
        if self.__dm.has_logs():
            try:
                logs = self.__dm.logs.get(block=0)
                fittingdata = logs['fittingdatalog']
                cr220_serial = logs['whoisthere'][0]
                
                log.info('Recieved Logs from CR220 device. Now analysing logs for sessions...')
                discovered_sessions = analyzer.LogAnalyzer(fittingdata).implants()
                log.info(discovered_sessions)
                for implant, rtc in discovered_sessions:
                    log.info('Generating FittingData.xml for implant and rtc at: %s', (implant, rtc))
                    logs = analyzer.LogAnalyzer(fittingdata)
                    logs.remove_all_other_sessions(implant, rtc)
                    
                    utc = logs.rtc_to_utc(rtc)
                    impedances = logs.latest_impedance(implant, rtc)[0]
                    profile = logs.latest_nrt_profile(implant, rtc)[0]
                    
                    self.__save_log(cr220_serial, impedances, profile, logs.tostring(), implant, utc)
            except Exception, e:
                log.exception(e)
                self.__on_error(str(e))
            
        
class EmailController(object):
    """
    Contains methods associated with sending and polling emails.
    """
    def __init__(self, email, data, refresh, on_error):
        self.__email = email
        self.__errors = []
        self.__data = data
        self.__on_error = on_error
        self.__refresh = refresh
    
    def poll(self):
        email_errors = self.__email.get_errors()
        if email_errors:
            self.__errors.append(str(email_errors))
            log.info(email_errors)
            
            self.__on_error(str('\n'.join(self.__errors)))
            
    def send_selected(self, title, body):
        log.info('Sending selected sessions to email')
        
        def prepare(session):
            session = session.as_dict(self.__data)
            report = Report([session]).pdf()
            crf = self.__data.get_crf(session['identifier']).tostring()
            
            return {
                'targets': [self.__data.address_for_clinic(session['clinic'])],
                'replyto': self.__data.address_for_surgeon(session['surgeon']),
                'subject': title,
                'body': body,
                'attachments': [('report.pdf', report), ('session.crf', crf)],
            }
        
        try:
            sessions = self.__data.get_selected(constants.CR220_MODE)
            emails = [prepare(x) for x in sessions]
            self.__email.send_sessions(emails)
            for x in sessions:
                self.__data.move(x.identifier, constants.CR220_MODE, constants.HISTORY_MODE)
            self.__refresh()
            
            log.info('Completed')
        except Exception, e:
            log.exception(e)
            self.__errors.append("{0}: {1}".format(str(type(e)), str(e)))
            self.__on_error(str('\n'.join(self.__errors)))
        
        
class PrintingController(object):
    """
    Associated with managing printing and printing-related tasks such as PDF output.
    """
    def __init__(self, app):
        self._app = app
        
    def save_selected_to_pdf(self, mode, message, wildcard):
        location = self._app.get_save_location(message, wildcard)
        if not location:
            return
            
            
        log.info("User selected %s as the output location", location)
        
        report = Report(self.data.get_selected(mode))
        report.save_pdf(location)
            
        log.info("Saved in %s", location)

        
class Logging(object):
    def __init__(self):
        self.__log = logging.getLogger('JS')
        
    def log(self, cb):
        cb.Call({
            'info': self.__log.info,
            'debug': self.__log.debug})

class ModalController(object):
    def __init__(self, data, refresh, update_modal_data, show_modal, hide_modal):
        self.__data = data
        self.__refresh = refresh
        self.__show_modal = show_modal
        self.__hide_modal = hide_modal
        self.__update_modal_data = update_modal_data
        
        self.__stack = []
        self.__SENTINEL = 'Expected Close'
        
    def __show_modal_with_stack(self, key, row_identifier, data):
        existing = bool(self.__stack)
        self.__stack.append((key, row_identifier, data))
        if existing:
            # There is an "existing" modal dialogue, which will close.
            self.__stack.append(self.__SENTINEL)
        self.__show_modal(key, CAN_NEW, row_identifier, data)
        
    def __hide_modal_with_stack(self):
        self.__hide_modal()
        
    def on_click_view(self, identifier):
        log.info("View Button clicked for %s", identifier)
        self.__hide_modal_with_stack()
        data = self.__data.get_session_by_id(int(identifier)).as_dict(self.__data)
        identifier = int(identifier)
        self.__show_modal_with_stack('view', identifier, data)
        
    def on_click_new(self, identifier, key):
        self.__hide_modal_with_stack()
        if key == 'clinic':
            data = {'clinic': '', 'cochlear_id': '', 'address': ''}
        elif key == 'surgery':
            data = {'surgery': '', 'cochlear_id': '', 'address': ''}
        elif key == 'surgeon':
            data = {'surgeon': '', 'cochlear_id': '', 'address': ''}
        else:
            data = {}
        
        identifier = int(identifier)
        self.__show_modal_with_stack(key, identifier, data)

    def on_modal_value_change(self, modal_name, key, value):
        log.info("on_modal_value_change: %s %s %s", modal_name, key, value);
        if key.endswith('_options'):
            key = key.rsplit('_', 1)[0]
            
        if isinstance(value, str):
            value = value.decode('utf-8')
            
        modal_name, identifier, data = self.__stack[-1]
        data[key] = value
        log.info('%s', data)
        # Save immediately if modal_name is 'view':
        if modal_name == 'view':
            self.__data.update_value(identifier, key, value)
            data = self.__data.get_session(identifier).as_dict(self.__data)
            self.__refresh()
            self.__update_modal_data(modal_name, CAN_NEW, identifier, data)
        
    def on_modal_save(self, modal_name):
        # Note:
        #  This immediately saves all the data (for this modal view) into the __data.
        #  It then updates the respective option in the session data via 'update_value'.
        #  This will be problematic if the save should be deferred until the 'save' button
        #  has been selected.
        #  For now, however, we wish to save immediately (ie, as soon as the values have changed)
        #  so will revisit this later if that requirement ever changes...
        for name in ['clinic', 'surgery', 'surgeon']:
            key, identifier, data = self.__stack[-1]
            if modal_name == name and name in data:
                self.__data.save_new(name, data)
                self.__data.update_value(identifier, name, data[name])
                self.__refresh()
                self.__hide_modal_with_stack()
                
    def on_modal_shown(self):
        pass
        
    def on_modal_hide(self):
        value = self.__stack.pop()
        if self.__stack and value != self.__SENTINEL:
            key, row_identifier, data = self.__stack.pop()
            data = self.__data.get_session_by_id(int(row_identifier)).as_dict(self.__data)
            self.__show_modal_with_stack(key, row_identifier, data)

            
class SerialsController(object):
    def __init__(self, data, asyncSerials, refresh):
        self.__data = data
        self.__serials = asyncSerials
        self.__refresh = refresh
        self._delta = 60*5
        self.__last_serials_update = 0
        
    def new_implant_id(self, implant_id):
        self.__serials.fetch(implant_id)
        
    def poll(self):
        for serials in self.__serials.completed():
            self.__last_serials_update = time.time()
            data = {}
            for serial in serials:
                if serial['implant_id'] not in data:
                    data[serial['implant_id']] = {'partid':[], 'serial':[]}
                data[serial['implant_id']]['serial'].append(serial['implant_serial'])
                data[serial['implant_id']]['partid'].append(serial['implant_partid'])
            if data:
                for implant_id, v in data.items():
                    self.__data.add_implant_details(implant_id, v['serial'], v['partid'])
                    self.__refresh()
                    
        current = time.time()
        if current - self.__last_serials_update > self._delta:
            self.__last_serials_update = current
            log.info('Checking implant serials for update...')
            for session in self.__data.get_sessions(constants.CR220_MODE):
                if not session.implant_serial_options:
                    self.new_implant_id(session.implant_id)
 
class ExposedMethods(JavascriptCallbackSupport, SerialsController, DeviceManagerController, EmailController, PrintingController, ModalController, Logging):
    """
    """
    def __init__(self, asyncSerials, data, email, app, deviceManager):
        JavascriptCallbackSupport.__init__(self)
        DeviceManagerController.__init__(self,
            deviceManager,
            status_listener=lambda *args: self.invoke_callback("status_listener", *args),
            on_error=lambda *args: self.invoke_callback("on_error", *args),
            save_log=self._new_log_data)
        EmailController.__init__(self, email, data,
            refresh=self._set_refresh_needed,
            on_error=lambda *args: self.invoke_callback("on_error", *args))
        PrintingController.__init__(self, app)
        ModalController.__init__(self, data,
            refresh=self._set_refresh_needed,
            update_modal_data=lambda *args: self.invoke_callback("update_modal_data", *args),
            show_modal=lambda *args: self.invoke_callback("show_modal", *args),
            hide_modal=lambda: self.invoke_callback("hide_current_modal"))
        SerialsController.__init__(self, data, asyncSerials, self._set_refresh_needed)
        Logging.__init__(self)
        
        self.__app = app
        self.__data = data
        self.__refresh_needed = True
        
    def _new_log_data(self, cr220_serial, impedances, profile, fittingdata, implant_id, utc):
        if implant_id == 'No ID':
            log.info('Recieved NEW data, but it had no implant ID. Discarding...')
            return
            
        log.info('Recieved NEW data from CR220! For session: %s', (implant_id, utc))
        self.new_implant_id(implant_id)
        session = database.Session(self.__data,
            serial=implant_id,
            impedances=impedances,
            profile=profile,
            utc_date=utc,
            implant_id=implant_id)

        self.__data.add_session(constants.CR220_MODE, session, cr220_serial, fittingdata)
        self.__refresh_needed = True
        
    def on_row_value_changed(self, identifier, key, value):
        identifier = int(identifier)
        if key.endswith('_options'): key = key.rsplit('_', 1)[0]
        if value is None: value = ""
        if isinstance(value, str):
            value = value.decode('utf-8')
            
        self.__data.update_value(id=identifier, key=key, value=value)
        self.__refresh_needed = True
            
    def event_onload(self):
        log.info('onload event')
        self.__app.loaded = True
        
    def _set_refresh_needed(self):
        self.__refresh_needed = True
        
    def refresh(self):
        log.info("Making call to set_view")
        header = 'row_header_template'
        row_template = 'editable_row_template'
        
        for mode in constants.VIEW_MODES:
            self.invoke_callback('set_view', mode, CAN_NEW, header, row_template, [x.as_dict(self.__data) for x in self.__data.get_sessions(mode)])
        
        log.info("Call completed")
        
    def poll(self):
        DeviceManagerController.poll(self)
        EmailController.poll(self)
        SerialsController.poll(self)
                
        if self.__refresh_needed:
            self.__refresh_needed = False
            self.refresh()
            