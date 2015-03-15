import subprocess
import os

def get_version():
    p = subprocess.Popen('git describe --long'.split(), stdout=subprocess.PIPE)
    stdout = p.communicate()[0].strip()
    build_number = os.getenv('BUILD_NUMBER')
    major_minor, patch, gsha = stdout.split('-')
    major, minor = major_minor.split('.')
    if build_number is None:
        build_number = '0'
    return major[1:], minor, patch, build_number, gsha
    
    
def print_version(version):
    str_version = '.'.join(version)
    os.putenv('BUILD_NUMBER', str_version)
    with file('version.txt', 'wb') as f:
        f.write(str_version)
    print "##teamcity[buildNumber '%s']" % str_version