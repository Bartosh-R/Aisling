from gi.repository import Gtk, Gdk
from Xlib.display import Display
from Xlib import X,XK

from Extractor import Extractor
from Window import Window

import time
import sys


Q_code = 24
W_code = 25


def handle_event(aEvent):
    keycode = aEvent.detail
    if aEvent.type == X.KeyPress:
        if keycode == 24:
           	show_window()
        elif keycode == 25:
         	sys.exit(1)

def getSelection():
    clip = Gtk.Clipboard.get (Gdk.SELECTION_PRIMARY)
    text=clip.wait_for_text ()
   # text=text.encode("utf-8")
    #print text 
    return text

def show_window():
    selection = getSelection()
    ext = Extractor(selection)
    
    Window(ext.words[0])
    Gtk.main()
    #print ext.words

def main():
    # current display
    disp = Display()
    root = disp.screen().root

    # we tell the X server we want to catch keyPress event
    root.change_attributes(event_mask = X.KeyPressMask)

    """keysym = XK.string_to_keysym("E")
    keycode = disp.keysym_to_keycode(keysym)"""


    root.grab_key(Q_code, X.ControlMask, X.NONE ,X.GrabModeAsync, X.GrabModeAsync)
    root.grab_key(W_code, X.ControlMask, X.NONE, X.GrabModeAsync, X.GrabModeAsync)

    while 1:
        event = root.display.next_event()
        handle_event(event)

if __name__ == '__main__':
    main()