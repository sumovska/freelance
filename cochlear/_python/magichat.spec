# -*- mode: python -*-
from cefpython3 import cefpython
try:
    from PyInstaller.utils import versioninfo as VI
except ImportError:
    pass
import os
import sys
import boto

DARWIN = 'darwin'

a = Analysis(['src/magichat.py'],
             pathex=['/Users/johnchapman/dev/magichat/src'],
             hiddenimports=[
                 # Hidden imports from cefpython:
                 'json', 'json.decoder', 'json.scanner', 'json.encoder',
                 # Hidden imports from xhtml2pdf
                 'reportlab.rl_settings'],
             hookspath=None,
             runtime_hooks=None)

html = Tree('src/html', prefix='html')

if sys.platform == DARWIN:
    libcef_dylib = os.path.join(os.path.dirname(cefpython.__file__), 'libcef.dylib')
    assert os.path.exists(libcef_dylib)
    resources = Tree(os.path.join(os.path.dirname(cefpython.__file__), 'Resources'), prefix='Resources')
    subprocess_exe = os.path.join(os.path.dirname(cefpython.__file__), 'subprocess')
    for x in list(a.binaries):
        if 'libwx' in x[1]:
            a.binaries.remove(x)

    additional_datas = [
                   ['cefpython3/libcef.dylib', libcef_dylib, 'BINARY'],
                   ['subprocess', subprocess_exe, 'BINARY']]
else:
    libcef_dylib = os.path.join(os.path.dirname(cefpython.__file__), 'libcef.dll')
    assert os.path.exists(libcef_dylib)
    resources = Tree(os.path.dirname(cefpython.__file__), prefix='')
    subprocess_exe = os.path.join(os.path.dirname(cefpython.__file__), 'subprocess.exe')
    cefclient = os.path.join(os.path.dirname(cefpython.__file__), 'cefclient.exe')

    additional_datas = [
    		   ['boto/endpoints.json', os.path.dirname(boto.__file__)+'/endpoints.json', 'DATA'],
    		   ['boto/cacerts/cacerts.txt', os.path.dirname(boto.__file__)+'/cacerts/cacerts.txt', 'DATA'],
                   ['hid.pyd', 'dependencies/hid.pyd', 'BINARY'],
                   ['subprocess.exe', subprocess_exe, 'DATA'],
                   ['cefclient.exe', cefclient, 'DATA']]
    a.binaries = [x for x in a.binaries if 'wx' not in x[1]]
    a.datas = [x for x in a.binaries if 'include' not in x[1]]
    for x in list(a.pure):
        if 'wx' in x[1]:
            a.pure.remove(x)

    locales = []
    dlls = []
    for x in list(resources):
        if x[0].endswith('.dll'):
            if x[0] not in [z[0] for z in a.datas]:
                dlls.append(x)
        elif 'locales' in x[0]:
            locales.append(x)

pyz = PYZ(a.pure)

if sys.platform == DARWIN:
    exe = EXE(pyz,
              a.scripts,
              exclude_binaries=True,
              name='magichat',
              debug=False,
              strip=None,
              upx=False,
              console=False)

    coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               additional_datas,
               resources,
               html,
               strip=None,
               upx=False,
               name='magichat')

    app = BUNDLE(coll,
             name='MagicHat.app')

else:
    with file('version.txt', 'rb') as f:
        VERSION = f.read().strip().split('.')
    VERSION_INFO = VI.VSVersionInfo(
        ffi=VI.FixedFileInfo(
            filevers=[int(x) for x in VERSION[:4]],
            prodvers=[int(x) for x in VERSION[:4]],
            mask=0x3f,
        flags=0x0,
            OS=0x40004,
            fileType=0x1,
            subtype=0x0,
            date=(0, 0)
        ),
        kids=[
            VI.StringFileInfo(
                [
                    VI.StringTable(
                        u'040904B0',
                        [
                            VI.StringStruct(u'CompanyName', u'Cochlear Limited'),
                            VI.StringStruct(u'FileDescription', u'Magic Hat'),
                            VI.StringStruct(u'FileVersion', unicode('.'.join(VERSION))),
                            VI.StringStruct(u'InternalName', u'MagicHat'),
                            VI.StringStruct(u'LegalCopyright', u'\xa9 Cochlear Limited. All rights reserved.'),
                            VI.StringStruct(u'OriginalFilename', u'MagicHat.exe'),
                            VI.StringStruct(u'ProductName', u'Magic Hat'),
                            VI.StringStruct(u'ProductVersion', unicode('.'.join(VERSION))),
                        ],
                    ),
                ]),
            VI.VarFileInfo([VI.VarStruct(u'Translation', [1033, 1200])])
        ]
    )


    exe = EXE(pyz,
              a.scripts,
              exclude_binaries=1,
              name='magichat.exe',
              debug=False,
              strip=None,
              upx=False,
               cdict={},
              console=True)

    dist = COLLECT(exe,
               a.binaries,
               a.datas,
               additional_datas,
               dlls,
               html,
               locales,
               strip=None,
               upx=False,
               cdict={},
               name='magichat')

    exe = EXE(pyz,
              a.scripts,
               a.binaries,
               a.datas,
               additional_datas,
               dlls,
               html,
               locales,
               cdict={},
              exclude_binaries=0,
              name='magichat.exe',
              debug=False,
              strip=None,
              upx=False,
              version=VERSION_INFO,
              console=False)
