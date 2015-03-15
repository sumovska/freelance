from cefpython3 import cefpython
import cefwindow
import win32con
import win32gui
import win32api
import time
import sys
from path_utils import GetApplicationPath
from gui.error_handling import ExceptHook

import os
import mh_logging as logging

DEBUG = not hasattr(sys, 'frozen')
log = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Helper functions.

Log = lambda x: log.info('%s', x)


def CloseWindow(windowHandle, message, wparam, lparam):
    browser = cefpython.GetBrowserByWindowHandle(windowHandle)
    browser.CloseBrowser()
    return win32gui.DefWindowProc(windowHandle, message, wparam, lparam)

def QuitApplication(windowHandle, message, wparam, lparam):
    win32gui.PostQuitMessage(0)
    return 0

def GetPywin32Version():
    fixed_file_info = win32api.GetFileVersionInfo(win32api.__file__, '\\')
    return fixed_file_info['FileVersionLS'] >> 16
    
def AdditionalSwitches():
    return {}
    
def AdditionalApplicationSettings():
    return {}
    
class MainApp(object):

    @property
    def browser(self):
        return cefpython.GetBrowserByWindowHandle(self.handle)
        
    def __init__(self, index_page, app_settings, browser_settings):
        log.debug('MainApp.__init__(...)')
        self._index_page = index_page
        self._application_settings = app_settings
        self._browser_settings = browser_settings
        
    def get_save_location(self, message, wildcard):
        try:
            (filename, str2, int1) = win32gui.GetSaveFileNameW(
                self.handle,
                hInstance=None,
                Filter=wildcard.replace(',', '\0')+'\0',
                CustomFilter=None,
                FilterIndex=0,
                File='',
                MaxFile=1024,
                InitialDir=None,
                Title=message,
                Flags=0,
                DefExt=".pdf",
                TemplateName=None)
            log.info('SaveFileDialog returned (%s, %s, %d)', filename, str2, int1)
            return filename
        except Exception, e:
            log.error(e)
            
        
    def MainLoop(self):
        cefwindow.g_debug = self._application_settings['debug']

        wndproc = {
            win32con.WM_CLOSE: CloseWindow,
            win32con.WM_DESTROY: QuitApplication,
            win32con.WM_SIZE: cefpython.WindowUtils.OnSize,
            win32con.WM_SETFOCUS: cefpython.WindowUtils.OnSetFocus,
            win32con.WM_ERASEBKGND: cefpython.WindowUtils.OnEraseBackground
        }

        if os.path.exists("icon.ico"):
            icon = os.path.abspath("icon.ico")
        else:
            icon = ""

        windowHandle = cefwindow.CreateWindow(title="Magic Hat",
                className="cefpython3_example", width=1024, height=768,
                icon=icon, windowProc=wndproc)
        windowInfo = cefpython.WindowInfo()
        windowInfo.SetAsChild(windowHandle)
        browser = cefpython.CreateBrowserSync(windowInfo, self._browser_settings,
            navigateUrl=self._index_page)
        self.handle = windowHandle
        self.OnInit()
        cefpython.MessageLoop()
        self.OnExit()
        
    def OnInit(self, evt=None):
        pass
        
    def OnExit(self, evt=None):
        pass