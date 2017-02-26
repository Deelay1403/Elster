#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Autor:  Patryk Szczodrowski
        Oskar Jaskólski
Data modyfikacji: 10.11.16

Program do obsługi systemu bezprzewodowego zarządzania elSter. Dzięki procesorom ATMEGA program
jest w stanie komunikować się z odbiornikami. Wszystkie urządzenia w systemie muszą być wcześniej spreparowane oraz
zaprogramowane do działania pod konkretnym modułem
"""
# import self as self
import Tkinter as tk
import sys
import time

import serial

from BlinkInTime import blinkInTime

"""
sudo apt-get install python python-tk idle python-pmw python-imaging python-gtk2 libgtk-3-dev
"""

# from numpy.distutils.fcompiler import none
pass
from threading import Thread
import gtk
import glob
from random import randint
import StepWindow
import ConfigWindow
import generateScene
import battery #dodal oskar
from mainSerial import serialComunnication
from multiprocessing import Process

x = 1
#gladeFileName = "./window.glade"

logo = """
  ____       _               _      ____                      _                       _    _
 |  _ \ __ _| |_ _ __ _   _| | __ / ___|_______ _______   __| |_ __ _____      _____| | _(_)
 | |_) / _` | __| '__| | | | |/ / \___ |_  / __|_  / _ \ / _` | '__/ _ \ \ /\ / / __| |/ | |
 |  __| (_| | |_| |  | |_| |   <   ___) / | (__ / | (_) | (_| | | | (_) \ V  V /\__ |   <| |
 |____ \__,_|\__|_|   \__, |_|\_\ |____/___\___/___\___/ \__,_|_|  \___/ \_/\_/ |___|_|\_|_|
  ( _ )               |___/
  / _ \/\
 | (_>  <
  \___/\/   _                    _           _         _     _    _
  / _ \ ___| | ____ _ _ __      | | __ _ ___| | _____ | |___| | _(_)
 | | | / __| |/ / _` | '__|  _  | |/ _` / __| |/ / _ \| / __| |/ | |
 | |_| \__ |   | (_| | |    | |_| | (_| \__ |   | (_) | \__ |   <| |
  ____/|___|_|\_\__,_|_|     \___/ \__,_|___|__\_\___/|_|___|_|\_|_|                _         _____ _ __        _____ ____  _____
 |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___   | |_ ___     ___  _ __   ___ _ __ __ _| |_ ___  | ____| |\ \      / |_ _|  _ \| ____|
 | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \  | __/ _ \   / _ \| '_ \ / _ | '__/ _` | __/ _ \ |  _| | | \ \ /\ / / | || |_) |  _|
 |  __/| | | (_) | (_| | | | (_| | | | | | | | || (_) | | (_) | |_) |  __| | | (_| | ||  __/ | |___| |__\ V  V /  | ||  _ <| |___
 |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|  \__\___/   \___/| .__/ \___|_|  \__,_|\__\___| |_____|_____\_/\_/  |___|_| \_|_____|
 __     __        |____                ___   _____            |_|
 \ \   / ___ _ __ ___(_) ___  _ __    / _ \ |___ /
  \ \ / / _ | '__/ __| |/ _ \| '_ \  | | | |  |_  |
   \ V |  __| |  \__ | | (_) | | | | | |_| _ ___) |
    \_/ \___|_|  |___|_|\___/|_| |_|  \___(_|____/


"""

print(logo)
global alphabet
global Who
Who = 0
alphabet = {}
for i in range(47, 91):
    alphabet[i - 47] = chr(i)


def getWho():
    return Who

'''Metoda przeznaczona do wysyłania komend'''
def lightLED(receiver, state, led, option):
    if not dial == 'NO_PORTS':
        str = `receiver` + "." + `state` + "." + `led` + "." + `option` + "."
        dial.serial.SerialSend(str)
        # ser.write(`receiver` + "." + `state` + "." + `led` + "." + `option` + ".")
        # # ser.write(receiver + "." + state + "." + led + "." + option + ".")
    else:
        print('EMULATING')
        #TODO: SIMULATING SCENES

'''Gaszenie pojedyńczego urządzenia'''
def forLedBlackOutSingle(cstate, check1, check2, bt1, bt2, receiver, state, option):
    check1.set_active(cstate)
    check2.set_active(cstate)
    bt1.set_active(cstate)
    bt2.set_active(cstate)
    for x in range(1, 3):
        lightLED(receiver, state, x, option)

'''Gaszenie wszystkich urządzeń'''
def forLedBlackOutAll(state, option):
    for x in range(2, 7):
        for y in range(1, 3):
            lightLED(x, state, y, option)


# forLedBlackOutAll(0, 0)
activebuttons = True


# Example of callFunctionLightLed();
# def on_togglebutton1_3_toggled(self, widget):callFunctionLightLed(self, self.toggle1_3,self.check1_2, 2, 1, 2, 0)
'''Metoda wywoływana przez przyciski mająca na celu jednoczesne przygaszanie ich'''
def callFunctionLightLed(self, bt, check, receiver, state, led, option):
    check.set_active(True)
    lightLED(receiver, state, led, option)
    self.activecheck(self)
    if (bt.get_active() == False):
        check.set_active(False)
        if (state == 1):
            state = 0
        else:
            state = 1
        lightLED(receiver, state, led, option)
        self.activecheck(self)
#
# '''Ustalenie nazw zmiennych do dalszej pracy'''
# def defineValues(self):
#     self.toggle1_1 = self.builder.get_object("togglebutton1_1")
#     self.toggle1_2 = self.builder.get_object("togglebutton1_2")
#     self.toggle1_3 = self.builder.get_object("togglebutton1_3")
#     self.check1_1 = self.builder.get_object("Aktor1_1")
#     self.check1_2 = self.builder.get_object("Aktor1_2")
#     self.toggle2_1 = self.builder.get_object("togglebutton2_1")
#     self.toggle2_2 = self.builder.get_object("togglebutton2_2")
#     self.toggle2_3 = self.builder.get_object("togglebutton2_3")
#     self.check2_1 = self.builder.get_object("Aktor2_1")
#     self.check2_2 = self.builder.get_object("Aktor2_2")
#     self.toggle3_1 = self.builder.get_object("togglebutton3_1")
#     self.toggle3_2 = self.builder.get_object("togglebutton3_2")
#     self.toggle3_3 = self.builder.get_object("togglebutton3_3")
#     self.check3_1 = self.builder.get_object("Aktor3_1")
#     self.check3_2 = self.builder.get_object("Aktor3_2")
#     self.toggle4_1 = self.builder.get_object("togglebutton4_1")
#     self.toggle4_2 = self.builder.get_object("togglebutton4_2")
#     self.toggle4_3 = self.builder.get_object("togglebutton4_3")
#     self.check4_1 = self.builder.get_object("Aktor4_1")
#     self.check4_2 = self.builder.get_object("Aktor4_2")
#     self.toggle5_1 = self.builder.get_object("togglebutton5_1")
#     self.toggle5_2 = self.builder.get_object("togglebutton5_2")
#     self.toggle5_3 = self.builder.get_object("togglebutton5_3")
#     self.check5_1 = self.builder.get_object("Aktor5_1")
#     self.check5_2 = self.builder.get_object("Aktor5_2")
#
#     self.loop6 = self.builder.get_object("loopb6")
#     self.toggle_wszyscy = self.builder.get_object("togglebutton_wszyscy")
#     self.toggle_blackout = self.builder.get_object("togglebutton_wygas")
#

# Class to blink in time. It's generated by PyGTK and set value in sec
'''Klasa do zmiany adresu'''
class changeAddress():
    '''Klasa do bezprzewodowej zmiany adresu danego odbiornika'''
    def __init__(self, Who_, spBut):
        '''Konstruktor klasy'''
        global Who
        Who = Who_ + 1
        self.dialog = gtk.Dialog("Change Address",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_APPLY, gtk.RESPONSE_ACCEPT))
        self.hBox = gtk.HBox(gtk.FALSE, 1)
        # self.title = gtk.Label("Address")
        # self.title.set_alignment(0,0.5)
        self.adjustment = gtk.Adjustment(1, 1, 100, 1)
        self.spButton = gtk.SpinButton(self.adjustment, 0, 0)

        self.hBox.add(self.spButton)
        self.hBox.show()
        self.spButton.show()
        self.dialog.vbox.add(self.hBox)
        self.dialog.show()
        self.spBut = spBut
        self.dialog.connect('response', self.response)
        self.dialog.connect("destroy", self.on_window1_destroy())
    '''Główna metoda odpowiedzialna za zmiane adresu'''
    def response(self, Widget, data):
        self.New_address = self.adjustment.get_value() + 1
        print self.New_address
        print Who
        print str(int(Who)) + " 4 " + str(int(self.New_address)) + " 0"
        lightLED(int(Who), 4, int(self.New_address), 0)
        self.spBut.set_value(self.New_address - 1)
        self.dialog.destroy()
    '''Pobieranie nowego adresu'''
    def getNewAddress(self):
        return self.New_address
    '''Zachowanie w przypadku naciśnięcia CANCEL'''
    def on_window1_destroy(self, object, data=None):
        print ("quit with cancel")
        gtk.main_quit()
    '''Zachowanie w przypadku wyłączenia okna'''
    def on_gtk_quit_activate(self, menuitem, data=None):
        print ("quit from menu")
        gtk.main_quit()
'''Klasa głównego okna'''
class Mainwindow:
    '''Klasa głównego okna odpowiedzialna za generowanie konsoli'''
    '''Zachowanie w przypadku wyjścia z okna'''
    def on_window1_destroy(self, object, data=None):
        print ("quit with cancel")
        gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print ("quit from menu")
        gtk.main_quit()
    '''Reakcja na przyciski - na razie wyłączone'''
    def on_key_press(self, widget=None, event=None, data=None):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if (keyname, event.keyval)[0] == 't':
            self.on_togglebutton5_2_toggled(self)
            active = not (self.toggle5_2.get_active())
            self.toggle5_2.set_active(active)
        if (keyname, event.keyval)[0] == 'r':
            self.on_togglebutton4_2_toggled(self)
            active = not (self.toggle4_2.get_active())
            self.toggle4_2.set_active(active)
        if (keyname, event.keyval)[0] == 'e':
            self.on_togglebutton3_2_toggled(self)
            active = not (self.toggle3_2.get_active())
            self.toggle3_2.set_active(active)
        if (keyname, event.keyval)[0] == 'w':
            self.on_togglebutton2_2_toggled(self)
            active = not (self.toggle2_2.get_active())
            self.toggle2_2.set_active(active)
        if (keyname, event.keyval)[0] == 'q':
            self.on_togglebutton1_2_toggled(self)
            active = not (self.toggle1_2.get_active())
            self.toggle1_2.set_active(active)

        if (keyname, event.keyval)[0] == '5':
            self.on_togglebutton5_1_toggled(self)
            active = not (self.toggle5_1.get_active())
            self.toggle5_1.set_active(active)
        if (keyname, event.keyval)[0] == '4':
            self.on_togglebutton4_1_toggled(self)

            active = not (self.toggle4_1.get_active())
            self.toggle4_1.set_active(active)
        if (keyname, event.keyval)[0] == '3':
            self.on_togglebutton3_1_toggled(self)
            active = not (self.toggle3_1.get_active())
            self.toggle3_1.set_active(active)
        if (keyname, event.keyval)[0] == '2':
            self.on_togglebutton2_1_toggled(self)
            active = not (self.toggle2_1.get_active())
            self.toggle2_1.set_active(active)
        if (keyname, event.keyval)[0] == '1':
            self.on_togglebutton1_1_toggled(self)
            active = not (self.toggle1_1.get_active())
            self.toggle1_1.set_active(active)

        if (keyname, event.keyval)[0] == 'g':
            self.on_togglebutton5_3_toggled(self)
            active = not (self.toggle5_3.get_active())
            self.toggle5_3.set_active(active)
        if (keyname, event.keyval)[0] == 'f':
            self.on_togglebutton4_3_toggled(self)
            active = not (self.toggle4_3.get_active())
            self.toggle4_3.set_active(active)
        if (keyname, event.keyval)[0] == 'd':
            self.on_togglebutton3_3_toggled(self)
            active = not (self.toggle3_3.get_active())
            self.toggle3_3.set_active(active)
        if (keyname, event.keyval)[0] == 's':
            self.on_togglebutton2_3_toggled(self)
            active = not (self.toggle2_3.get_active())
            self.toggle2_3.set_active(active)
        if (keyname, event.keyval)[0] == 'a':
            self.on_togglebutton1_3_toggled(self)
            active = not (self.toggle1_3.get_active())
            self.toggle1_3.set_active(active)

        if (keyname, event.keyval)[0] == 'l':
            self.on_togglebutton_wygas_toggled(self)
            active = not (self.toggle_blackout.get_active())
            self.toggle_blackout.set_active(active)

        if (keyname, event.keyval)[0] == 'k':
            self.on_togglebutton_wszyscy_toggled(self)
            active = not (self.toggle_wszyscy.get_active())
            self.toggle_wszyscy.set_active(active)
    '''Reakcja na kliknięcie - stara'''
    def click(self, Widget, *Data):
        # print Data[0]
        state = Widget.get_active()
        print str(Data[0] + 1) + ',' + str(int(state)) + ',' + str(Data[1]) + ',' + str(0)
        lightLED(Data[0] + 1, int(state), Data[1], 0)
    '''Reakcja na zmiane adresu'''
    def click_change_address(self, Widget, *Data):
        print "Uwaga dane"

        print self.getBT(Data[0])
        print Data[1]
        changeaddress = changeAddress(self.getBT(Data[0]), Data[1])
        #  Data[1].set_value(changeaddress.getNewAddress())
    '''Wygaszanie'''
    def blackoutclock(self, Widget, *Data):
        state = Widget.get_active()
        for x in range(1, 3):
            state = Widget.get_active()
            # if(state == True):
            #     state = 1
            # else:
            #     state = 0
            lightLED((Data[0]+1), 0, x, 0)
    '''Zmiana adresu danej kolumy - adresu komunikacyjnego kolumny'''
    def addressValueChange(self, Widget, *Data):
        for bt in range(1, ConfigWindow.iloscbt + 1):
            # if self.bt_table_id[Data[0]][0] == 0:
            #     self.btBox[Data[0]].disconnect(self.bt_table_id[Data[0]][bt])
            # else:
            # print Widget
            # print self.bt_table_id
            print 'data .......'
            print Data[2]
            print 'FUCKING BT_TABLE_ID FUUUUUUUUUUUUUUUUUUUUUUU'
            print self.bt_table_id
            self.bt_table[Data[0]][bt].disconnect(self.bt_table_id[Data[0]][bt])
            self.bt_table_id[Data[0]][bt] = self.bt_table[Data[0]][bt].connect('clicked', self.click, self.sb_address[
                Data[0]].get_value_as_int(), bt)
            # self.bt_table_id[Data[0]][0] = 1
            # print self.bt_table_id[Data[0]]
            # print self.sb_address[Data[0]].get_value_as_int()

    def addressValueChange2(self, Widget, *Data):
        # for bt in range(1,iloscbt+1):
        print '...'
        print Data[2]
        print 'lel'
        print self.bt_table

    size_of_window = 110
    def setBT(self,bt):
        global b
        b = bt
    def getBT(self, index):
        return b[index].get_value_as_int()
    def printfuckingBT(self):
        print self.bt_table_id
    '''Konstruktor klasy'''
    def __init__(self):
        '''Konstruktor klasy MainWindow'''
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("elSter - console")
        self.window.connect("destroy", self.on_window1_destroy)
        self.window.set_border_width(0)
        self.container = gtk.HBox(gtk.FALSE, ConfigWindow.zmienna+1)
        self.container.set_border_width(10)

        self.vcontainer = gtk.VBox(gtk.FALSE,2)
        self.window.set_default_size((self.size_of_window * ConfigWindow.zmienna) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt,
                                      (self.size_of_window * ConfigWindow.iloscbt) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt)
        #self.window.set_default_size(640,320)
        self.scrolled_window = gtk.ScrolledWindow()
        self.scrolled_window.set_policy(gtk.POLICY_ALWAYS,gtk.POLICY_ALWAYS)
        self.scrolled_window.show()
        # self.window.add(self.vcontainer)
        self.window.add(self.vcontainer)
        # self.scrolled_window.add(self.menuTool())
        # self.scrolled_window.add(self.container)
        #self.scrolled_window.add(self.container)
        #self.scrolled_window.set_size_request(640,320)
        # self.vcontainer.add(self.scrolled_window)
        self.vcontainer.pack_start(self.menuTool(),False,False,0)
        self.vcontainer.pack_start(self.container, False, False, 0)
       #
        #  self.vcontainer.pack_start(self.scrolled_window,True,True,0)


        # self.cb_list = gtk.ListStore(str)
        # self.cb_keyboard = gtk.ComboBox(self.cb_list)
        # self.cb_cell = gtk.CellRendererText()
        # self.cb_keyboard.pack_start(self.cb_cell,True)
        # self.cb_keyboard.add_attribute(self.cb_cell,'text',0)
        # print alphabet
        # for i in range(47,91):
        #     self.cb_list.append(alphabet[i-47])
        # self.cb_keyboard.set_model(self.cb_list)
        # self.cb_keyboard.show()
        # global bt_table_id, bt_table
        '''Początek tworzenia tablic odpowiedzialnych za przechowywanie obiektów graficznych'''
        self.vBox = {}
        self.btBox = {}
        self.btBlackout = {}
        self.sb_address = {}
        self.sb_adjustment = {}
        self.bt_id = {}
        self.frame = {}
        self.hbox_for_frame = {}
        self.bt_address = {}
        self.bt_table_id = [[1 for x in range(ConfigWindow.iloscbt + 1)] for y in range(ConfigWindow.zmienna + 1)]
        self.bt_table = [[1 for bt_x in range(ConfigWindow.iloscbt + 1)] for bt_y in range(ConfigWindow.zmienna + 1)]
        '''Uzupełnianie głównego kontenera'''
        for num in range(1, ConfigWindow.zmienna + 1):
            self.vBox[num] = gtk.VBox(gtk.FALSE, ConfigWindow.zmienna)
            #self.vBox[num].set_size_request(1000,300)

            self.container.add(self.vBox[num])
            self.vBox[num].show()
        '''Uzupełnianie kontenera o pionowe elementy'''
        for i in range(1, ConfigWindow.zmienna2 + 1):
            self.sb_adjustment[i] = gtk.Adjustment(i, 1, 100, 1, 5, 0)
            self.sb_address[i] = gtk.SpinButton(self.sb_adjustment[i], 0, 0)
            self.setBT(self.sb_address)
            self.sb_address[i].show()
            self.btBlackout[i] = gtk.ToggleButton("Blackout")
            self.btBlackout[i].connect("clicked", self.blackoutclock, i, self.bt_id)
            self.btBlackout[i].show()
            self.vBox[i].add(self.btBlackout[i])
            print  self.bt_table
            print self.bt_table_id
            for bt in range(1, ConfigWindow.iloscbt + 1):
                self.btBox[bt] = gtk.ToggleButton("LED" + str(bt))
                # self.btBox[bt].connect('clicked',self.click,i,bt)
                self.btBox[bt].show()
                self.bt_id[bt] = self.btBox[bt].connect('clicked', self.click, i, bt)
                self.bt_id[0] = 0
                try:
                    self.bt_table[i][bt] = self.btBox[bt]
                except IndexError:
                    print 'lel'
                self.bt_table_id[i][bt] = self.bt_id[bt]
                print "lel XD"
                print self.btBox[bt]
                print 'end'
                print self.bt_table
                # self.bt_table[i-1][bt-1] = self.btBox[bt]

                # for self.vBox in range(1,zmienna2+1):
                self.vBox[i].add(self.btBox[bt])

            print "lel"
            print self.btBox
            self.frame[i] = gtk.Frame("Change address")
            # self.bt_address[i] = gtk.Button("Change")
            self.lel = gtk.Frame()
            self.lel.set_border_width(5)
            self.bt_address[i] = gtk.Button("Change")
            self.bt_address[i].connect("clicked", self.click_change_address, i,self.sb_address[i])
            self.frame[i].set_border_width(5)
            self.bt_address[i].set_border_width(10)

            self.frame[i].add(self.bt_address[i])

            self.frame[i].show()
            self.bt_address[i].show()

            self.vBox[i].add(self.frame[i])

            self.sb_adjustment[i].connect('value_changed', self.addressValueChange, i, self.bt_id, self.bt_table)
            print ";-;"
            print self.bt_id
            print "XD"
            print self.bt_table_id
            self.vBox[i].add(self.sb_address[i])
            self.printfuckingBT()
        '''Uruchomienie kilku ważnych wewnętrznych metod'''
        self.printfuckingBT()
        self.container.show()
        self.vcontainer.show()
        self.window.show()

    def menuTool(self):
        self.menu = gtk.Menu()
        self.viewMenu = gtk.Menu()

        self.firstMenuitem = {}
        self.viewMenuitem = {}

        self.firstMenuitem[0] = gtk.MenuItem("Generator")
        self.firstMenuitem[1] = gtk.MenuItem("Zamknij")

        self.viewMenuitem[0] = gtk.MenuItem("Bateria")
        self.viewMenuitem[1] = gtk.MenuItem("Miganie")

        for i in range(0, len(self.firstMenuitem)):
            self.menu.append(self.firstMenuitem[i])
            self.firstMenuitem[i].show()

        for i in range(0, len(self.viewMenuitem)):
            self.viewMenu.append(self.viewMenuitem[i])
            self.viewMenuitem[i].show()

        self.firstMenuitem[0].connect("activate", self.generateSceneWindow)
        self.firstMenuitem[1].connect("activate", gtk.main_quit)

        self.viewMenuitem[0].connect("activate", self.viewWindow,"battery")
        self.viewMenuitem[1].connect("activate", self.viewWindow,"blink")

        self.root = gtk.MenuItem("Narzędzia")
        self.view = gtk.MenuItem("Widok")

        self.root.show()
        self.root.set_submenu(self.menu)

        self.view.show()
        self.view.set_submenu(self.viewMenu)

        self.menu_bar = gtk.MenuBar()
        self.menu_bar.show()
        self.menu_bar.append(self.root)
        self.menu_bar.append(self.view)

        self.menu.show()
        self.viewMenu.show()

        return self.menu_bar
    def viewWindow(self,Data,SayMyName):
            if SayMyName == "battery":
                print self.batteryWindow.getVisibleOfWindow()
        # except AttributeError:
        #     print "lel"

    def generateSceneWindow(self,args):
        g = generateScene.generateScene()
    def activecheck(self, chbutton):
        print "kek"
    '''Metoda nie używana'''
    def on_loopb6_toggled(self, widget):

        class lop(Thread):
            def __init__(self):
                Thread.__init__(self)
                self.daemon = True
                self.start()

            def run(self):
                while (True):
                    print "lel"
                    time.sleep(1)
                    lightLED(6, 0, 2, 0)
                    lightLED(6, 1, 1, 0)
                    time.sleep(1)
                    lightLED(6, 0, 1, 0)
                    lightLED(6, 1, 2, 0)
                    if (self.loopb6.get_active() == False):
                        forLedBlackOutSingle(6, 0, 0)
                        break
        lop()
        while True:
            pass

    def on_togglebutton_wszyscy_toggled(self, widget):
        if (activebuttons == True):
            forLedBlackOutAll(1, 0)
            self.activecheck(self)
            if self.toggle_wszyscy.get_active() == False:
                print "check"
                forLedBlackOutAll(0, 0)
                self.activecheck(self)

    def on_togglebutton_wygas_toggled(self, widget):
        forLedBlackOutAll(0, 0)
        if self.toggle_blackout.get_active() == False:
            forLedBlackOutAll(1, 0)




# Serial detect!
'''Wykrycie podłączonych urządzeń do komputera'''
def serial_ports():
    ok = []
    return ok

class serialPorts():
    def __init__(self):
        # print "WYSZUKUJEE"
        # Windows
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        # Linux
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        # Mac OS X
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        self.portsOpen = []
        for port in ports:
            try:
                # Trying if ports are open
                s = serial.Serial(port, timeout=0.5)
                print port
                s.write("99,7") #PING
                print "zapisano"
                line = s.read_until(';')
                print "odczytano"
                line = line.strip("\r\n")
                print line
                if line.startswith('ACK_OK'): #akceptujemy tylko nasze urzadzenia, a nie jakies modemy xD
                    s.close()
                    self.portsOpen.append(port)
            # if OS is diferent it pass program without connect serial
            except (OSError, serial.SerialException):
                pass

    def get(self):
        return self.portsOpen
        pass



'''Ustawienie urządzenia obsługiwanego'''
def set_serial(serial):
    global index
    index = serial
    print "SET SERIAL " + str(index)

# for situation in serialPorts().get():
#     print str(x) + ": " + situation
#     x += 1

def keylisten(event):
    print(event.char)

def keyrequest():
    root = tk.Tk()
    root.bind('<KeyPress>', keylisten)
    root.mainloop()

time.sleep(2)

#if mode False wykonanie z ConfigWindow, True, przeciwnie xD
def serialActivate(dial, mode):
    print "SERIAL active"
    global ser
    serial_ports = serialPorts().get()
    print serial_ports
    print dial
    print mode
    print "END"


    if not serial_ports:
        print "BRAK PORTOW NA STATKI";
        ser = "NO_PORTS";
    else:
        if mode:
            whichIndex = dial.getIndex()
        else:
            whichIndex = dial
        if whichIndex > -1:
            print whichIndex
            print serial_ports[whichIndex]
            ser = serial.Serial(serial_ports[whichIndex], 9600)
        else:
            print "BRAK PORTOW NA STATKII"
            ser = "NO_PORTS"


'''Funcja uruchamiana przez wątek. Obsługuje ona wszystko'''


'''Główna metoda klasy uruchamiająca wątek'''

def createObjectDial():
    global dial
    dial = ConfigWindow.serialWindow()
def createObjectWindowMain():
    global window
    window = Mainwindow()
def createObjectBlink():
    global blink
    blink = blinkInTime(ConfigWindow.zmienna)
def createObjectBaterry():
    global batteryWindow
    batteryWindow = battery.batteryWindow(dial.serial.GetOpenPort(), 5, True, 1024, 6)

def createObjectInter(port):
    import interactiveSerial as inSer
    global inter
    inter = inSer.interactiveSerial(port)
    inter.addObject('battery', batteryWindow)
def start():
    import mainSerial
    #global dial, batteryWindow, blinkWindow
    print "XD"
    dialProcess = Process(target=createObjectDial(),name="Dial")
    dialProcess.start()
    print "XD"
    # dial = ConfigWindow.serialWindow()
    #mainSerial.serialComunnication().SerialActivate(dial, True)
    # window = Mainwindow()
    # ser = dial.serial.GetOpenPort()
    windowProcess = Process(target=createObjectWindowMain(),name="Window")
    windowProcess.start()

    # batteryWindow = battery.batteryWindow(ser, 5, True, 1024, 6)
    # blinkWindow = Process(target=createObjectBlink()).start()
    # blinkWindow = blinkInTime(ConfigWindow.zmienna)

    Battery = Process(target=createObjectBaterry())
    Battery.start()

    interProcess = Process(target=createObjectInter(dial.serial.GetOpenPort()))
    interProcess.start()

    aktywneID = ConfigWindow.activeID
    print aktywneID
    if aktywneID[0] == "list":
        for num in range(0, len(aktywneID)):
            batteryWindow.add(aktywneID[1][num], aktywneID[1][num])
    else:
        for num in range(1, (aktywneID[1] + 1)):
            batteryWindow.add(num, num)

    inter.start()
    #inter.updateBattery(5, 500)
    #inter.getObject('battery').update(3, 512)
    # mały pokaz nowych funkcji
    '''zmiana nazwy baterii'''
    #batteryWindow.changeName(1, "DZIAŁA!")
    '''aktualizacja stanu baterii'''
    #batteryWindow.update(1, 640)

    batteryWindow.show()

    Process(target=gtk.main()).start()

    # t3 = Thread(name="key", target=keyrequest())
    # t3.start()
if __name__ == "__main__":
    t2 = Process(target=start).start()
def __init__():
    # t = Thread(name="log", target=log("lel"))
    # t.setDaemon(True)
    # t2 = Thread(name="main", target=start)
    # # t.start()
    # t2.start()
    t2 = Process(target=start).start()
#TODO wraz ze zmiana adresu urzadzenia zmiana adresu baterii
#TODO sprawdzanie bledow w tle
#TODO pokomentowc troche :>