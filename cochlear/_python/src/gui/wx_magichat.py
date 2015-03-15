from __future__ import unicode_literals

import gui.import_this_first
from cefpython3 import cefpython

import sys
import wx
import time
import re
import uuid
import platform
import inspect
import struct

from path_utils import GetApplicationPath
from error_handling import ExceptHook

import mh_logging as logging

log = logging.getLogger(__name__)

g_applicationSettings = None
g_browserSettings = None
g_countWindows = 0

# Which method to use for message loop processing.
#   EVT_IDLE - wx application has priority (default)
#   EVT_TIMER - cef browser has priority
# It seems that Flash content behaves better when using a timer.
# IMPORTANT! On Linux EVT_IDLE does not work, the events seems to
# be propagated only when you move your mouse, which is not the
# expected behavior, it is recommended to use EVT_TIMER on Linux,
# so set this value to False.
USE_EVT_IDLE = False

def AdditionalApplicationSettings():
    return {
        "resources_dir_path": cefpython.GetModuleDirectory()+"/Resources",
        "browser_subprocess_path": "%s/%s" % (
            cefpython.GetModuleDirectory(), "subprocess"),
    }

def AdditionalSwitches():
    return {
        "locale_pak": cefpython.GetModuleDirectory()
            +"/Resources/en.lproj/locale.pak"
        }

class MainFrame(wx.Frame):
    mainPanel = None
    _created = False

    @property
    def browser(self):
        if self._created:
            return cefpython.GetBrowserByWindowHandle(self.mainPanel.GetHandle())

    def __init__(self, url):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title='wxPython CEF 3 example', size=(800,600))

        self.CreateMenu()

        # Cannot attach browser to the main frame as this will cause
        # the menu not to work.
        # --
        # You also have to set the wx.WANTS_CHARS style for
        # all parent panels/controls, if it's deeply embedded.
        self.mainPanel = wx.Panel(self, style=wx.WANTS_CHARS)

        windowInfo = cefpython.WindowInfo()
        (width, height) = self.mainPanel.GetClientSizeTuple()
        windowInfo.SetAsChild(self.mainPanel.GetHandle(),
                              [0, 0, width, height])

        cefpython.SetGlobalClientCallback("OnAfterCreated",
                self.OnAfterCreated)

        browser = cefpython.CreateBrowserSync(
            windowInfo,
            browserSettings=g_browserSettings,
            navigateUrl=url)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        if USE_EVT_IDLE:

            self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnAfterCreated(self, browser):
        self._created = True

    def CreateMenu(self):
        filemenu = wx.Menu()
        filemenu.Append(1, "Open")
        exit = filemenu.Append(2, "Exit")
        self.Bind(wx.EVT_MENU, self.OnClose, exit)
        aboutmenu = wx.Menu()
        aboutmenu.Append(1, "CEF Python")
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File")
        menubar.Append(aboutmenu, "&About")
        self.SetMenuBar(menubar)

    def OnClose(self, event):
        # Remove all CEF browser references so that browser is closed
        # cleanly. Otherwise there may be issues for example with cookies
        # not being flushed to disk when closing app immediately
        # (Issue 158).
        browser = cefpython.GetBrowserByWindowHandle(self.mainPanel.GetHandle())
        event.Skip()
        cefpython.QuitMessageLoop()

        self.Destroy()

    def OnIdle(self, event):
        cefpython.MessageLoopWork()


class MainApp(wx.App):
    timer = None
    timerID = 1
    timerCount = 0

    @property
    def browser(self):
        return self.frame.browser

    def __init__(self, index_page, app_settings, browser_settings):
        global g_applicationSettings
        global g_browserSettings
        g_applicationSettings = app_settings
        g_browserSettings = browser_settings
        self._index_page = index_page
        super(MainApp, self).__init__(False)

    def get_save_location(self, message, wildcard):
        dlg = wx.FileDialog(self.frame,
                            message=message,
                            wildcard=wildcard,
                            style=wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            return dlg.GetPath()


    def OnInit(self):
        if not USE_EVT_IDLE:
            self.CreateTimer()
        self.frame = MainFrame(self._index_page)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def CreateTimer(self):
        # See "Making a render loop":
        # http://wiki.wxwidgets.org/Making_a_render_loop
        # Another approach is to use EVT_IDLE in MainFrame,
        # see which one fits you better.
        self.timer = wx.Timer(self, self.timerID)
        self.timer.Start(10) # 10ms
        wx.EVT_TIMER(self, self.timerID, self.OnTimer)

    def OnTimer(self, event):
        self.timerCount += 1
        #print("[wxpython.py] OnTimer() %d" % self.timerCount)
        cefpython.MessageLoopWork()

    def OnExit(self):
        # When app.MainLoop() returns, MessageLoopWork() should
        # not be called anymore.
        if not USE_EVT_IDLE:
            self.timer.Stop()
