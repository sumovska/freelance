
window.magichat = {}
window.magichat.set_callback = function(name, func) {
}
window.CR220_DATA = [
    {
        'identifier': 1,
        'selected': false,
        'local_date': '2014-12-12 12:13:14',
        'dob': '1947-06-22',
        'implant_serial': '',
        'implant_serial_options': ['123412341234', '4215234123512'],
        'locus': 'left',
        'name_first': 'Charlie',
        'name_last': 'Brown',
        'name_full': 'Charlie Brown',
        'gender': 'male',
        'surgery': '',
        'surgery_options': ["Li'l Folks Surgery", "Howdy Doody"],
        'surgeon': '',
        'surgeon_options': ['Lucy van Pelt', 'Linus van Pelt', 'Snoopy', 'Schroeder'],
        'clinic': '',
        'clinic_options': ['Peanuts'],
    },
    {
        'identifier': 2,
        'selected': false,
        'local_date': '2014-12-12 12:13:14',
        'dob': '1947-06-22',
        'implant_serial': '',
        'implant_serial_options': ['123412341234', '4215234123512'],
        'locus': 'left',
        'name_first': 'Charlie',
        'name_last': 'Brown',
        'name_full': 'Charlie Brown',
        'gender': 'male',
        'surgery': '',
        'surgery_options': ["Li'l Folks Surgery", "Howdy Doody"],
        'surgeon': '',
        'surgeon_options': ['Lucy van Pelt', 'Linus van Pelt', 'Snoopy', 'Schroeder'],
        'clinic': '',
        'clinic_options': ['Peanuts'],
    },
    {
        'identifier': 3,
        'selected': false,
        'local_date': '2014-12-12 12:13:14',
        'dob': '1947-06-22',
        'implant_serial': '',
        'implant_serial_options': ['123412341234', '4215234123512'],
        'locus': 'left',
        'name_first': 'Charlie',
        'name_last': 'Brown',
        'name_full': 'Charlie Brown',
        'gender': 'male',
        'surgery': '',
        'surgery_options': ["Li'l Folks Surgery", "Howdy Doody"],
        'surgeon': '',
        'surgeon_options': ['Lucy van Pelt', 'Linus van Pelt', 'Snoopy', 'Schroeder'],
        'clinic': '',
        'clinic_options': ['Peanuts'],
    },
    ];
window.CRF_DATA = [
    {
        'identifier': 4,
        'selected': false,
        'local_date': '2014-12-12 12:13:14',
        'dob': '1947-06-22',
        'implant_serial': '123412341234',
        'implant_serial_options': ['123412341234', '4215234123512'],
        'locus': 'left',
        'name_first': 'Charlie',
        'name_last': 'Brown',
        'name_full': 'Charlie Brown',
        'gender': 'male',
        'surgery': "Li'l Folks Surgery",
        'surgery_options': ["Li'l Folks Surgery", "Howdy Doody"],
        'surgeon': 'Lucy van Pelt',
        'surgeon_options': ['Lucy van Pelt', 'Linus van Pelt', 'Snoopy', 'Schroeder'],
        'clinic': 'Peanuts',
        'clinic_options': ['Peanuts'],
    },
    ];
window.HISTORY_DATA = [
    {
        'identifier': 5,
        'selected': false,
        'local_date': '2014-12-12 12:13:14',
        'dob': '1947-06-22',
        'implant_serial': '123412341234',
        'implant_serial_options': ['123412341234', '4215234123512'],
        'locus': 'left',
        'name_first': 'Charlie',
        'name_last': 'Brown',
        'name_full': 'Charlie Brown',
        'gender': 'male',
        'surgery': "Li'l Folks Surgery",
        'surgery_options': ["Li'l Folks Surgery", "Howdy Doody"],
        'surgeon': 'Lucy van Pelt',
        'surgeon_options': ['Lucy van Pelt', 'Linus van Pelt', 'Snoopy', 'Schroeder'],
        'clinic': 'Peanuts',
        'clinic_options': ['Peanuts'],
    },
    ];
    
window.magichat.CAN_NEW = ['surgery_options', 'clinic_options', 'surgeon_options'];
window.magichat.event_onload = function() {
    var header = 'row_header_template';
    var row_template = 'editable_row_template';
    set_view('cr220_view', window.magichat.CAN_NEW, header, row_template, window.CR220_DATA);
    set_view('crf_view', window.magichat.CAN_NEW, header, row_template, window.CRF_DATA);
    set_view('history_view', window.magichat.CAN_NEW, header, row_template, window.HISTORY_DATA);
}
window.magichat.poll = function() {
}

window.magichat.on_row_value_changed = function(identifier, datatype, value) {
    log.info('On row value changed: Event ignored in html mode');
}

window.magichat.on_modal_shown = function() {
}

window.magichat.on_modal_hide = function() {
}

window.magichat.on_click_view = function(identifier) {
    var data = window.CR220_DATA[0];
    log.info('Stubbornly displaying the first row only in html mode');
    show_modal('view', window.magichat.CAN_NEW, identifier, data)
}

window.magichat.on_click_new = function(identifier, key) {
    log.info(identifier, key);
    if (key == 'clinic') {
        data = {'clinic': '', 'cochlear_id': '', 'address': ''}
    } else if (key == 'surgery') {
        data = {'surgery': '', 'cochlear_id': '', 'address': ''}
    } else if (key == 'surgeon') {
        data = {'surgeon': '', 'cochlear_id': '', 'address': ''}
    } else {
        data = {}
    }
    hide_current_modal();
    show_modal(key, identifier, data);
}