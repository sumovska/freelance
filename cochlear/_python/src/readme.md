Magic Hat:
==========

Build Requirements:

1. The version of Visual Studio used to compile python, available at http://aka.ms/vcpython27
2. Python 2.7, available at https://www.python.org/downloads/  Make sure you use the 32-bit version.
3. Pip, use the provided get_pip.py script to get this.
4. pip install cython, you may need to use the Visual C++ 2008 32-bit Command Prompt for this.
5. pip install hidapi, which is a cython-based wrapper for hidapi. Again the VC++ command prompt might be needed.

I don't know if you need hidapi itself, I compiled this using VS 2013, but this was in an attempt to get hidapi-cffi
to work, but it didn't, so I used hidapi instead (which uses cython instead)
 - hidapi (for python) seems to embed the hidapi (for C) so there doesn't seem to be a need to include hibapi.dll.

Running:

This early version is very simple:  Run cr2xx.py, and then plug in the cr220.  Then unplug it.
Then plug it in again.
Then unplug it.
Try another CR220 device, plug it in.

Also works for CR230 devices, however they do have a different PID. (CR220 is 0x0fb8, CR230 is 0x0fb7)


