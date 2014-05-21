import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

sendmessage("Simpla - handy translator")

import sys
import os
try:
    libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib'))
    sys.path.insert(0, libdir)
except:
    # probably running inside py2exe which doesn't set __file__
    pass

import main
main.main()