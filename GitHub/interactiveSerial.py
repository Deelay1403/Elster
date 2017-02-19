import pygtk

pygtk.require('2.0')
import gtk
from time import sleep

class interactiveSerial:
    def __init__(self):
        self.check = "nieOk"
        print "inicjacja zakonczona"

    def startLoop(self):
        while True:
            if (self.check == "ok"):
                print "OK"
            else:
                print "!OK"

            sleep(2)


    def changeState(self, state):
        if state:
            self.check = "ok"
            print "zmieniono OK"
        else:
            self.check = "nieOk"
            print "zmieniono nieOk"

if __name__ == "__main__":
    popcorn = interactiveSerial()
    popcorn.startLoop()
    sleep(5)
    popcorn.changeState(False)
    sleep(5)
    popcorn.changeState(True)

