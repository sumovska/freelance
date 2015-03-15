import appdirs
import os
try:
    import win32com.client
except ImportError:
    pass # Obviously ain't windows.

class AppDirs(appdirs.AppDirs):
    @property
    def user_documents(self):
        if os.name == 'posix':
            return os.path.expanduser("~/Documents")
        else:
            # Assume windows, useful links:
            # https://en.wikipedia.org/wiki/Windows_Script_Host
            # https://technet.microsoft.com/en-us/library/ee156616.aspx
            wsh = win32com.client.Dispatch("WScript.Shell")
            return wsh.SpecialFolders("MyDocuments")
