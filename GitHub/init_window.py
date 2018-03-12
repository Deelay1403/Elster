#!/usr/bin/env python
#-*- coding: utf-8 -*-
import gtk
from multiprocessing import Process


class initWindow:
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_title("Start")
        self.vbox = gtk.VBox(2, True)
        self.generateSceneBt = gtk.Button("Włącz Generator Scen")
        self.arduinoUniversalOriented = gtk.Button("Włącz konsolę")

        self.generateSceneBt.connect("clicked", self.generateSceneDef)
        self.arduinoUniversalOriented.connect("clicked", self.arduinoUniversalOrientedDef)

        self.window.add(self.vbox)

        self.vbox.pack_start(self.arduinoUniversalOriented)
        self.vbox.pack_start(self.generateSceneBt)

        self.window.show()
        self.vbox.show()
        self.generateSceneBt.show()
        self.arduinoUniversalOriented.show()

    def generateSceneDef(self,args):

        self.target = "generateScene.generateScene()"
        p1 = Process(target=self.createObjectGenerate()).start()
        #g = generateScene.generateScene()
        self.window.hide()

    def arduinoUniversalOrientedDef(self,args):

        self.window.hide()
        # a = arduino_universal_oriented.start(self)
        self.target = "arduino_universal_oriented.start(self)"
        p2 = Process(target=self.createObjectArduino()).start()

    def createObjectGenerate(self):
        import generateScene
        self.g = generateScene.generateScene()

    def createObjectArduino(self):
        import arduino_universal_oriented
        self.a = arduino_universal_oriented.start()


if __name__ == "__main__":
    i = initWindow()
    gtk.main()
def __init__():
    i = initWindow()
    gtk.main()