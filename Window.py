import cairo
from gi.repository import Gtk, Gdk

class Window (Gtk.Window):



    def __init__(self, word):
        super(Window, self).__init__()
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_keep_above(True)
        self.set_decorated(False)
        self.set_border_width(30)
        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        if self.visual != None and self.screen.is_composited():
            print "yay"
            self.set_visual(self.visual)

        box = Gtk.Box()
        label = Gtk.Label("""Hello World""")
        label.set_markup("<span foreground=\"white\" size=\"x-large\">"+word+"</span>")
        #label.connect("button_press_event", self.quit)
        box.add(label)
        self.add(box)

        self.set_app_paintable(True)
        self.connect("draw", self.area_draw)
        self.connect("button_press_event", self.quit)
        self.show_all()

    def show_word(self, word):
        self.show_all()
        print "hello"

    def quit(self, widget, event):
        print "Agrrrr"
        self.destroy()
        Gtk.main_quit()

    def area_draw(self, widget, cr):
        cr.set_source_rgba(.2, .2, .2, 0.9)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

#Window("Woda vytautas")
#Gtk.main()