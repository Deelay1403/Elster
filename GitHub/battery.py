import pygtk
pygtk.require('2.0')
import gtk

class battery:

	def __init__(self):
		self.level = 0
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
	   
	def __call__(self):
		self.show()

	def add(self, ID):
		self.battery = gtk.VBox(gtk.FALSE, 1)

		self.baterry_icon = gtk.Image()
		self.obraz = "./battW" + str(6) + ".png"
		self.baterry_icon.set_from_file(self.obraz)
		self.baterry_icon.show()
		    
		self.baterry_ID_label = gtk.Label("Bateria " + str(ID))
		self.baterry_ID_label.show()
		self.baterry_poziom_label = gtk.Label("100%")
		self.baterry_poziom_label.show()

		self.battery.add(self.baterry_icon)
		self.battery.add(self.baterry_ID_label)
		self.battery.add(self.baterry_poziom_label)

		self.battery.show()

		self.window.add(self.battery)

	def delete_event(self, widget, event, data=None):
		# If you return FALSE in the "delete_event" signal handler,
		# GTK will emit the "destroy" signal. Returning TRUE means
		# you don't want the window to be destroyed.
		# This is useful for popping up 'are you sure you want to quit?'
		# type dialogs.
		print "delete event occurred"

		# Change FALSE to TRUE and the main window will not be destroyed
		# with a "delete_event".
		return False

	def destroy(self, widget, data=None):
		print "destroy signal occurred"
		gtk.main_quit()

	def info(self, ID):
		# a horizontal box to hold the buttons
	

		# create several images with data from files and load images into
		# buttons
		if ID == 0:
			self.ID_OLD = 6
		else:
			self.ID_OLD = ID

		self.ID_OLD = ID
		self.image = gtk.Image()
		self.update(1, ID)
		self.image.show()
		# a button to contain the image widget
		self.button = gtk.Button()
		self.button.add(self.image)
		self.button.show()
		self.hbox.pack_start(self.button)
		self.button.connect("clicked", self.update, ID)

		print ID
		pass

	def update(self, ok, level):
		if self.level == 0:
			self.level = level
		print level
		self.level_old = self.level - 1
		self.level = self.level_old

		obraz = "./batt" + str(self.level) + ".png"
		print(obraz)
		self.image.set_from_file(obraz)
		pass


	def show(self):
		self.window.show()
 		gtk.main()
		pass

if __name__ == "__main__":
	bateria = battery()
	bateria.add(5)
	bateria.add(7)
	bateria.show()