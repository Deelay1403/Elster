#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
#import arduino_universal_oriented
import time
from mainSerial import serialComunnication
#arduino_universal = arduino_universal_oriented
class serialWindow():

    def __init__(self):
        self.cb_serial = gtk.ComboBox()
        self.liststore = gtk.ListStore(str)
        self.cell = gtk.CellRendererText()
        self.cb_serial.pack_start(self.cell)
        #self.cb_serial.add(self.cell)
        self.cb_serial.set_wrap_width(5)
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
        '''Create dialog'''
        self.dialog = gtk.Dialog("Configuration",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_APPLY,gtk.RESPONSE_ACCEPT))
        '''Center dialog'''
        self.dialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.dialog.vbox.pack_start(self.cb_serial_frame)
        self.dialog.vbox.add(self.count_frame)
        self.dialog.connect('destroy', gtk.main_quit)
        self.dialog.connect('delete-event', gtk.main_quit)
        self.dialog.connect('close', gtk.main_quit)

        #self.dialog.action_area.pack_start(self.cb_serial)
        #self.dialog.action_area.add(self.cb_serial)

        # x = 0
        # serial_ports = arduino_universal.serialPorts().get()
        # for pack in serial_ports:
        #     self.liststore.append([serial_ports[x]])
        #     x += 1
        x = 0
        self.serial = serialComunnication()
        self.serial_ports = self.serial.GetAvailablePorts()
        print self.serial_ports
        for pack in self.serial_ports:
            self.liststore.append([self.serial_ports[x]])
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
        #Warunek stworzony na szybko by usunąć problem z nieaktywnym portem bez naciśnięcia przycisku "AutoSet"
        if response == gtk.RESPONSE_ACCEPT:
            index = self.cb_serial.get_active()
            print index
            if(index != None):
                self.serial.SerialActivate(index, False)

    def autoset(self,Widget):
        print "INDEX"
        index = self.cb_serial.get_active()
        print index
        self.serial.SerialActivate(index, False)
        print "AUTOSET GET"
        print self.serial.GetOpenPort()
        print "ENDD"
        if self.serial.GetOpenPort() == "NO_PORTS":
            print "zaden statek nie zadokuje :c"
            self.serial = serialComunnication()
            print self.serial.GetAvailablePorts()
            x = 0
            self.liststore.clear()
            for pack in self.serial.GetAvailablePorts():
                #TODO niech nowe porty pojawiaja sie od miejsca 0
                self.liststore.append([self.serial.GetAvailablePorts()[x]])
                x += 1
            return
        #self.liststore.move_before(0) #proba indeksowania od zera? ;_;
        if self.serial.SerialSend("99,4") == "ERR01":
            self.serial.SerialClose()
            self.autoset(Widget)
            return
        time.sleep(2)
        if self.serial.SerialSend("99,5") == "ERR01":
            self.serial.SerialClose()
            self.autoset(Widget)
            return
        komenda = ''
        x = -1;
        line = self.serial.ReadUntil(';')
        if line == "ERR02":
            self.serial.SerialClose()
            self.autoset(Widget)
            return
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

        #TODO: spisac i przekazac aktywne adresy do typu danych dict nastepnie do klasy battery
        self.count_sp_Address.set_value(2)
        self.count_sp_Devices.set_value(x)


    def changed_cb(self, combobox):
        global index
        index = combobox.get_active()
        self.serial.SetSerialIndex(index)
        # if index > -1:
        #     arduino_universal.set_serial(index)
        return
        pass
    def getIndex(self = None):
        return index
        pass

    #zmienna2 = zmienna = iloscbt = 3
    def response(self,Widget,Data):
        self.changed_cb(self.cb_serial)
        global zmienna, zmienna2, iloscbt
        zmienna = self.count_sp_Devices.get_value_as_int()
        zmienna2 = self.count_sp_Devices.get_value_as_int()
        iloscbt = self.count_sp_Address.get_value_as_int()
        pass
