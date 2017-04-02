import threading
import time
import gobject
import gtk

gobject.threads_init()

class batteryWindow(threading.Thread):
    def __init__(self, port, howManyInRow=3, buttonFunction=False, maxLevel=1024, maxBar=6, resizeFunction=False):
        super(MyThread, self).__init__()
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
        self.window.connect("destroy", self.destroy)

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
        self.addresses = {}
        self.howMany = 0
        self.level = {}
        self.level_old = {}

    def __call__(self):
        self.show()

    def add(self, ID, name):
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

    def info(self, ID):
        # a horizontal box to hold the battery_buttons


        # create several images with data from files and load images into
        # battery_buttons
        if ID == 0:
            self.ID_OLD = 6
        else:
            self.ID_OLD = 6

        self.ID_OLD = ID
        self.image = gtk.Image()
        self.update(1, ID)
        self.image.show()
        # a battery_button to contain the image widget
        self.button = gtk.button()
        self.button.add(self.image)
        self.button.show()
        self.hbox.pack_start(self.button)
        self.button.connect("clicked", self.updateFromBttn, ID, 190)
        pass

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
        gtk.threads_enter()
        # type: (object, object, object, object) -> object
        print ""
        print "UPDATE BATTERY!"
        ID = int(ID)
        if maxLevel == None:
            maxLevel = self.maxLevel
        if maxBar == None:
            maxBar = self.maxBar

        ileBelek = 0;
        while ileBelek <= maxBar:
            procentLvl = self.obliczProcent(level, maxLevel)
            procentBelka = self.obliczProcent(ileBelek, maxBar)
            if (procentLvl >= procentBelka) & (procentLvl <= self.obliczProcent(ileBelek + 1, maxBar)):
                print "BELKI: " + str(procentLvl) + " " + str(ileBelek) + " ID: " + str(ID)
                obraz = "./img/battW" + str(ileBelek) + ".png"
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
        gtk.threads_leave()

    def obliczProcent(self, level, maxLevel):
        return round(((100 * float(level)) / maxLevel), 1)
        pass

    def changeName(self, ID, name):
        self.battery_ID_label[self.addresses[ID]].set_text("Bateria " + str(name))
        pass

    def show(self):
        # GObject.threads_init()
        # gtk.threads_init()
        print "MAAAAAAAAAAAAAAAAAAIN!"
        # gtk.gdk.threads_init()
        # gtk.threads_enter()
        self.window.show()
        gtk.main()
        # gtk.threads_leave()
        # self.run_gui_thread()
        # gui_thread = Process(target=self.run_gui_thread, args=[self]).start()
        print "MAAAAAAAAAAAAAAAAAAIN!MAAAAAAAAAAAAAAAAAAIN!"
        # gtk.main()
        pass

    def run_gui_thread(self, kupa):
        print "RUN GUI"
        from time import sleep
        while True:
            sleep(1)
            print "fffds"
            self.gtk.main()

# def batteryObject():
#     global batteryWindow
#     batteryWindow = batteryWindow('COM1', 3, True, 1024, 6)
#     batteryWindow.add(5, "pioruny")
#     batteryWindow.update(5, 555)
#     batteryWindow.changeName(5, "Aktor 1")
#     batteryWindow.show()

# if __name__ == "__main__":
#     from multiprocessing import Process

#     batteryWindow = Process(target=batteryObject, name="bateria").start() #nie dziala na macu

#     # batteryObject()
#     while True:
#         print "xD"
#         from time import sleep
#         sleep(2)


