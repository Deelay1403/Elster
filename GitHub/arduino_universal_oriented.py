# import self as self
import Tkinter as tk
import sys
import time

import serial

"""
sudo apt-get install libgtk-3-dev
sudo apt-get install python python-tk idle python-pmw python-imaging
sudo apt-get install python-gtk2
"""

# from numpy.distutils.fcompiler import none
pass
from threading import Thread
import gtk
# import gtk.glade
import glob
from random import randint

import ConfigWindow

x = 1
gladeFileName = "./window.glade"

logo = """
  ____       _              _      ____                      _                       _    _
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


def lightLED(receiver, state, led, option):
    ser.write(`receiver` + "." + `state` + "." + `led` + "." + `option` + ".")
    # ser.write(receiver + "." + state + "." + led + "." + option + ".")


def forLedBlackOutSingle(cstate, check1, check2, bt1, bt2, receiver, state, option):
    check1.set_active(cstate)
    check2.set_active(cstate)
    bt1.set_active(cstate)
    bt2.set_active(cstate)
    for x in range(1, 3):
        lightLED(receiver, state, x, option)


def forLedBlackOutAll(state, option):
    for x in range(2, 7):
        for y in range(1, 3):
            lightLED(x, state, y, option)


# forLedBlackOutAll(0, 0)
activebuttons = True


# Example of callFunctionLightLed();
# def on_togglebutton1_3_toggled(self, widget):callFunctionLightLed(self, self.toggle1_3,self.check1_2, 2, 1, 2, 0)
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


def defineValues(self):
    self.toggle1_1 = self.builder.get_object("togglebutton1_1")
    self.toggle1_2 = self.builder.get_object("togglebutton1_2")
    self.toggle1_3 = self.builder.get_object("togglebutton1_3")
    self.check1_1 = self.builder.get_object("Aktor1_1")
    self.check1_2 = self.builder.get_object("Aktor1_2")
    self.toggle2_1 = self.builder.get_object("togglebutton2_1")
    self.toggle2_2 = self.builder.get_object("togglebutton2_2")
    self.toggle2_3 = self.builder.get_object("togglebutton2_3")
    self.check2_1 = self.builder.get_object("Aktor2_1")
    self.check2_2 = self.builder.get_object("Aktor2_2")
    self.toggle3_1 = self.builder.get_object("togglebutton3_1")
    self.toggle3_2 = self.builder.get_object("togglebutton3_2")
    self.toggle3_3 = self.builder.get_object("togglebutton3_3")
    self.check3_1 = self.builder.get_object("Aktor3_1")
    self.check3_2 = self.builder.get_object("Aktor3_2")
    self.toggle4_1 = self.builder.get_object("togglebutton4_1")
    self.toggle4_2 = self.builder.get_object("togglebutton4_2")
    self.toggle4_3 = self.builder.get_object("togglebutton4_3")
    self.check4_1 = self.builder.get_object("Aktor4_1")
    self.check4_2 = self.builder.get_object("Aktor4_2")
    self.toggle5_1 = self.builder.get_object("togglebutton5_1")
    self.toggle5_2 = self.builder.get_object("togglebutton5_2")
    self.toggle5_3 = self.builder.get_object("togglebutton5_3")
    self.check5_1 = self.builder.get_object("Aktor5_1")
    self.check5_2 = self.builder.get_object("Aktor5_2")

    self.loop6 = self.builder.get_object("loopb6")
    self.toggle_wszyscy = self.builder.get_object("togglebutton_wszyscy")
    self.toggle_blackout = self.builder.get_object("togglebutton_wygas")


# Class to blink in time. It's generated by PyGTK and set value in sec
class blinkInTime():
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('destroy', gtk.main_quit)
        self.window.connect('delete-event', gtk.main_quit)
        # self.window.connect('close',gtk.main_quit)
        self.window.set_border_width(10)
        self.container = gtk.HBox(gtk.FALSE, ConfigWindow.zmienna)
        self.window.add(self.container)
        self.vBox = {}
        self.startBT = {}
        self.HzAdjustment = {}
        self.Spinbutton = {}
        for num in range(1, ConfigWindow.zmienna + 1):
            self.vBox[num] = gtk.VBox(gtk.FALSE, ConfigWindow.zmienna)
            self.startBT[num] = gtk.ToggleButton("Start")
            self.HzAdjustment[num] = gtk.Adjustment(1, 1, 60, 1)
            self.Spinbutton[num] = gtk.SpinButton(self.HzAdjustment[num], 0, 0)

            self.container.add(self.vBox[num])
            self.vBox[num].show()

            self.vBox[num].add(self.Spinbutton[num])
            self.vBox[num].add(self.startBT[num])

            self.Spinbutton[num].show()
            self.startBT[num].show()
        self.container.show()
        self.window.show()


class changeAddress():
    def __init__(self, Who, spBut):
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
        self.New_address = 0
        self.Who = Who + 1
        self.spBut = spBut
        self.dialog.connect('response', self.response)

    def setWho(self, s):
        self.Who = s

    def response(self, Widget, data):
        self.New_address = self.adjustment.get_value() + 1
        print self.New_address
        print self.Who
        print str(int(self.Who)) + " 4 " + str(int(self.New_address)) + " 0"
        lightLED(int(self.Who), 4, int(self.New_address), 0)
        self.spBut.set_value(self.New_address)

    def getNewAddress(self):
        return self.New_address


"""
class serialWindow:

    def __init__(self):
        self.cb_serial = gtk.ComboBox()
        self.liststore = gtk.ListStore(str)
        self.cell = gtk.CellRendererText()
        self.cb_serial.pack_start(self.cell)
        #self.cb_serial.set_wrap_width(5)
        self.cb_serial.add_attribute(self.cell,'text',0)
        self.cb_serial_hbox = gtk.HBox(gtk.FALSE, 0)
        self.cb_serial_hbox.add(self.cb_serial)
        self.cb_serial_hbox.set_border_width(10)
        self.cb_serial_frame = gtk.Frame("Select device")

        self.count_frame = gtk.Frame("Configuration")
        self.count_hbox = gtk.VBox(gtk.FALSE,2)
        self.count_hbox.set_border_width(10)
        self.count_frame.add(self.count_hbox)

        self.coun_adjustment_dev = gtk.Adjustment(1,1,100,1)
        self.coun_adjustment_adr = gtk.Adjustment(1, 1, 100, 1)
        self.count_sp_Devices = gtk.SpinButton(self.coun_adjustment_dev,0,0)

        self.count_sp_Devices_title = gtk.Label("Devices")
        self.count_sp_Devices_title.set_alignment(0,0.5)
        self.count_sp_Address_title = gtk.Label("Led's")
        self.count_sp_Address_title.set_alignment(0, 0.5)

        self.count_sp_Address = gtk.SpinButton(self.coun_adjustment_adr,0,0)

        self.count_bt_auto = gtk.Button("Auto set")
        # W oczekiwaniu na Oskara
        self.count_bt_auto.connect('clicked',self.autoset)


        self.count_hbox.add(self.count_sp_Devices_title)
        self.count_hbox.add(self.count_sp_Devices)
        self.count_hbox.add(self.count_sp_Address_title)
        self.count_hbox.add(self.count_sp_Address)

        self.count_hbox.add(self.count_bt_auto)

        self.count_frame.show()
        self.count_hbox.show()
        self.count_sp_Devices.show()
        self.count_sp_Devices_title.show()
        self.count_sp_Address.show()
        self.count_sp_Address_title.show()
        self.count_bt_auto.show()

        self.cb_serial_frame.add(self.cb_serial_hbox)
        self.cb_serial_frame.show()
        self.cb_serial_hbox.show()
        self.dialog = gtk.Dialog("Configuration",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_APPLY,gtk.RESPONSE_ACCEPT))
        self.dialog.vbox.pack_start(self.cb_serial_frame)
        self.dialog.vbox.add(self.count_frame)
        self.dialog.connect('destroy', gtk.main_quit)
        self.dialog.connect('delete-event', gtk.main_quit)
        self.dialog.connect('close', gtk.main_quit)

        self.dialog.action_area.pack_end(self.cb_serial)

        x = 0
        for pack in serial_ports:
            self.liststore.append([serial_ports[x]])
            x += 1
        self.cb_serial.set_model(self.liststore)
        self.cb_serial.connect('changed', self.changed_cb)
        self.dialog.connect('response', self.response)
        self.cb_serial.set_active(0)

        self.cb_serial.show()
        response = self.dialog.run()
        self.dialog.destroy()

        if response == gtk.RESPONSE_CANCEL:
            gtk.main_quit()
        if response == gtk.STOCK_CLOSE:
            gtk.main_quit()

    def autoset(self,Widget):
        serialActivate()
        ser.write("99,4")
        time.sleep(2)
        ser.write("99,5")
        komenda = ''
        k = ser.read_until(';')
        x = -1;
        line = ser.read_until(';')
        line = line.strip("\r\n")
        print line
        if line.startswith('ACT_'):  # szuka odpowiedzniej komendy
            raw = line.strip('ACT_;\n')  # "oczyszcza" ja
            print 'komenda ' + raw
            while 1:
                ++x
                try:
                    print raw.split(':')[x]
                except IndexError:
                    break

        self.count_sp_Address.set_value(2)
        self.count_sp_Devices.set_value(x)


    def changed_cb(self, combobox):
        index = combobox.get_active()
        if index > -1:
            set_serial(index)
        return
    #zmienna2 = zmienna = iloscbt = 3
    def response(self,Widget,Data):
        self.changed_cb(self.cb_serial)
        global zmienna, zmienna2, iloscbt
        zmienna = self.count_sp_Devices.get_value_as_int()
        zmienna2 = self.count_sp_Devices.get_value_as_int()
        iloscbt = self.count_sp_Address.get_value_as_int()"""


class Mainwindow:
    def on_window1_destroy(self, object, data=None):
        print ("quit with cancel")
        gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print ("quit from menu")
        gtk.main_quit()

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

    def click(self, Widget, *Data):
        # print Data[0]
        state = Widget.get_active()
        print str(Data[0] + 1) + ',' + str(int(state)) + ',' + str(Data[1]) + ',' + str(0)
        lightLED(Data[0] + 1, int(state), Data[1], 0)

    def click_change_address(self, Widget, *Data):
        print "Uwaga dane"
        print Data[0]
        print Data[1]
        changeaddress = changeAddress(Data[0], Data[1])
        #  Data[1].set_value(changeaddress.getNewAddress())

    def blackoutclock(self, Widget, *Data):
        state = Widget.get_active()
        for x in range(1, 3):
            state = Widget.get_active()
            lightLED(Data[0], state, x, 0)

            # TODO: Make it fucking works !
            # This function is fucking annoying

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

    def printfuckingBT(self):
        print "FUCK"
        print self.bt_table_id

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.on_window1_destroy)
        self.window.set_border_width(10)
        self.container = gtk.HBox(gtk.FALSE, ConfigWindow.zmienna)
        self.window.set_default_size((self.size_of_window * ConfigWindow.zmienna) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt,
                                     (self.size_of_window * ConfigWindow.iloscbt) + 10 * ConfigWindow.zmienna * ConfigWindow.iloscbt)
        self.window.add(self.container)
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
        for num in range(1, ConfigWindow.zmienna + 1):
            self.vBox[num] = gtk.VBox(gtk.FALSE, ConfigWindow.zmienna)
            self.container.add(self.vBox[num])
            self.vBox[num].show()

        for i in range(1, ConfigWindow.zmienna2 + 1):
            self.sb_adjustment[i] = gtk.Adjustment(i, 1, 100, 1, 5, 0)
            self.sb_address[i] = gtk.SpinButton(self.sb_adjustment[i], 0, 0)

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
            self.bt_address[i].connect("clicked", self.click_change_address, self.sb_adjustment[i].get_value(),
                                       self.sb_adjustment[i])
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

        self.printfuckingBT()

        self.container.show()
        self.window.show()


        # self.gladefile = gladeFileName
        # self.builder = gtk.Builder()
        #
        # self.builder.add_from_file(self.gladefile)
        # self.builder.connect_signals(self)
        #
        # self.window = self.builder.get_object("window1")
        # self.window.connect("key_press_event", self.on_key_press)
        # #self.window2 = self.builder.get_object("window2")
        # self.window.show()
        # #self.window2.show()
        # self.window.set_size_request(640,320)
        # self.window2.set_size_request(320,320)

        # self.textview1 = self.builder.get_object("textview1")
        # self.textbuffer = self.textview1.get_buffer()
        # self.detail = self.builder.get_object("textview1").get_buffer()
        # self.textbuffer.set_text("123")
        # dv = defineValues(self)

    def activecheck(self, chbutton):
        print "kek"

    # def on_togglebutton1_1_toggled(self, widget):
    #     if (activebuttons == True):
    #         forLedBlackOutSingle(2, 0, 0)
    #         self.activecheck(self)
    def on_togglebutton1_1_toggled(self, widget):
        forLedBlackOutSingle(False, self.check1_1, self.check1_2, self.toggle1_2, self.toggle1_3, 2, 0, 0)

    def on_togglebutton2_1_toggled(self, widget):
        forLedBlackOutSingle(False, self.check2_1, self.check2_2, self.toggle2_2, self.toggle2_3, 3, 0, 0)

    def on_togglebutton3_1_toggled(self, widget):
        forLedBlackOutSingle(False, self.check3_1, self.check3_2, self.toggle3_2, self.toggle3_3, 4, 0, 0)

    def on_togglebutton4_1_toggled(self, widget):
        forLedBlackOutSingle(False, self.check4_1, self.check4_2, self.toggle4_2, self.toggle4_3, 5, 0, 0)

    def on_togglebutton5_1_toggled(self, widget):
        forLedBlackOutSingle(False, self.check5_1, self.check5_2, self.toggle5_2, self.toggle5_3, 6, 0, 0)

    def on_togglebutton1_2_toggled(self, widget):
        callFunctionLightLed(self, self.toggle1_2, self.check1_1, 2, 1, 1, 0)

    def on_togglebutton1_3_toggled(self, widget):
        callFunctionLightLed(self, self.toggle1_3, self.check1_2, 2, 1, 2, 0)

    def on_togglebutton2_2_toggled(self, widget):
        callFunctionLightLed(self, self.toggle2_2, self.check2_1, 3, 1, 1, 0)

    def on_togglebutton2_3_toggled(self, widget):
        callFunctionLightLed(self, self.toggle2_3, self.check2_2, 3, 1, 2, 0)

    def on_togglebutton3_2_toggled(self, widget):
        callFunctionLightLed(self, self.toggle3_2, self.check3_1, 4, 1, 1, 0)

    def on_togglebutton3_3_toggled(self, widget):
        callFunctionLightLed(self, self.toggle3_3, self.check3_2, 4, 1, 2, 0)

    def on_togglebutton4_2_toggled(self, widget):
        callFunctionLightLed(self, self.toggle4_2, self.check4_1, 5, 1, 1, 0)

    def on_togglebutton4_3_toggled(self, widget):
        callFunctionLightLed(self, self.toggle4_3, self.check4_2, 5, 1, 2, 0)

    def on_togglebutton5_2_toggled(self, widget):
        callFunctionLightLed(self, self.toggle5_2, self.check5_1, 6, 1, 1, 0)

    def on_togglebutton5_3_toggled(self, widget):
        callFunctionLightLed(self, self.toggle5_3, self.check5_2, 6, 1, 2, 0)

    # def activecheck(self, chbutton):
    #     print "kek"
    # def on_togglebutton1_1_toggled(self,widget):
    #     if (activebuttons == True):
    #         forLedBlackOutSingle(2,0,0)
    #         self.activecheck(self)
    # def on_togglebutton1_2_toggled(self,widget):
    #   if (activebuttons == True):
    #       lightLED(2,1,1,0)
    #       self.activecheck(self)
    #       if (self.toggle1_2.get_active() == False):
    #           lightLED(2, 0, 1, 0)
    #           self.activecheck(self)
    # def on_togglebutton1_3_toggled(self,widget):
    #
    # def on_togglebutton2_1_toggled(self,widget):
    #     if (activebuttons == True):
    #         forLedBlackOutSingle(3,0,0)
    #         self.activecheck(self)
    # def on_togglebutton2_2_toggled(self,widget):
    #   if (activebuttons == True):
    #       lightLED(3,1,1,0)
    #       self.activecheck(self)
    #       if (self.toggle2_2.get_active() == False):
    #           lightLED(3, 0, 1, 0)
    #           self.activecheck(self)
    # def on_togglebutton2_3_toggled(self,widget):
    #       if (activebuttons == True):
    #           lightLED(3,1,2,0)
    #           self.activecheck(self)
    #           if (self.toggle2_3.get_active() == False):
    #               lightLED(3,0,2,0)
    #               self.activecheck(self)
    #
    # def on_togglebutton2_3_toggled(self, widget):
    #     if (activebuttons == True):
    #         lightLED(3, 1, 2, 0)
    #         self.activecheck(self)
    #         if (self.toggle2_3.get_active() == False):
    #             lightLED(3, 0, 2, 0)
    #             self.activecheck(self)

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


# #support LINUX - Ubuntu
# try:
#     print("trying /dev/ttyACM0/")
#     ser = serial.Serial('/dev/ttyACM0', 9600)
#     print("/dev/ttyACM0/ found!! \n")
# except serial.SerialException:
#     print('/dev/ttyACM0/ not found\n')
#     pass
# try:
#     print ('trying /dev/ttyACM1/')
#     ser = serial.Serial('/dev/ttyACM1', 9600)
#     print("/dev/ttyACM1/ found!! \n")
# except serial.SerialException:
#     print ('/dev/ttyACM1/ not found\n')
# try:
#     print ('trying /dev/ttyACM2/')
#     ser = serial.Serial('/dev/ttyACM2', 9600)
#     print("/dev/ttyACM2/ found!! \n")
# except serial.SerialException:
#     print ('/dev/ttyACM2/ not found\n')
#     pass
# try:
#     print ('trying /dev/ttyACM3/')
#     ser = serial.Serial('/dev/ttyACM3', 9600)
#     print("/dev/ttyACM3/ found!! \n")
# except serial.SerialException:
#     print ('/dev/ttyACM2/ not found\n')
#     pass
#
# #support Mac OS X
# try:
#     print("trying /dev/tty.usbmodem/")
#     ser = serial.Serial('/dev/tty.usbmodem',9600)
#     print("/dev/tty.usbmodem/ found!! \n")
# except serial.SerialException:
#     print('/dev/tty.usbmodem not found\n')
#     pass
#
# try:
#     print("trying /dev/tty.usbmodem/")
#     ser = serial.Serial('/dev/tty.usbserial',9600)
#     print("/dev/tty.usbserial/ found!! \n")
# except serial.SerialException:
#     print('/dev/tty.usbserial not found\n')
#     pass


# Serial detect!

def serial_ports():
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
    result = []
    for port in ports:
        try:
            # Trying if ports are open
            s = serial.Serial(port)
            s.close()
            result.append(port)
        # if OS is diferent it pass program without connect serial
        except (OSError, serial.SerialException):
            pass
    return result


serial_ports = serial_ports()


def set_serial(serial):
    global index
    index = serial
    print index


for situation in serial_ports:
    print str(x) + ": " + situation
    x += 1


def keylisten(event):
    print(event.char)


def keyrequest():
    root = tk.Tk()
    root.bind('<KeyPress>', keylisten)
    root.mainloop()


time.sleep(2)


def serialActivate(dial):
    global ser
    ser = serial.Serial(serial_ports[dial.getIndex()], 9600)


def getSer():
    return ser


def start():
    dial = ConfigWindow.serialWindow()
    serialActivate(dial)
    # global ser
    # ser = serial.Serial(serial_ports[index], 9600)
    # ser.re
    app = Mainwindow()
    app2 = blinkInTime()
    gtk.main()
    t3 = Thread(name="key", target=keyrequest())
    t3.start()


if __name__ == "__main__":
    # t = Thread(name="log", target=log("lel"))
    # t.setDaemon(True)
    t2 = Thread(name="main", target=start)

    # t.start()
    t2.start()
