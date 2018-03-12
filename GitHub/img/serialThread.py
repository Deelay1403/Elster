
import threading
import time
from multiprocessing import Process
#
# class serialThread:
#     def __init__():
#         print ""
#
#     def __call__(self):
#         self.show()
#
#     def add(self, ID, name):
#
#     def hideWindow(self):
#         self.window.hide()
#
#     def showWindow(self):
#         self.window.show()


def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

def loop1():
    while(True):
        print "1 Wlaczam sie co 1s"
        time.sleep(1)
def loop2():
    while(True):
        print "2 Wlaczam sie co 0.5s"
        time.sleep(0.5)
def loop3():
    while(True):
        print "1 Wlaczam sie co 0.2s"
        time.sleep(0.2)
def loop4():
    while(True):
        print "2 Wlaczam sie co 0.00001s"
        time.sleep(0.00001)


p1 = Process(target=loop1)
p2 = Process(target=loop2)
p3 = Process(target=loop3)
p4 = Process(target=loop4)

p1.start()
p2.start()
p3.start()
p4.start()
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()