# import pygtk
# from threading import Thread
# from multiprocessing import Process
#
# pygtk.require('2.0')
# import gtk
#
#
# class batteryWindow:
#     def __init__(self, port, howManyInRow=3, buttonFunction=False, maxLevel=1024, maxBar=6, resizeFunction=False):
#         self.port = port
#         self.buttonFunction = buttonFunction
#         self.howManyInRow = howManyInRow
#         self.maxLevel = maxLevel
#         self.maxBar = maxBar
#
#         import os
#         import sys
#         os.chdir(os.path.dirname(os.path.abspath(__file__)))  # zmiana working directory na lokalizacje skryptu
#
#         print os.getcwd()  # dziala /home/oskar i nie dziala na innym systemie
#         print os.path.dirname(os.path.abspath(__file__))  # dziala /home/oskar/Pulpit/elSter/GitHub
#         print os.getcwd()  # dziala /home/oskar i nie dziala na innym systemie
#         print os.path.dirname(sys.argv[0])  # !dziala ./Pulpit/elSter/GitHub
#         print "DEBUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUG"
#
#         self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#         self.window.set_title("elSter - battery mannager")
#         self.window.set_border_width(10)
#
#         self.window.connect("delete_event", self.delete_event)
#         self.window.connect("destroy", self.destroy)
#
#         self.glownyVKontener = gtk.VBox(gtk.FALSE, 10)
#         self.glownyVKontener.show()
#
#         if resizeFunction:
#             self.scrolledCol = gtk.ScrolledWindow()
#             self.scrolledCol.set_border_width(10)
#             self.scrolledCol.set_resize_mode(True)
#             self.scrolledCol.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
#             self.scrolledCol.add_with_viewport(self.glownyVKontener)
#             self.scrolledCol.set_visible(True)
#
#             self.window.add(self.scrolledCol)
#         else:
#             self.window.add(self.glownyVKontener)
#
#         self.podkontenerH = {}
#         self.battery = {}
#         self.battery_icon = {}
#         if self.buttonFunction: self.battery_button = {}
#         self.battery_ID_label = {}
#         self.battery_poziom_label = {}
#         self.addresses = {}
#         self.howMany = 0
#         self.level = {}
#         self.level_old = {}
#
#     def __call__(self):
#         self.show()
#
#     def add(self, ID, name):
#         if self.port == "NO_PORTS":
#             print "I:------------ batterry.py BRAK PORTOW NA STATKII!"
#
#         if ID not in self.addresses:
#             self.addresses[ID] = self.howMany
#         else:
#             print "E:------- ERROR THE SAME ID (" + str(ID) + ") IN LIST FOR " + str(
#                 self.addresses[ID]) + "! (cloudn't add '" + str(name) + "')"
#             return
#
#         if not self.howMany % self.howManyInRow:
#             self.obecne_ID_kontenera = self.howMany
#             self.podkontenerH[self.addresses[ID]] = gtk.HBox(gtk.FALSE, 10)
#             self.podkontenerH[self.addresses[ID]].show()
#             self.glownyVKontener.add(self.podkontenerH[self.addresses[ID]])
#
#         self.battery[self.addresses[ID]] = gtk.VBox(gtk.FALSE, 10)
#
#         self.battery_icon[self.addresses[ID]] = gtk.Image()
#         self.obraz = "./img/battW" + str(6) + ".png"
#         self.battery_icon[self.addresses[ID]].set_from_file(self.obraz)
#         self.battery_icon[self.addresses[ID]].show()
#
#         if self.buttonFunction:
#             self.battery_button[self.addresses[ID]] = gtk.Button()
#             self.battery_button[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
#             self.battery_button[self.addresses[ID]].connect("clicked", self.updateFromBttn, ID, 190)
#             self.battery_button[self.addresses[ID]].show()
#
#         self.battery_ID_label[self.addresses[ID]] = gtk.Label("Bateria " + str(name))
#         self.battery_ID_label[self.addresses[ID]].show()
#         self.battery_poziom_label[self.addresses[ID]] = gtk.Label("100%")
#         self.battery_poziom_label[self.addresses[ID]].show()
#
#         if self.buttonFunction:
#             self.battery[self.addresses[ID]].add(self.battery_button[self.addresses[ID]])
#         else:
#             self.battery[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
#         self.battery[self.addresses[ID]].add(self.battery_ID_label[self.addresses[ID]])
#         self.battery[self.addresses[ID]].add(self.battery_poziom_label[self.addresses[ID]])
#
#         self.battery[self.addresses[ID]].show()
#         self.podkontenerH[self.obecne_ID_kontenera].add(self.battery[self.addresses[ID]])
#         self.howMany = self.howMany + 1
#
#         self.level[self.addresses[ID]] = 0
#
#     def hideWindow(self):
#         self.window.hide()
#
#     def showWindow(self):
#         self.window.show()
#
#     def getVisibleOfWindow(self):
#         return self.window.get_property("visible")
#
#         # print self.howMany
#
#     # print self.obecne_ID_kontenera
#     # print ID
#     # print name
#     # print self.addresses
#
#
#
#     def delete_event(self, widget, event, data=None):
#         # If you return FALSE in the "delete_event" signal handler,
#         # GTK will emit the "destroy" signal. Returning TRUE means
#         # you don't want the window to be destroyed.
#         # This is useful for popping up 'are you sure you want to quit?'
#         # type dialogs.
#         print "delete event occurred"
#
#         # Change FALSE to TRUE and the main window will not be destroyed
#         # with a "delete_event".
#         return False
#
#     def destroy(self, widget, data=None):
#         print "destroy signal occurred"
#         gtk.main_quit()
#
#     def info(self, ID):
#         # a horizontal box to hold the battery_buttons
#
#
#         # create several images with data from files and load images into
#         # battery_buttons
#         if ID == 0:
#             self.ID_OLD = 6
#         else:
#             self.ID_OLD = 6
#
#         self.ID_OLD = ID
#         self.image = gtk.Image()
#         self.update(1, ID)
#         self.image.show()
#         # a battery_button to contain the image widget
#         self.button = gtk.button()
#         self.button.add(self.image)
#         self.button.show()
#         self.hbox.pack_start(self.button)
#         self.button.connect("clicked", self.updateFromBttn, ID, 190)
#         pass
#
#     def updateOLD(self, widget, ID):
#         if self.level[self.addresses[ID]] == 0:
#             self.level[self.addresses[ID]] = 6
#         self.level_old[self.addresses[ID]] = self.level[self.addresses[ID]] - 1
#         self.level[self.addresses[ID]] = self.level_old[self.addresses[ID]]
#         obraz = "./img/battW" + str(self.level[self.addresses[ID]]) + ".png"
#         self.battery_icon[self.addresses[ID]].set_from_file(obraz)
#         pass
#
#     def updateFromBttn(self, idButtn, ID, level):
#         self.update(ID, level)
#         pass
#
#     def update(self, ID, level, maxLevel=None, maxBar=None):
#         gtk.threads_enter()
#         # type: (object, object, object, object) -> object
#         print ""
#         print "UPDATE BATTERY!"
#         ID = int(ID)
#         if maxLevel == None:
#             maxLevel = self.maxLevel
#         if maxBar == None:
#             maxBar = self.maxBar
#
#         ileBelek = 0;
#         while ileBelek <= maxBar:
#             procentLvl = self.obliczProcent(level, maxLevel)
#             procentBelka = self.obliczProcent(ileBelek, maxBar)
#             if (procentLvl >= procentBelka) & (procentLvl <= self.obliczProcent(ileBelek + 1, maxBar)):
#                 print "BELKI: " + str(procentLvl) + " " + str(ileBelek) + " ID: " + str(ID)
#                 obraz = "./img/battW" + str(ileBelek) + ".png"
#                 self.battery_poziom_label[self.addresses[ID]].set_text(str(procentLvl) + "%")
#                 print "zmienilem label"
#                 print "ADRES: " + str(self.addresses[ID])
#                 print "ID: " + str(ID)
#                 print "OBRAZ: " + obraz
#                 print "OBIEKT BAT: " + str(self.battery_icon[self.addresses[ID]])
#
#                 self.battery_icon[self.addresses[ID]].set_from_file(obraz)
#                 print "zmienilem obraz"
#                 return
#             ileBelek = ileBelek + 1
#             print "if"
#         pass
#         gtk.threads_leave()
#
#     def obliczProcent(self, level, maxLevel):
#         return round(((100 * float(level)) / maxLevel), 1)
#         pass
#
#     def changeName(self, ID, name):
#         self.battery_ID_label[self.addresses[ID]].set_text("Bateria " + str(name))
#         pass
#
#     def show(self):
#         # GObject.threads_init()
#         # gtk.threads_init()
#         print "MAAAAAAAAAAAAAAAAAAIN!"
#         # gtk.gdk.threads_init()
#         # gtk.threads_enter()
#         self.window.show()
#         gtk.main()
#         # gtk.threads_leave()
#         # self.run_gui_thread()
#         # gui_thread = Process(target=self.run_gui_thread, args=[self]).start()
#         print "MAAAAAAAAAAAAAAAAAAIN!MAAAAAAAAAAAAAAAAAAIN!"
#         # gtk.main()
#         pass
#
#     def run_gui_thread(self, kupa):
#         print "RUN GUI"
#         from time import sleep
#         while True:
#             sleep(1)
#             print "fffds"
#             self.gtk.main()
#
# # def batteryObject():
# #     global batteryWindow
# #     batteryWindow = batteryWindow('COM1', 3, True, 1024, 6)
# #     batteryWindow.add(5, "pioruny")
# #     batteryWindow.update(5, 555)
# #     batteryWindow.changeName(5, "Aktor 1")
# #     batteryWindow.show()
#
# # if __name__ == "__main__":
# #     from multiprocessing import Process
#
# #     batteryWindow = Process(target=batteryObject, name="bateria").start() #nie dziala na macu
#
# #     # batteryObject()
# #     while True:
# #         print "xD"
# #         from time import sleep
# #         sleep(2)
#
