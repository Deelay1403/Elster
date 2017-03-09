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
import time

from BlinkInTime import blinkInTime

"""
sudo apt-get install python python-tk idle python-pmw python-imaging python-gtk2 libgtk-3-dev
"""

pass
from threading import Thread
import gtk

import ConfigWindow
import generateScene
import battery #dodal oskar
from multiprocessing import Process, Queue

x = 1

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

time.sleep(2)


'''Funcja uruchamiana przez wątek. Obsługuje ona wszystko'''


'''Główna metoda klasy uruchamiająca wątek'''

# objects_Table = {}
#
# def setObject(object,name):
#     objects_Table[name] = object
# def getObject(name):
#     return objects_Table[name]

def createObjectDial(q):
    global dial
    dial = ConfigWindow.serialWindow()
    #q.put(dial)
    from time import sleep
    # while True:
    #     print "KKKK"
    #     sleep(1)
def createObjectWindowMain(q):
    global window
    window = Mainwindow()
    #q.put(window)
def createObjectBlink(q):
    global blink
    blink = blinkInTime(ConfigWindow.zmienna)

def createObjectBaterry(q):
    global batteryWindow
    batteryWindow = battery.batteryWindow(dial.serial.GetOpenPort(), 5, True, 1024, 6, False)
    #q.put(batteryWindow)
def createObjectInter(port,q):
    import interactiveSerial as inSer
    global inter
    inter = inSer.interactiveSerial(port)
    inter.addObject('battery', batteryWindow)
    inter.fuckLoop()
    inter.start()

def createKeyboard():
    print "lel"

def start():
    global dial, window, inter, batteryWindow
    global iloscBt,zmienna,zmienna2


    queue_of_cry = [Queue() for i in range(0,4)]
    # dialProcess = Process(target=createObjectDial(),name="Dial")
    # dialProcess.start()
    t = Thread(target=createObjectDial(None), name="Dial", args=(queue_of_cry[0],))
    t.start()
    t.join()
    #dial = queue_of_cry[0].get()
    #
    # iloscBt = queue_of_cry[0].iloscBT
    # zmienna = ConfigWindow.zmienna
    # zmienna2 = ConfigWindow.zmienna2
    print "XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
    #print getObject("dial").getSelf() #   :c
    print "------------------------------------DIAL--------------------"
    windowProcess = Thread(target=createObjectWindowMain(None), name="Window", args=(queue_of_cry[1],))
    windowProcess.daemon = False
    windowProcess.start()
    windowProcess.join()
#    window = queue_of_cry[1].get()

    #windowProcess._target.dial.serial.GetOpenPort()
    Battery = Thread(target=createObjectBaterry, name="Battery", args=(queue_of_cry[2],))
    # batteryWindow = queue_of_cry[2].get()
    Battery.daemon = False
    Battery.start()
    Battery.join()


    # interProcess = Process(target=createObjectInter(dial.serial.GetOpenPort()))
    # interProcess.start()
    interThread = Process(target=createObjectInter,name="inter",args=(dial.serial.GetOpenPort(),queue_of_cry[3]))
    interThread.daemon = False
    interThread.start()
    # interThread.join()

    keyBoard = Thread(target=createKeyboard(), name="Keyboard")
    keyBoard.start()

    aktywneID = ConfigWindow.activeID
    print aktywneID
    print window.sb_adjustment
    if aktywneID[0] == "list":
        for num in range(0, len(aktywneID[1])):
            batteryWindow.add(aktywneID[1][num], aktywneID[1][num]-1)
            window.sb_adjustment[num+1].set_value(aktywneID[1][num]-1)
    else:
        for num in range(1, (aktywneID[1] + 1)):
            batteryWindow.add(num, num)

    # inter.start()
    # mały pokaz nowych funkcji
    '''zmiana nazwy baterii'''
    '''aktualizacja stanu baterii'''

    batteryWindow.show()

    """Trying set object table"""

    Process(target=gtk.main, name="GTK main").start()


if __name__ == "__main__":
    t2 = Process(target=start).start()
def __init__():
    t2 = Process(target=start).start()
#TODO wraz ze zmiana adresu urzadzenia zmiana adresu baterii
#TODO sprawdzanie bledow w tle
#TODO pokomentowc troche :>

def getWho():
    return Who

