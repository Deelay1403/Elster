#!/usr/bin/env python
import gtk
from threading import Thread
class newWindowToGenerateScene:
    def __init__(self,serial,oldGenerateScene):
        #To work in accept
        self.oldGenerateScene = oldGenerateScene
        #Utworzenie okna
        #Creating a window
        self.window = gtk.Dialog("New Generate",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_APPLY,gtk.RESPONSE_ACCEPT))
        #set possition to center
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.vbox = gtk.VBox(True,2)



        self.adj = {}
        self.SPBtn = {}

        # self.label = [gtk.Label("Scene"),
        #               gtk.Label("Devices"),
        #               gtk.Label("Led")]
        # self.Frame = [gtk.Frame(""),
        #               gtk.Frame(""),
        #               gtk.Frame("")]
        #

        #Creating a label and frame for chboxes
        self.label = [gtk.Label("Devices"),
                      gtk.Label("Led")]
        self.Frame = [gtk.Frame(""),
                      gtk.Frame("")]
        # self.scene = gtk.SpinButton(self.adj[0],0,0)
        # self.devices = gtk.SpinButton(self.adj[1],0,0)
        # self.led = gtk.SpinButton(self.adj[2],0,0)

        #Set all atributes to chkboxes
        for i in range(2):
            self.adj[i] = gtk.Adjustment(1,1,100000,1)
            self.SPBtn[i] = gtk.SpinButton(self.adj[i],0,0)

            self.Frame[i].show()
            self.SPBtn[i].show()
            self.label[i].show()

            self.Frame[i].add(self.label[i])
            self.window.vbox.pack_start(self.Frame[i], False, True)
            self.window.vbox.pack_start(self.SPBtn[i], False, True)

        self.window.connect('destroy', gtk.main_quit)
        self.window.connect('delete-event', gtk.main_quit)
        self.window.connect('close', gtk.main_quit)
        self.window.connect('response',self.Accept)

        self.window.show()
        self.serial = serial
    def Accept(self,widget,seal):
        if(seal==gtk.RESPONSE_ACCEPT):
            self.window.hide()
            self.oldGenerateScene.hide()
            import generateScene
            # g = generateScene.generateScene(int(self.adj[1].get_value()), int(self.adj[2].get_value()),int(self.adj[0].get_value()),serial = self.serial)
            #Deleting a scene :(
            g = generateScene.generateScene(int(self.adj[0].get_value()),
                                            int(self.adj[1].get_value()),
                                            1,
                                            serial=self.serial)
        elif(seal==gtk.RESPONSE_CANCEL):
            gtk.main_quit()
