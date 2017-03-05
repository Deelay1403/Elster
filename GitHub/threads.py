from threading import Thread
from multiprocessing import Process
from time import sleep

def background():
    while True:
        print "KUPA"
        sleep(1)

def foreground():
    while True:
        print "KKKKK"
        sleep(2)

b = Process(name='background', target=background())
f = Process(name='foreground', target=foreground())

b.start()
f.start()

while  True:
    print "JAK!?"
    sleep(3)

print "ale to sie nie wyprintuje!" #xD nawet pycharm się wkurwia