'''Metoda przeznaczona do wysyłania komend'''
def lightLED(receiver, state, led, option):
    if not dial == 'NO_PORTS':
        str = `receiver` + "." + `state` + "." + `led` + "." + `option` + "."
        dial.serial.SerialSend(str)
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
# activebuttons = True


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

    '''Reakcja na kliknięcie - stara'''
    def reactToKeyBoard(self,Widget,event):
        print self.bt_key_table
        keys = ('1234567890-qwertyuiop[]asdfghjkl;\''+
                'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?')
        keyname = gtk.gdk.keyval_name(event.keyval)
        for i in range(1,ConfigWindow.zmienna2+1):
            # dodatek = 11
            # if (i == 1):
            #     dodatek = 0
            for j in range(1,ConfigWindow.iloscbt+1):
                # if(self.bt_key_table[i][j] == keyname):
                if(keys[i-1+j-1] == keyname):
                    self.click_with_keyboard(self.bt_table[i][j],i,j)
        # for i in range(1,(ConfigWindow.zmienna2)+1):
        #     print self.bt_key_table[i]
        #     if(keyname == self.bt_key_table[i]):
        #         print self.bt_table
        #         self.click_with_keyboard(self.bt_table[i][1],i,1)
    def click_with_keyboard(self,Widget,*Data):
        Widget.set_active(not Widget.get_active())
        state = Widget.get_active()
        print str(Data[0] + 1) + ',' + str(int(state)) + ',' + str(Data[1]) + ',' + str(0)
        lightLED(Data[0] + 1, int(state), Data[1], 0)

    def setKeyboardButtor(self,columnButton, rowButton, key):
        print key
        print "DATA 2"
        if (key != None):
            self.bt_key_table[columnButton][rowButton] = key
    def click(self, Widget ,*Data):
        state = Widget.get_active()
        print str(Data[0] + 1) + ',' + str(int(state)) + ',' + str(Data[1]) + ',' + str(0)
        lightLED(Data[0] + 1, int(state), Data[1], 0)
    '''Reakcja na zmiane adresu'''
    def click_change_address(self, Widget, *Data):
        print "Uwaga dane"

        print self.getBT(Data[0])
        print Data[1]
        changeaddress = changeAddress(self.getBT(Data[0]), Data[1])

    '''Wygaszanie'''
    def blackoutclock(self, Widget, *Data):
        state = Widget.get_active()
        for x in range(1, 3):
            state = Widget.get_active()

            lightLED((Data[0]+1), 0, x, 0)
    '''Zmiana adresu danej kolumy - adresu komunikacyjnego kolumny'''
    def addressValueChange(self, Widget, *Data):
        for bt in range(1, ConfigWindow.iloscbt + 1):

            print Data[2]
            print self.bt_table_id
            self.bt_table[Data[0]][bt].disconnect(self.bt_table_id[Data[0]][bt])
            self.bt_table_id[Data[0]][bt] = self.bt_table[Data[0]][bt].connect('clicked', self.click, self.sb_address[
                Data[0]].get_value_as_int(), bt)


    def addressValueChange2(self, Widget, *Data):
        # for bt in range(1,iloscbt+1):
        print Data[2]
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
    # def keyBoardTable(self):
    #     self.bt_key_table1 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
    #                           6: '6', 7: '7', 8: '8', 9: '9', 10: '0',
    #                           11: '-', 12: '='}
    #     self.bt_key_table2 = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't',
    #                           6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
    #                           11:'[',12:']'}
    #     self.bt_key_table3 = {1: 'a', 2: 's', 3: 'd', 4: 'f', 5: 'g',
    #                           6: 'h', 7: 'j', 8: 'k', 9: 'l', 10: ';',
    #                           11:'\''}
    #     self.bt_key_table4 = {1: 'z', 2: 'x', 3: 'c', 4: 'v', 5: 'b',
    #                           6: 'n', 7: 'm', 8: ',', 9: '.', 10: '/'}
    #
    def __init__(self):
        '''Konstruktor klasy MainWindow'''
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("elSter - console")
        self.window.connect("destroy", self.on_window1_destroy)

        self.window.connect('key_press_event', self.reactToKeyBoard)

        self.window.set_border_width(0)
        self.container = gtk.HBox(gtk.FALSE, ConfigWindow.zmienna+1)
        self.container.set_border_width(10)

        self.vcontainer = gtk.VBox(gtk.FALSE,2)
        self.window.set_default_size((self.size_of_window * ConfigWindow.zmienna) + 70 * ConfigWindow.zmienna * ConfigWindow.iloscbt,
                                      (self.size_of_window * ConfigWindow.iloscbt) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt)

        self.scrolledCol = gtk.ScrolledWindow()
        self.scrolledCol.set_border_width(10)
        #self.scrolledCol.set_resize_mode(True)
        self.scrolledCol.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scrolledCol.set_size_request((self.size_of_window * ConfigWindow.zmienna) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt,
                                      (self.size_of_window * ConfigWindow.iloscbt) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt)

        self.window.add(self.vcontainer)

        self.vcontainer.pack_start(self.menuTool(),False,False,0)
        #self.vcontainer.pack_start(self.container, False, False, 0)

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
        self.bt_key_table = [[None for x in range(ConfigWindow.iloscbt + 1)] for y in range(ConfigWindow.zmienna + 1)]
        self.bt_table_id = [[None for x in range(ConfigWindow.iloscbt + 1)] for y in range(ConfigWindow.zmienna + 1)]
        self.bt_table = [[None for bt_x in range(ConfigWindow.iloscbt + 1)] for bt_y in range(ConfigWindow.zmienna + 1)]
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

                '''Setting button on keyboard'''
                self.setKeyboardButtor(i,bt,'1234567890-=qwertyuiop[]asdfghjkl;\''+
                                            'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?')

                self.bt_id[0] = 0
                try:
                    self.bt_table[i][bt] = self.btBox[bt]
                except IndexError:
                    print 'IndexError'
                self.bt_table_id[i][bt] = self.bt_id[bt]
                print self.btBox[bt]
                print self.bt_table

                self.vBox[i].add(self.btBox[bt])

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
            print self.bt_id
            print self.bt_table_id
            self.vBox[i].add(self.sb_address[i])
            self.printfuckingBT()
        '''Uruchomienie kilku ważnych wewnętrznych metod'''
        self.printfuckingBT()
        self.container.show()
        self.vcontainer.show()
        self.window.show()

        self.scrolledCol.set_visible(True)
        self.scrolledCol.add_with_viewport(self.container)
        self.vcontainer.pack_start(self.scrolledCol, True, True, 0)

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

    def generateSceneWindow(self,args):
        g = generateScene.generateScene()

