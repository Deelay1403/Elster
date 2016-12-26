import pygtk
pygtk.require('2.0')
import gtk

class battery:

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
		# When the window is given the "delete_event" signal (this is given
		# by the window manager, usually by the "close" option, or on the
		# titlebar), we ask it to call the delete_event () function
		# as defined above. The data passed to the callback
		# function is NULL and is ignored in the callback function.
		self.window.connect("delete_event", self.delete_event)
    
		# Here we connect the "destroy" event to a signal handler.  
		# This event occurs when we call gtk_widget_destroy() on the window,
		# or if we return FALSE in the "delete_event" callback.
		self.window.connect("destroy", self.destroy)
	    
		# Sets the border width of the window.
		self.window.set_border_width(100)
		self.hbox = gtk.HBox()
		self.hbox.show()
		self.window.add(self.hbox)
		# Creates a new button with the label "Hello World".
		#self.button = gtk.Button("Hello World")
    
		# When the button receives the "clicked" signal, it will call the
		# function hello() passing it None as its argument.  The hello()
		# function is defined above.
		#self.button.connect("clicked", self.hello, None)
    
		# This will cause the window to be destroyed by calling
		# gtk_widget_destroy(window) when "clicked".  Again, the destroy
		# signal could come from here, or the window manager.
		#self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
    
		# This packs the button into the window (a GTK container).
		#self.window.add(self.button)
    
		# The final step is to display this newly created widget.
		#self.button.show()
    
    	# and the window


		print "OK"

	def __call__(self):
		print "domyslna"

	def hello(self, widget, data=None):
		print "Hello World"

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
		self.image = gtk.Image()
		obraz = "./batt" + str(ID) + ".png"
		print(obraz)
		self.image.set_from_file(obraz)
		self.image.show()
		# a button to contain the image widget
		self.button = gtk.Button()
		self.button.add(self.image)
		self.button.show()
		self.hbox.pack_start(self.button)
		self.button.connect("clicked", self.hello, "2")

		print ID
		pass


	def show(self):
		self.window.show()
 		gtk.main()
		pass

if __name__ == "__main__":
	aktor1 = battery()
	#aktor1()
	aktor1.info(5)
	aktor1.info(2)
	aktor1.show()
	#aktor1.hello(98)