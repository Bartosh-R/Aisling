import cairo
from gi.repository import Gtk, Gdk

class Window (Gtk.Window):

	label = Gtk.Label("""Hello World""")
	current = 0
	words = []

	def __init__(self, words):
		super(Window, self).__init__()

		self.words = words
		self.set_word(words[self.current])

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
		box.add(self.label)

		self.add(box)
		self.set_app_paintable(True)
		self.add_events(Gdk.EventMask.SCROLL_MASK)
		self.connect("draw", self.area_draw)
		self.connect("button-press-event", self.quit)
		self.connect("scroll-event", self.scroll)
		self.show_all()

	def set_word(self, word):
		self.label.set_justify(Gtk.Justification.FILL)
		self.label.set_markup("<span foreground=\"white\" size=\"x-large\">"+word+"</span>")

	def scroll(self, widget, event):
		if event.direction == 1 and self.current > 0: # scroll_down
			self.current -= 1
			self.set_word(self.words[self.current])
		elif event.direction == 0 and self.current < len(self.words)-1:
			self.current += 1
			self.set_word(self.words[self.current])

	def quit(self, widget, event):
		print "Agrrrr"
		self.destroy()
		Gtk.main_quit()

	def area_draw(self, widget, cr):
		cr.set_source_rgba(.2, .2, .2, 0.9)
		cr.set_operator(cairo.OPERATOR_SOURCE)
		cr.paint()
		cr.set_operator(cairo.OPERATOR_OVER)
