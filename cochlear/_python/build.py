#!/usr/bin/python
#
# This is the build script for MagicHat.
#

import subprocess
import shutil
import json
import os
import sys
import tempfile
import logging
from version import get_version, print_version
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('build')
puts = lambda *x: log.info('%s', ' '.join(str(x) for x in x))

VERSION = get_version()
print_version(VERSION)

def call(*args, **kwargs):
    print args
    r = subprocess.call(*args, **kwargs)
    if r != 0:
        raise Exception('Subprocess failed with error: ' + str(r))


def activate(venv):
    activate = venv+'/bin/activate_this.py'
    if os.path.exists(activate):
        execfile(activate, globals())
    activate = venv+'/Scripts/activate_this.py'
    if os.path.exists(activate):
        execfile(activate, globals())

def setup(venv, create=True):
    if create:
        puts("Constructing virtualenv in", venv)
        call([sys.executable, "dependencies/virtualenv/virtualenv.py", '--no-setuptools', venv])

    activate(venv)
    shutil.copyfile('dependencies/hid.pyd', 'src/hid.pyd')

    puts('Ensuring that pip exists...')
    call([PYTHON, 'dependencies/get-pip.py'])
    if sys.platform != 'win32':
        puts('Ensuring that cython is installed. There are strange issues if installed as part of requirements.txt...')
        call([PYTHON, '-m', 'pip', 'install', 'cython==0.21.2'])
        puts('And now that we have cython, lets install hidapi')
        call([PYTHON, '-m', 'pip', 'install', 'hidapi==0.7.99-5'])

    puts('Ensuring that all other dependencies exist...')
    call([PYTHON, '-m', 'pip', 'install', '-r', 'requirements.txt'])

    if sys.platform == 'win32':
        try:
            call([EASYINSTALL, 'dependencies/pywin32-219.win32-py2.7.exe'])
        except:
            puts('There was an error installing pywin32, perhaps it was already installed. Continuing regardless')
            

def test(venv):
    puts('Performing tests')
    call([PYTHON, '-m', 'coverage', 'run', '-m', 'tests.runner'], cwd='src')
    call([PYTHON, '-m', 'coverage', 'report', '--omit', '*site-packages*,cochlear*,generated*'], cwd='src')


def build(venv):
    puts('Generating platform installer')
    call([PYINSTALLER, 'magichat.spec', '-y', '--onefile', '--windowed'])



def publish(venv):
    import os
    import shutil
    host = 'aum-filesrv01.cochlear.com'
    source_file = './dist/magichat.exe'
    target_file = '\\\\'+host+'\\Software\\Builds\\MagicHat\\{0}-magichat.exe'.format('.'.join(get_version()))
    
    import hashlib
    m = hashlib.sha1()
    with file(source_file, 'rb') as f:
        m.update(f.read())
    with file(source_file+'.sha1', 'wb') as f:
        f.write("{0}  {1}".format(m.hexdigest(), source_file.split('/')[-1]))
    
    os.system("net use x: \\\\{host}\\Software /user:{username} {password}".format(
        host=host,
        username=os.getenv('FILESHARE_USERNAME'),
        password=os.getenv('FILESHARE_PASSWORD')))
    try:
        shutil.copy(source_file, target_file)
        shutil.copy(source_file+'.sha1', target_file+'.sha1')
        
        print "##teamcity[setParameter name='artifactPath' value='{0}']".format(target_file)
    finally:
        os.system("net use x: /d")

explicit_venv = sys.argv[-1] if os.path.isdir(sys.argv[-1]) else ''
tempdir = None
try:
    if explicit_venv:
        venv = explicit_venv
    else:
        venv = tempdir = tempfile.mkdtemp()

    venv = os.path.abspath(venv)
    if sys.platform == 'win32':
        PYTHON = venv+'/Scripts/python.exe'
        PYINSTALLER = venv+'/Scripts/pyinstaller.exe'
        EASYINSTALL = venv+'/Scripts/easy_install.exe'
    else:
        PYTHON = venv+'/bin/python'
        PYINSTALLER = venv+'/bin/pyinstaller'

    setup(venv, bool(tempdir))

    test(venv)
    if '--nobuild' not in sys.argv:
        build(venv)
        try:
            publish(venv)
        except Exception, e:
            print e
finally:
    if tempdir:
        shutil.rmtree(tempdir)
    os.remove('src/hid.pyd')
