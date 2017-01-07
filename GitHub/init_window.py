#!/usr/bin/env python
#-*- coding: utf-8 -*-
import gtk



class initWindow:
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Start")
        self.vbox = gtk.VBox(2, True)
        self.generateSceneBt = gtk.Button("Włącz Generator Scen")
        self.arduinoUniversalOriented = gtk.Button("Włącz konsole")

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
        import generateScene
        g = generateScene.generateScene()
        self.window.hide()

    def arduinoUniversalOrientedDef(self,args):
        import arduino_universal_oriented
        a = arduino_universal_oriented.start()
        self.window.hide()


if __name__ == "__main__":
    i = initWindow()
    gtk.main()
def __init__():
    i = initWindow()
    gtk.main()