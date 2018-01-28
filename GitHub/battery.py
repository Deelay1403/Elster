#Oskar  28.01.2018
import threading
import time
import Queue
import gobject, gtk

class batteryWindow:
    def __init__(self, gtkIsSet, port, howManyInRow=3, buttonFunction=False, maxLevel=1024, maxBar=6, resizeFunction=False):
        self.gtkIsSet = gtkIsSet
        self.gui_ready = threading.Event()
        self.queue = Queue.Queue()

        import gobject
        gobject.threads_init()
        import gtk

        self.port = port
        self.buttonFunction = buttonFunction
        self.howManyInRow = howManyInRow
        self.maxLevel = maxLevel
        self.maxBar = maxBar

        import os
        import sys
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # zmiana working directory na lokalizacje skryptu

        print os.getcwd()  # dziala /home/oskar i nie dziala na innym systemie
        print os.path.dirname(os.path.abspath(__file__))  # dziala /home/oskar/Pulpit/elSter/GitHub
        print os.getcwd()  # dziala /home/oskar i nie dziala na innym systemie
        print os.path.dirname(sys.argv[0])  # !dziala ./Pulpit/elSter/GitHub
        print "DEBUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUG"

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("elSter - battery mannager")
        self.window.set_border_width(10)

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.koniec)

        self.glownyVKontener = gtk.VBox(gtk.FALSE, 10)
        self.glownyVKontener.show()

        if resizeFunction:
            self.scrolledCol = gtk.ScrolledWindow()
            self.scrolledCol.set_border_width(10)
            self.scrolledCol.set_resize_mode(True)
            self.scrolledCol.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
            self.scrolledCol.add_with_viewport(self.glownyVKontener)
            self.scrolledCol.set_visible(True)

            self.window.add(self.scrolledCol)
        else:
            self.window.add(self.glownyVKontener)

        self.podkontenerH = {}
        self.battery = {}
        self.battery_icon = {}
        if self.buttonFunction: self.battery_button = {}
        self.battery_ID_label = {}
        self.battery_poziom_label = {}
        try:
            print "STARE ADDRESES: " + str(self.addresses)
        except AttributeError:
            print "Nie ma Addreses, czyli init"
        self.addresses = {} # {1,2}
        self.howMany = 0
        self.level = {}
        self.level_old = {}

    def __call__(self):
        self.show()

    def getQueue(self):
        return self.queue

    def add(self, ID, name):
        #gobject.idle_add(self.add2, ID, name)
        self.add2(ID, name)
        pass

    def add2(self, ID, name):
        print "dodaje " + str(ID) + " jako " + name
        if self.port == "NO_PORTS":
            print "I:------------ batterry.py BRAK PORTOW NA STATKII!"

        if ID not in self.addresses:
            self.addresses[ID] = self.howMany
        else:
            print "E:------- ERROR THE SAME ID (" + str(ID) + ") IN LIST FOR " + str(
                self.addresses[ID]) + "! (cloudn't add '" + str(name) + "')"
            return

        if not self.howMany % self.howManyInRow:
            self.obecne_ID_kontenera = self.howMany
            self.podkontenerH[self.addresses[ID]] = gtk.HBox(gtk.FALSE, 10)
            self.podkontenerH[self.addresses[ID]].show()
            self.glownyVKontener.add(self.podkontenerH[self.addresses[ID]])

        self.battery[self.addresses[ID]] = gtk.VBox(gtk.FALSE, 10)

        self.battery_icon[self.addresses[ID]] = gtk.Image()
        self.obraz = "./img/battW" + str(6) + ".png"
        self.battery_icon[self.addresses[ID]].set_from_file(self.obraz)
        self.battery_icon[self.addresses[ID]].show()

        if self.buttonFunction:
            self.battery_button[self.addresses[ID]] = gtk.Button()
            self.battery_button[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
            self.battery_button[self.addresses[ID]].connect("clicked", self.updateFromBttn, ID, 190)
            self.battery_button[self.addresses[ID]].show()

        self.battery_ID_label[self.addresses[ID]] = gtk.Label("Bateria " + str(name))
        self.battery_ID_label[self.addresses[ID]].show()
        self.battery_poziom_label[self.addresses[ID]] = gtk.Label("100%")
        self.battery_poziom_label[self.addresses[ID]].show()

        if self.buttonFunction:
            self.battery[self.addresses[ID]].add(self.battery_button[self.addresses[ID]])
        else:
            self.battery[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
        self.battery[self.addresses[ID]].add(self.battery_ID_label[self.addresses[ID]])
        self.battery[self.addresses[ID]].add(self.battery_poziom_label[self.addresses[ID]])

        self.battery[self.addresses[ID]].show()
        self.podkontenerH[self.obecne_ID_kontenera].add(self.battery[self.addresses[ID]])
        self.howMany = self.howMany + 1

        self.level[self.addresses[ID]] = 0

    def hideWindow(self):
        self.window.hide()

    def showWindow(self):
        self.window.show()

    def getVisibleOfWindow(self):
        return self.window.get_property("visible")

        # print self.howMany

    # print self.obecne_ID_kontenera
    # print ID
    # print name
    # print self.addresses



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

    def updateOLD(self, widget, ID):
        if self.level[self.addresses[ID]] == 0:
            self.level[self.addresses[ID]] = 6
        self.level_old[self.addresses[ID]] = self.level[self.addresses[ID]] - 1
        self.level[self.addresses[ID]] = self.level_old[self.addresses[ID]]
        obraz = "./img/battW" + str(self.level[self.addresses[ID]]) + ".png"
        self.battery_icon[self.addresses[ID]].set_from_file(obraz)
        pass

    def updateFromBttn(self, idButtn, ID, level):
        self.update(ID, level)
        pass

    def update(self, ID, level, maxLevel=None, maxBar=None):
        #gobject.idle_add(self.update2, ID, level, maxLevel, maxBar) #nie stosuje zamieniam na qiu
        print "UPDATE func"
        print ID
        print level
        print maxLevel
        print maxBar
        self.queue.put(['UPDATE', ID, level, maxLevel, maxBar])
        pass

    def update2(self, ID, level, maxLevel=None, maxBar=None):
        print ""
        print "UPDATE BATTERY!"
        ID = int(ID)
        if maxLevel == None:
            maxLevel = self.maxLevel
        if maxBar == None:
            maxBar = self.maxBar

        ileBelek = 0
        while ileBelek <= maxBar:
            procentLvl = self.obliczProcent(level, maxLevel)
            procentBelka = self.obliczProcent(ileBelek, maxBar)
            if (procentLvl >= procentBelka) & (procentLvl <= self.obliczProcent(ileBelek + 1, maxBar)):
                print "BELKI: " + str(procentLvl) + " " + str(ileBelek) + " ID: " + str(ID)
                obraz = "./img/battW" + str(ileBelek) + ".png"
                print "IDZIE DEBUG"
                print self.addresses
                self.battery_poziom_label[self.addresses[ID]].set_text(str(procentLvl) + "%")
                print "zmienilem label"
                print "ADRES: " + str(self.addresses[ID])
                print "ID: " + str(ID)
                print "OBRAZ: " + obraz
                print "OBIEKT BAT: " + str(self.battery_icon[self.addresses[ID]])

                self.battery_icon[self.addresses[ID]].set_from_file(obraz)
                print "zmienilem obraz"
                return
            ileBelek = ileBelek + 1
            print "if"
        pass

    def obliczProcent(self, level, maxLevel):
        return round(((100 * float(level)) / maxLevel), 1)
        pass

    def changeName(self, ID, name):
        self.battery_ID_label[self.addresses[ID]].set_text("Bateria " + str(name))
        pass

    def show(self):
        self.window.show()
        self.start()
        pass


    def runProcess(self, queue):
        print "RUN GUI"
        from time import sleep
        while True:
            sleep(1)
            print "fffds"
            self.gtk.main()

    def run_gui_thread(self):
        self.window.show()
        #self.w.connect("destroy", lambda _: self.koniec())
        self.gui_ready.set()
        #gtk.main() psuje sie na macu
        if not self.gtkIsSet:
            print "GTK ONNNNNNNNNNNN"
            gtk.main()

    def startThread(self):
        gui_thread = threading.Thread(target=self.run_gui_thread, name="batteryGUI")
        gui_thread.start()

        # wait for the GUI thread to initialize GTK
        #self.gui_ready.wait()

        # it is now safe to import GTK-related stuff
        import gobject, gtk
        worker = threading.Thread(target=self.countdown, args=(7040,), name="BatteryBackgroundWorker")
        print 'starting work...'
        worker.start()
        pass

    def stopThread(self):
        self.queue.put(['STOP_LISTENING', ''])
        pass


    def countdown(self, maxSec):
            #gobject.idle_add(self.update_label, maxSec)
            while maxSec > 0:
                try:
                    daneOdebrane = self.queue.get_nowait()
                    if (daneOdebrane[0] == "STOP_LISTENING"):
                        print "STOP!"
                        self.koniec()
                        break
                except Exception:
                    daneOdebrane = ["brak", "danych"]
                #print maxSec
                time.sleep(0.5)
                #maxSec -= 1
                #gobject.idle_add(self.update_label, maxSec)
                if daneOdebrane[0] == "UPDATE":
                    # gobject.idle_add(self.update2, ID, level, maxLevel, maxBar)
                    gobject.idle_add(self.update2, daneOdebrane[1], daneOdebrane[2], daneOdebrane[3], daneOdebrane[4])

                print "dane odebrane z battery " + str(daneOdebrane) + ", a queue " + str(self.queue)

            if maxSec == 0:
                self.koniec()

    def koniec(self, ID="none"):
        print "KOOOOOONIEC!"
        gobject.idle_add(gtk.main_quit)
        self.stopThread()

    def saySomething(self):
        print "I'M ALIVE!"
        print "SELF: " + str(self)
        print "Adresy: " + str(self.addresses)
        print "Window: " + str(self.window)
        print "GTK is set? " + str(self.gtkIsSet)


if __name__ == "__main__":
    batteryWindow1 = batteryWindow(True, 'COM1', 3, True, 1024, 6)
    batteryWindow1.add(1, "pioruny 1")
    batteryWindow1.add(2, "pioruny 2")
    batteryWindow1.add(3, "pioruny 3")
    batteryWindow1.startThread()
    # batteryWindow2 = batteryWindow(False, 'COM1', 3, True, 1024, 6)
    # batteryWindow2.add(1, "pioruny")
    # batteryWindow2.startThread()
    time.sleep(2)

    # batteryWindow1.add(2, "pioruny")
    # time.sleep(0.5)
    # batteryWindow1.add(3, "pioruny")
    # time.sleep(0.5)
    # batteryWindow1.add(4, "pioruny")
    # time.sleep(0.5)
    # batteryWindow1.add(5, "pioruny")
    # time.sleep(0.5)
    # batteryWindow1.add(6, "pioruny")
    # time.sleep(2)
    # batteryWindow1.changeName(1, "TO")
    # time.sleep(0.5)
    # batteryWindow1.changeName(2, "NA")
    # time.sleep(0.5)
    # batteryWindow1.changeName(3, "PRA")
    # time.sleep(0.5)
    # batteryWindow1.changeName(4, "WDE")
    # time.sleep(0.5)
    # batteryWindow1.changeName(5, "DZIALA")
    # time.sleep(0.5)
    # batteryWindow1.changeName(6, "!!!!")
    # x = 1024
    # y = True
    # z = 1024
    # while y:
    #     batteryWindow1.update(2, x)
    #     time.sleep(0.1)
    #     if x > 0:
    #         x -=10
    #     if x < 512:
    #         batteryWindow1.update(5, z)
    #         #time.sleep(0.1)
    #         z -=20
    #         if z < 0:
    #             y = False
    #
    # batteryWindow1.add(7, "OSKAR")
    # time.sleep(2)
    # batteryWindow1.update(1, 768)
    # batteryWindow1.update(3, 768)
    # batteryWindow1.update(4, 768)
    # batteryWindow1.update(6, 768)
    #batteryWindow.stopThread()