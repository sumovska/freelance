import gui.import_this_first
from cefpython3 import cefpython

import mh_logging as logging
import sys
import os
from database import MagicDatabase
import constants
from mh_email import MagicHatEmail
from path_utils import GetApplicationPath
from engine import ExposedMethods
from gui.error_handling import ExceptHook
from gui.magichat_app import magichat
from devicedetector import DeviceManager, log as dm_logs
import appdirs
from serials import AsyncSerials
import time

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

DEBUG = not hasattr(sys, 'frozen')
APP_DIRS = appdirs.AppDirs('MagicHat')


class MainApp(magichat.MainApp):

    def __init__(self, **kwargs):
        dm_logs.setLevel(logging.WARN)
        log.info('Initializing main app')
        
        self._dm = DeviceManager()
        self._dm.start()
        self._email = MagicHatEmail()
        self._email.start()
        self._data = MagicDatabase()
        self._asyncSerials = AsyncSerials(self._data)
        self._asyncSerials.start()
        self._data.load(APP_DIRS.user_data_dir)
        self.loaded = False
        self.exposed = ExposedMethods(self._asyncSerials, self._data, self._email, self, self._dm)

        log.info('Calling into superclass init')
        super(MainApp, self).__init__(**kwargs)
        log.info('Main app initialized')

    def OnInit(self):
        r = super(MainApp, self).OnInit()
        log.info('Constructing bindings...')

        bindings = cefpython.JavascriptBindings(
            bindToFrames=False, bindToPopups=True)
        bindings.SetObject("magichat", self.exposed)
        self.browser.SetJavascriptBindings(bindings)
        log.info('Bindings completed')
        return r

    def OnTimer(self, evt):
        super(MainApp, self).OnTimer(evt)

    def OnExit(self):
        super(MainApp, self).OnExit()
        self._email.die()
        self._asyncSerials.die()
        self._dm.die()
        self._dm.join()
        self._email.join()
        self._asyncSerials.join()

if __name__ == '__main__':
    log.info("%s", sys.version)
    sys.excepthook = ExceptHook

    # Application settings
    applicationSettings = {
        # Disk cache
        # "cache_path": "webcache/",

        "debug": False,
        "log_severity": cefpython.LOGSEVERITY_INFO,
        "log_file": os.path.join(APP_DIRS.user_data_dir, "debug.log"),
        "release_dcheck_enabled": False,

        "unique_request_context_per_browser": True,
        "downloads_enabled": True,
        "remote_debugging_port": 0 if DEBUG else -1,

        # Mouse context menu
        "context_menu": {
            "enabled": DEBUG,
            "navigation": DEBUG,
            "print": True,
            "view_source": DEBUG,
            "external_browser": False,
            "devtools": DEBUG,
        },

        "ignore_certificate_errors": False,
    }
    if not os.path.exists(APP_DIRS.user_data_dir):
        os.makedirs(APP_DIRS.user_data_dir)

    if os.path.exists(GetApplicationPath('subprocess.exe')):
        applicationSettings['browser_subprocess_path'] = GetApplicationPath('subprocess.exe')
    elif os.path.exists(GetApplicationPath('subprocess')):
        applicationSettings['browser_subprocess_path'] = GetApplicationPath('subprocess')
    elif os.path.exists(cefpython.GetModuleDirectory()+'/subprocess.exe'):
        applicationSettings['browser_subprocess_path'] = cefpython.GetModuleDirectory()+'/subprocess.exe'

    browserSettings = {
        "plugins_disabled": True,
        "file_access_from_file_urls_allowed": True,
        "universal_access_from_file_urls_allowed": True,
    }

    # Command line switches set programmatically
    g_switches = {
        # On Mac it is required to provide path to a specific
        # locale.pak file. On Win/Linux you only specify the
        # ApplicationSettings.locales_dir_path option.

        # "proxy-server": "socks5://127.0.0.1:8888",
        # "no-proxy-server": "",
        # "enable-media-stream": "",
        # "remote-debugging-port": "12345",
        # "disable-gpu": "",
        # "--invalid-switch": "" -> Invalid switch name
    }

    applicationSettings.update(magichat.AdditionalApplicationSettings())
    g_switches.update(magichat.AdditionalSwitches())

    cefpython.Initialize(applicationSettings, g_switches)
    log.info('Loading html from: %s', GetApplicationPath('html/index.html'))
    app = MainApp(
        index_page='file://'+GetApplicationPath('html/index.html'),
        app_settings=applicationSettings,
        browser_settings=browserSettings,)
    app.MainLoop()

    # Let App destructor do the cleanup before calling
    # cefpython.Shutdown(). This is to ensure reliable CEF shutdown.
    del app

    # Workaround to assist pyinstaller in cleaning up _MEIPASS :
    if hasattr(sys, '_MEIPASS'):
        if sys.platform != 'darwin': # cefpython shutdown is buggy on mac os x.
            cefpython.Shutdown()
            time.sleep(2)
