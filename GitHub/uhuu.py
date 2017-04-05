import threading
import time

# Event marking the GUI thread as having imported GTK.  GTK must not
# be imported before this event's flag is set.
gui_ready = threading.Event()

def run_gui_thread():
    import gobject
    gobject.threads_init()
    import gtk
    w = gtk.Window()
    global label
    global stop
    stop = False
    label = gtk.Label()
    w.add(label)
    w.show_all()
    w.connect("destroy", lambda _: koniec())
    gui_ready.set()
    gtk.main()

gui_thread = threading.Thread(target=run_gui_thread)
gui_thread.start()

# wait for the GUI thread to initialize GTK
gui_ready.wait()

# it is now safe to import GTK-related stuff
import gobject, gtk

def koniec():
	print "KOOOOOONIEC!"
	gobject.idle_add(gtk.main_quit)
	stop = True
	print stop


def update_label(maxSec):
	label.set_text("Counter: %i" % maxSec)
	pass

def countdown(maxSec):
    gobject.idle_add(update_label, maxSec)
    while maxSec > 0 and not stop:
    	print stop
        print maxSec
        time.sleep(0.0001)
        maxSec -= 1
        gobject.idle_add(update_label, maxSec)

    koniec()

worker = threading.Thread(target=countdown, args=(240,))
print 'starting work...'
worker.start()

# When both the worker and gui_thread finish, the main thread
# will exit as well.