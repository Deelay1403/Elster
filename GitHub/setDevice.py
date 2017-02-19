#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
#import arduino_universal_oriented
import time
#arduino_universal = arduino_universal_oriented
import mainSerial
class serialWindow:
    def __init__(self):
        print "Aby uruchomić okno wywołaj WALSIENARYJ__init__"
    def WALSIENARYJ__init__(self):
        self.cb_serial = gtk.ComboBox()
        self.liststore = gtk.ListStore(str)
        self.cell = gtk.CellRendererText()
        self.cb_serial.pack_start(self.cell)
        self.cb_serial.add_attribute(self.cell,'text',0)
        self.cb_serial_hbox = gtk.HBox(gtk.FALSE, 0)
        self.cb_serial_hbox.add(self.cb_serial)
        self.cb_serial_hbox.set_border_width(10)
        self.cb_serial_frame = gtk.Frame("Select device")

        self.cb_serial_frame.add(self.cb_serial_hbox)
        self.cb_serial_frame.show()
        self.cb_serial_hbox.show()
        self.dialog = gtk.Dialog("Configuration",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_APPLY,gtk.RESPONSE_ACCEPT))
        self.dialog.vbox.pack_start(self.cb_serial_frame)

        self.dialog.connect('destroy', gtk.main_quit)
        self.dialog.connect('delete-event', gtk.main_quit)
        self.dialog.connect('close', gtk.main_quit)

        self.dialog.action_area.pack_end(self.cb_serial)

        x = 0
        self.serial = mainSerial.serialComunnication()
        serial_ports = self.serial.GetAvailablePorts()

        for pack in serial_ports:
            self.liststore.append([serial_ports[x]])
            x += 1
        self.cb_serial.set_model(self.liststore)

        self.cb_serial.set_active(0)

        self.cb_serial.show()
        response = self.dialog.run()
        self.dialog.destroy()

        if response == gtk.RESPONSE_CANCEL:
            gtk.main_quit()
        if response == gtk.STOCK_CLOSE:
            gtk.main_quit()
        # if response == gtk.RESPONSE_ACCEPT:
        #     return serialWindow
    def getCombobox(self):
        return self.cb_serial
    def response(self,Widget,Data):
        if(Data == gtk.RESPONSE_ACCEPT):
            return self.cb_serial.get_active_text()
