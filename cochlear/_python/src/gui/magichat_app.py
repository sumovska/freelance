# Just a bit of indirection to clarify the magichat.py entry point
# First attempt to import the native win32 environment.
# IF that fails, then try the generic wx environment.
import mh_logging as logging
log = logging.getLogger(__name__)
try:
    log.info('Attempting to load native win32 environment')
    import win32con
    import win32gui
    import win32api
    import gui.win32_magichat as magichat
    log.info('Native win32 magichat imported')
except ImportError:
    log.info('Could not import native win32 environment, falling back to wx')
    log.info('Attempting to import wx')
    import wx
    import gui.wx_magichat as magichat
    log.info('Cross platform WX magichat imported')
