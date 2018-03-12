import Queue
from threading import Thread
import time
import gobject
import gtk

gobject.threads_init()

class MyThread(Thread):
 def __init__(self):
     super(MyThread, self).__init__()
     self.label = gtk.Label()
     self.quit = False
     self.queue = Queue.Queue()

     w = gtk.Window()
     w.add(self.label)
     w.show_all()
     w.connect("destroy", lambda _: self.stop())

 def update_label(self, counter):
     self.label.set_text("Counter: %i" % counter)
     return False

 def start(self):
     super(MyThread, self).start()
     gtk.main()
     pass

 def stop(self):
     gtk.main_quit()
     self.quit = True
     pass

 def run(self):
     counter = 0
     while not self.quit:
         try:
             daneOdebrane = q.get_nowait()
             if  (daneOdebrane[0] == "STOP_LISTENING"):
                 print "STOP!"
                 break
         except Exception:
             daneOdebrane = ["brak", "danych"]
         counter += 1
         gobject.idle_add(self.update_label, counter)
         self.pisz()
         time.sleep(0.00001)

 def pisz(self):
     print "KUPA"


t = MyThread()
t.start()

# import threading
# import multiprocessing
# import time
# import gobject
# import gtk

# gtk.gdk.threads_init()

# class MyThread(multiprocessing.Process):
#  def __init__(self):
#      super(MyThread, self).__init__()
#      self.label = gtk.Label()
#      self.quit = False

#      w = gtk.Window()
#      w.add(self.label)
#      w.show_all()
#      w.connect("destroy", lambda _: self.stop())

#  def update_label(self, counter):
#     gtk.threads_enter()
#     try:
#         self.label.set_text("Counter: %i" % counter)
#     finally:
#         gtk.threads_leave()
#     return False

#  def start(self):
#      super(MyThread, self).start()
#      gtk.threads_enter()
#      gtk.main()
#      gtk.threads_leave()
#      pass

#  def stop(self):
#      gtk.main_quit()
#      self.quit = True
#      pass

#  def run(self):
#      counter = 0
#      while not self.quit:
#          counter += 1
#          #gobject.idle_add(self.update_label, counter)
#          self.update_label(counter)
#          self.pisz()
#          time.sleep(2)

#  def pisz(self):
#      print "KUPA"

# if __name__ == '__main__':
#     t = MyThread()
#     t.start()


# import threading
# import time
# import gobject
# import gtk

# gobject.threads_init()

# class MyThread(threading.Thread):
#  def __init__(self):
#      super(MyThread, self).__init__()
#      self.label = gtk.Label()
#      self.quit = False

#      w = gtk.Window()
#      w.add(self.label)
#      w.show_all()
#      w.connect("destroy", lambda _: self.stop())

#  def update_label(self, counter):
#      self.label.set_text("Counter: %i" % counter)
#      return False

#  def start(self):
#      super(MyThread, self).start()
#      gtk.main()
#      pass

#  def stop(self):
#      gtk.main_quit()
#      self.quit = True
#      pass

#  def run(self):
#      counter = 0
#      while not self.quit:
#          counter += 1
#          gobject.idle_add(self.update_label, counter)
#          self.pisz()
#          time.sleep(0.00001)

#  def pisz(self):
#      print "KUPA"


# t = MyThread()
# t.start()


# import threading
# import time
# import gobject
# import gtk

# gobject.threads_init()

# class MyThread(threading.Thread):
#  def __init__(self, label):
#      super(MyThread, self).__init__()
#      self.label = label
#      self.quit = False

#  def update_label(self, counter):
#      self.label.set_text("Counter: %i" % counter)
#      return False

#  def run(self):
#      counter = 0
#      while not self.quit:
#          counter += 1
#          gobject.idle_add(self.update_label, counter)
#          self.pisz()
#          time.sleep(0.00001)

#  def pisz(self):
#      print "KUPA"

# w = gtk.Window()
# l = gtk.Label()
# w.add(l)
# w.show_all()
# w.connect("destroy", lambda _: gtk.main_quit())
# t = MyThread(l)
# t.start()

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
