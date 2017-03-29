import threading
import time
import gobject
import gtk

gobject.threads_init()

class MyThread(threading.Thread):
 def __init__(self):
     super(MyThread, self).__init__()
     w = gtk.Window()
     self.label = gtk.Label()
     self.quit = False
     w.add(self.label)
     w.connect("destroy", lambda _: gtk.main_quit())
     w.show_all()

 def update_label(self, counter):
     self.label.set_text("Counter: %i" % counter)
     return False

 def run(self):
     counter = 0
     while not self.quit:
         counter += 1
         gobject.idle_add(self.update_label, counter)
         self.pisz()
         time.sleep(0.00001)

 def pisz(self):
     print "KUPA"

t = MyThread()
t.start()

gtk.main()
t.quit = True

# import threading
# import time
# import gobject
# import gtk
#
# gobject.threads_init()
#
# class MyThread(threading.Thread):
#  def __init__(self, label):
#      super(MyThread, self).__init__()
#      self.label = label
#      self.quit = False
#
#  def update_label(self, counter):
#      self.label.set_text("Counter: %i" % counter)
#      return False
#
#  def run(self):
#      counter = 0
#      while not self.quit:
#          counter += 1
#          gobject.idle_add(self.update_label, counter)
#          self.pisz()
#          time.sleep(0.00001)
#
#  def pisz(self):
#      print "KUPA"
#
# w = gtk.Window()
# l = gtk.Label()
# w.add(l)
# w.show_all()
# w.connect("destroy", lambda _: gtk.main_quit())
# t = MyThread(l)
# t.start()
#
# gtk.main()
# t.quit = True

# import threading
# import time
# import gobject
# import gtk

# gobject.threads_init()

# class licz:
#  def __init__(self):
#      self.quit = False
#      w = gtk.Window()
#      l = gtk.Label()
#      w.add(l)
#      w.show_all()
#      self.label = l
#      w.connect("destroy", lambda _: gtk.main_quit())

#  def update_label(self, counter):
#      self.label.set_text("Counter: %i" % counter)
#      return False

#  def run(self):
#      counter = 0
#      while not self.quit:
#          counter += 1
#          gobject.idle_add(self.update_label, counter)
#          time.sleep(0.0000001)

#  def startT(self):
#     gtk.threads_enter()
#     gtk.main()
#     gtk.threads_leave()

# def xD():
#     global t
#     t = licz()
#     t.startT()
#     print "DZIALA!"

# popcorn = threading.Thread(target=xD, name="Battery").start()

# print "chujjj"
