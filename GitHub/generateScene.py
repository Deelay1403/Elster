#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Patryk Szczodrowski\n
Date of last update: 03.11.16\n
Class created to generate/open file of scenes designed to work with elSter Light System
In easy way, this class can open way to simple work with light
'''
import gtk

# TODO: 1.Make changebutton responsible to call -> Throw it to the table
# TODO: 2.Create method to read/write file and generate window
# TODO: 3.Make it look better
# TODO: 4.Drink coffee - You deserve :)
# TODO: 5.Talk with Popcorator


class generateScene():
    """
    PL:Konstruktor klasy generateScene():
    ENG:generateScene() class constructor
    """
    def __init__(self, colums_main = 0, devices = 0):
        self.horizontal = 5
        self.microContainers = [[0 for x in range(self.checkInput(colums_main, self.horizontal))] for y in
                                range(self.horizontal)]
        self.devices = devices

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy",gtk.main_quit)
        self.main_window_col = gtk.VBox(gtk.FALSE,3)
        self.window.add(self.main_window_col)
        #self.line_window_bottom = gtk.HBox(gtk.FALSE,4)
        self.main_window_col.pack_start(self.menuTool(), False, False, 0)
        if colums_main !=0 | devices !=0:
            try:
                self.table = gtk.Table(self.checkInput(colums_main,self.horizontal), self.horizontal, True)

                self.napis = [[0 for x in range(self.checkInput(colums_main, self.horizontal))] for y in range(colums_main)]
                for x in range(0,colums_main):
                    for y in range(0, self.checkInput(colums_main,self.horizontal)):
                        self.napis[x][y] = gtk.Button("Test")
                        self.napis[x][y].show()

                for x in range(0,self.checkInput(colums_main,self.horizontal)):
                    print str(x) + " " + str(colums_main)
                    if(colums_main>5):
                        for y in range(0, self.horizontal):
                            self.generateSingleContainer(y, x)
                            self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)
                            colums_main-=1
                    elif (colums_main <= 5):
                        for y in range(0, colums_main):
                            self.generateSingleContainer(y, x)
                            self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)
                self.table.show()
                self.main_window_col.pack_start(self.table, True, True, 0)
            except(IndexError):
                print "lel"
        else:
            containerToFill = gtk.Table(3,3,True)
            containerToFill.show()
            self.main_window_col.pack_start(containerToFill,True,True,0)

        # for x in range(0,colums_main):
        #     for y in range(0, self.checkInput(colums_main,horizontalValue)):
        #         self.generateSingleContainer(x, y)
        #         self.table.attach(self.microContainers[x][y],x,x+1,y,y+1)



        # self.main_window_col.add(self.x_Box)
        #
        # for num in range(0,3):
        #     self.x_Box.add(self.y_Box[num])
        #     self.y_Box[num].show()
        #     for i in range(0,3):
        #         self.y_Box[num].add(self.napis[num][i])
          #  for i in range(0,3):
           #     self.y_Box[num].add(self.napis)

        self.main_window_col.pack_start(self.MainBottom(),False,False,0)

        self.window.show()
        self.main_window_col.show()
        #self.line_window_bottom.show()
        self.menu.show()
        # self.x_Box.show()
    #Metoda do przekonwertowania ilości urządzeń do tablicy kontenerów
    def checkInput(self, number,column):
        if(number%column==0):
            return (number/column)
        else:
            return ((number/column)+1)

    #Metoda do generowania pojedyńczego kontenera
    def generateSingleContainer(self,x,y):
        self.microContainers[x][y] = gtk.VBox(gtk.FALSE,self.devices+1)
        self.chkbx = {}
        self.entry = gtk.Entry()
        self.entry.set_text("LED " + str(x + 1) + "." + str(y + 1))
        self.entry.show()
        self.microContainers[x][y].show()

        for i in range(0,self.devices):
            self.chkbx[i] = gtk.CheckButton("LED"+str(i+1))
            self.chkbx[i].show()

        self.microContainers[x][y].pack_start(self.entry,False,False,0)

        for i in range(0,self.devices):
            self.microContainers[x][y].pack_start(self.chkbx[i],False,False,0)

    #Metoda do generowania paska menu
    def menuTool(self):
        self.menu = gtk.Menu()
        self.firstMenuitem = {}
        self.firstMenuitem[0] = gtk.MenuItem("Nowy")
        self.firstMenuitem[1] = gtk.MenuItem("Otworz")
        self.firstMenuitem[2] = gtk.MenuItem("Zapisz")
        self.firstMenuitem[3] = gtk.MenuItem("Zamknij")
        for i in range(0,len(self.firstMenuitem)):
            self.menu.append(self.firstMenuitem[i])
            self.firstMenuitem[i].show()

        self.firstMenuitem[0].connect("activate", self.fileInterpret,'new')
        self.firstMenuitem[1].connect("activate", self.fileInterpret,'open')
        self.firstMenuitem[2].connect("activate", self.fileInterpret,'save')
        self.firstMenuitem[3].connect("activate", gtk.main_quit)
        self.root = gtk.MenuItem("Plik")

        self.root.show()
        self.root.set_submenu(self.menu)
        self.menu_bar = gtk.MenuBar()
        self.menu_bar.show()
        self.menu_bar.append(self.root)

        self.menu.show()

        return self.menu_bar
    """
    BEGIN
    D:5 L:2 S:5.
    S:1.
    1:10.
    2:01.
    3:11.
    4:11.
    5:00.
    -
    S:2.
    ...
    END

    """
    def fileInterpret(self,widget,option):
        self.File = self.fileOpen_Choose_Save(widget, option)
        if self.File != None:
            print self.File
            if option == 'open':
                buffer = self.File['read'].readlines()
                self.fileParserOpen(buffer)
                # self.napis = [[0 for x in range(self.checkInput(, ))] for y in
                #               range()]
        self.File['read'].close()

    def fileParserOpen(self,buffer):
        #Get all str(file)
        sbuffer = str(buffer)
        #Convert into list without dot
        list = sbuffer.split(".")
        print list[1]
        #Convert into sublist without comma
        listOfComma = list[1].split(",")
        print listOfComma
        #Run window with value from file
        print self.firstArgumentParse(listOfComma,1)
        self.__init__(int(self.firstArgumentParse(listOfComma,1)),int(self.firstArgumentParse(listOfComma,2)))
        self.obj["label"].set_label("1/" + str(self.firstArgumentParse(listOfComma,3)))
    def firstArgumentParse(self,listOfComma,number):
        num = 0
        for x in range(0,len(listOfComma[number])):
            if listOfComma[number][x] == ":":
                 num = listOfComma[number][x+1:]
        return num
    def fileOpen_Choose_Save(self,widget,option):
        chooser = self.switch_choose(option)
        response = chooser.run()
        self.file = {}
        if response == gtk.RESPONSE_OK:
            name = chooser.get_filename()
            self.file['read'] = self.fileOpen(name,"rw")
            # self.file['write'] = self.fileOpen(name,"w")
            self.file['append'] = self.fileOpen(name, "a")
            chooser.destroy()
            return self.file
        if response == gtk.RESPONSE_CANCEL:
            chooser.destroy()
            return None
        chooser.destroy()
        return 0
    def fileOpen(self, file,mode):
        return open(file,mode)

    #Switch to decite which dialog is suppose to call

    def switch_choose(self,x):
        return {
            'open' : gtk.FileChooserDialog(title="FileMenu", action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                        buttons=(
                                        gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK)),

            'save' : gtk.FileChooserDialog(title="FileMenu", action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                        buttons=(
                                        gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)),

            'new' : gtk.FileChooserDialog(title="FileMenu", action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        buttons=(
                                        gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_NEW, gtk.RESPONSE_OK))
        }.get(x,gtk.FileChooserDialog(title="FileMenu", action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        buttons=(
                                        gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_NEW, gtk.RESPONSE_OK)))
    def MainBottom(self):
        self.container = gtk.HBox(gtk.FALSE,4)
        self.obj = {}
        self.obj["label"] = self.obj[0] = gtk.Label("-/-")
        self.obj["edit"] = self.obj[1] = gtk.Button("Edytuj")
        self.obj["leftbt"] = self.obj[2] = gtk.Button("<")
        self.obj["rightbt"] = self.obj[3] = gtk.Button(">")


        for i in range(0,4):
            self.obj[i].show()
            if(i!=1):
                self.container.pack_start(self.obj[i],False,False,0)
            else:
                self.container.pack_start(self.obj[i],True,True,0)

        self.obj["edit"].set_size_request(-1,-1)
        self.obj["label"].set_size_request(50,-1)
        self.obj["leftbt"].set_size_request(40,-1)
        self.obj["rightbt"].set_size_request(40, -1)

        self.container.show()
        return self.container

if __name__ == "__main__":
    g = generateScene()
    gtk.main()