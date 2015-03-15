# IMPORTANT - importing CEF Python
# --------------------------------------------------------------
# The cefpython library must be the very first library imported.
# This is because CEF was compiled with the tcmalloc memory
# allocator which hooks globally and replaces the default
# malloc allocator. If memory was allocated using malloc and
# then freed using tcmalloc then this would result in random
# segmentation faults in an application. See Issue 155 which
# is to provide CEF builds on Mac with tcmalloc disabled:
# https://code.google.com/p/cefpython/issues/detail?id=155

import ctypes, os, sys

libcef_so = os.path.join(os.path.dirname(os.path.abspath(__file__)),\
        'libcef.dylib')
libcef_dll = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'libcef.dll')
if os.path.exists(libcef_so):
    # Import a local module
    ctypes.CDLL(libcef_so, ctypes.RTLD_GLOBAL)
    if 0x02070000 <= sys.hexversion < 0x03000000:
        import cefpython_py27 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
elif os.path.exists(libcef_dll) or (hasattr(sys, 'frozen') and sys.platform == 'win32'):
    # Import a local module
    if (2,7) <= sys.version_info < (2,8):
        from cefpython3 import cefpython_py27 as cefpython
    elif (3,4) <= sys.version_info < (3,4):
        import cefpython_py34 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
else:
    # Import an installed package
    from cefpython3 import cefpython
