#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Patryk Szczodrowski\n
Date of last update: 24.12.16\n
Values: int devices = 0,
        int LED's = 0,
        int scenes = 0,
        three dimenstional array = [],
        two dimenstional array = [],
        object serial = None,
        two dimenstional array = []

                colums_main = 0,
                devices = 0,
                number_of_scenes = 0,
                body = [],
                meta = [],
                serial = None,
                names=[]

(Default values, named differend in constructor)
Class created to generate/open file of scenes designed to work with elSter Light System
In easy way, this class can open way to simple work with light

#need to install librsvg if doesn't work
'''
import gtk
import pickle
import newWindowToGenerateScene
from threading import Thread
import serial
import setDevice
"""
Typical file:

(lp0
I2
aI5
aI2
a.(lp0
(lp1
(lp2
I0
aI1
aa(lp3
I0
aI0
aa(lp4
I0
aI0
aa(lp5
I0
aI0
aa(lp6
I0
aI0
aaa(lp7
(lp8
I0
aI0
aa(lp9
I0
aI0
aa(lp10
I0
aI0
aa(lp11
I0
aI0
aa(lp12
I0
aI0
aaa.
    """

class generateScene():
    """
    PL:Konstruktor klasy generateScene():
    ENG:generateScene() class constructor
    """
    def __init__(self, colums_main = 0,
                 devices = 0,
                 number_of_scenes = 0,
                 body = [],
                 meta = [],
                 serial = None,
                 names=[]):

        t3 = Thread(name="main",target=self.wind(colums_main=colums_main,
                                                 devices=devices,
                                                 number_of_scenes=number_of_scenes,
                                                 body=body,
                                                 meta=meta,
                                                 serial=serial,
                                                 names=names))
        t3.daemon = True
        t3.start()
        t3.join()

    def wind(self, colums_main = 0,
             devices = 0,
             number_of_scenes = 0,
             body = [],
             meta = [],
             serial = None,
             names=[]):

        '''Wind like Wind Of The Change'''
        """Ustawienie serialu by potem być w stanie sprawdzać go w live mode"""
        self.serial = serial
        """To sendNames"""
        self.nevermind = 0
        """Ustawienie canILive dla każdego chkbox - W celu zniwelowania błędów"""
        self.canILive = False
        self.startScene = 1
        if(number_of_scenes==0):
            self.startScene = 0
        self.activeDevice = 0
        self.head_tab = [number_of_scenes, colums_main,devices]
        '''For all methods with chkbtn's'''
        self.chkbtn_tab = {}
        for j in range(self.head_tab[1]):
            self.chkbtn_tab[j] = {}
        '''
        ________________________________________________________________________________
        |                                                                               |
        |     head_tab                                                                  |
        |                                                                               |
        |       0           1           2                                               |
        |    scenes       Devices     "Leds"                                            |
        |                                                                               |
        |   meta_tab                                                                    |
        |_______________________________________________________________________________|

    scenes
    ↓         0           1           2                3
        0     time        loops     description   count of loops
        1
        2
        3

            body_tab
                    x →
                    "LEDS" →
        y             0            1               2
      devices   0    status        status        status
         ↓      1
                2
                3

    Scenes ↗

          ↗
        z
                            4   scene 5
                        3   scene 4
                    2   scene 3
                1   scene 2
            0   scene 1

        '''
        self.meta_tab = [[0 for i in range(4)]for l in range(self.head_tab[0])]

        self.body_tab = [[[0 \
                        for l in range(self.head_tab[2])] \
                        for d in range(self.head_tab[1])] \
                        for s in range(self.head_tab[0])]

        self.names_tab = [(("Aktor ")+str(j+1)) for j in range(self.head_tab[1])]
        '''automatically fill body_tab with body (when body != [])'''
        if(body != []):
            for x in range(self.head_tab[0]):
                for y in range(self.head_tab[1]):
                    for z in range(self.head_tab[2]):
                        self.body_tab[x][y][z] = body[x][y][z]

        print self.head_tab[0]

        if(meta != []):
            for x in range(self.head_tab[0]):
                for y in range(4):
                    print str(x) + " x"
                    print str(y) + " y"
                    self.meta_tab[x][y] = meta[x][y]

        print "ostatnia szansa"
        print names
        if(names != []):
                for y in range(self.head_tab[1]):
                    self.names_tab[y] = names[y]
        # print self.head_tab
        # print "META"
        # print self.meta_tab
        # print self.body_tab
        # print "Names"
        # print self.names_tab



        #self.changeSceneOnBottom(1,number_of_scenes)
        '''This sets max number of devices in one row'''
        self.horizontal = 5
        '''Set table of containers'''

        self.microContainers = [[0 for x in range(self.checkInput(colums_main, self.horizontal))] for y in
                                range(self.horizontal)]
        self.devices = devices

        '''Make main window'''

        '''Trying to set up icon'''

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #icon_theme = gtk.icon_theme_get_default()
        print "Hehe"

        #pixbuf = gtk.gdk.pixbuf_new_from_file_at_size("./img/batt0.png", 48, 48)
        #pixbuf = icon_theme.load_icon("./img/batt0.png", 48, 0)

        #need to install librsvg if doesn't work

        #windowicon = self.window.set_icon_from_file("./yfc.ico")
        #self.window.set_icon(windowicon)
        print "OK"
        # try:
        #     pixbuf = icon_theme.load_icon("./img/batt0.png", 48, 0)
        # except:
        #     print "can't load icon"
        #self.window.set_icon_from_file("./yfc.ico")
        #gtk.window_set_default_icon_from_file("./img/batt0.png")
        try:
            self.window.set_icon_from_file("./GitHub/yfc.ico")
        except:
            try:
                self.window.set_icon_from_file("./yfc.ico")
            except:
                print "Icon error"
        print self.window.get_icon()
        self.window.set_gravity(gtk.gdk.GRAVITY_CENTER)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

        '''Add keyboard event'''
        self.window.connect('key_press_event', self.reactToKeyBoard)

        print self.window.get_gravity()
        self.window.connect("destroy",gtk.main_quit)
        self.main_window_col = gtk.VBox(gtk.FALSE,3)

        '''Add to main window main container'''

        self.window.add(self.main_window_col)

        '''self.line_window_bottom = gtk.HBox(gtk.FALSE,4)'''
        #
        self.main_window_col.pack_start(self.menuTool(), False, False, 0)

        self.scrolledCol = gtk.ScrolledWindow()
        self.scrolledCol.set_border_width(10)
        self.scrolledCol.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        '''If enter values equals 0, then program won't generate singleContainers'''

        if colums_main != 0 or devices != 0:
            try:
                '''Set value self.table as gtk.Table'''
                '''gtk.Table looks like two-dimenstional array. If we set parameters as 3 and 3 it would look like:

                Y
                  00   -   01   -   02
                  10   -   11   -   12
                  20   -   21   -   22
                                       X

                '''

                self.table = gtk.Table(self.checkInput(colums_main,self.horizontal), self.horizontal, True)
                ''' Test string'''
                self.napis = [[0 for x in range(self.checkInput(colums_main, self.horizontal))]
                              for y in range(colums_main)]
                for x in range(0,colums_main):
                    for y in range(0, self.checkInput(colums_main,self.horizontal)):
                        self.napis[x][y] = gtk.Button("Test")
                        self.napis[x][y].show()
                '''Do loop which add elements to array od objects. This objects will show as singleConstainers'''
                '''t array for Thread with containers'''
                #t = [[0 for x in range(self.head_tab[1] / 5)] for y in range(self.horizontal)]
                for x in range(0,self.checkInput(colums_main,self.horizontal)):
                    print str(x) + " " + str(colums_main)
                    '''When devices is more than 5, program will render this in 2+ line'''
                    if(colums_main>5):
                        for y in range(0, self.horizontal):
                            #t[x][y] = Thread(target=self.generateSingleContainer(y, x,self.activeDevice)).start()
                            #t = Thread(target=self.generateSingleContainer(y, x, self.activeDevice)).start()
                            self.generateSingleContainer(y, x, self.activeDevice)
                            self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)
                            self.activeDevice +=1
                            colums_main-=1

                        '''When devices is less than 5, program will render 1 line'''
                    elif(colums_main <= 5):
                        for y in range(0, colums_main):
                         #  t[x][y] = Thread(target=self.generateSingleContainer(y, x, self.activeDevice)
                         #              ).start()
                            #t = Thread(target=self.generateSingleContainer(y, x, self.activeDevice)).start()
                            self.generateSingleContainer(y, x, self.activeDevice)
                            self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)
                            self.activeDevice+=1
                            print self.activeDevice
                self.table.show()
                '''Add gtk.table to main container'''
                self.scrolledCol.add_with_viewport(self.table)
                #self.scrolledCol.set_resize_mode(True)
                self.scrolledCol.set_visible(True)
                #self.main_window_col.pack_start(self.scrolledCol, True, True, 0)
                self.main_window_col.add(self.scrolledCol)
                #self.main_window_col.pack_start(self.table, True, True, 0)
            except(IndexError):
                print "IndexError"
        else:
            '''Method to generate any table if values are bad or don't exist'''
            containerToFill = gtk.Table(3, 3, True)
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
        self.fileMenusub.show()
        '''This react to body_tab and set status of all chkbtn's'''
        self.changeChkbtnActive(self.startScene)
        # self.x_Box.show()
        '''Metoda do przekonwertowania ilości urządzeń do tablicy kontenerów
        Method to convert a number of devices to container array
        '''

        '''Print head_tab just for create function'''
        print "UWAGA LECI GŁOWA"
        print self.meta_tab

    def changeSceneOnBottom(self, actualScene, oldScene):
        # self.obj["label"].set_text("lel")
        self.btnsWithoutEdit["label"].set_label(str(actualScene) + "/" + str(oldScene))
    def checkInput(self, number,column):
        if(number%column==0):
            return (number/column)
        else:
            return ((number/column)+1)

    '''Metoda do generowania pojedyńczego kontenera
        Method to generate singleContainer
    '''
    def saveToNamesTab(self,widget,entry,who):

        self.names_tab[who] = entry.get_text()
        #print self.names_tab[who] + " " + str(who)
        print "--------------------------------------------ENTER-----------------------------------------"
        print entry
        print who
        print self.names_tab


    def generateSingleContainer(self,x,y,dev):

        self.microContainers[x][y] = gtk.VBox(gtk.FALSE,self.devices+1)
        self.chkbx = {}
        entry = gtk.Entry()
        print "------------------------------ENTER CREATE---------------------------------------"
        print entry
        print dev
        print "------------------------------END CREATE------------------------------------------r"
        entry.set_text(self.names_tab[self.nevermind])
        entry.connect("activate",self.saveToNamesTab,entry,self.nevermind)
        self.nevermind+=1
        entry.show()
        self.microContainers[x][y].show()

        for i in range(0,self.devices):
            self.chkbx[i] = gtk.CheckButton("LED"+str(i+1))
            '''connect "toggled" to every chkbtn'''
            self.chkbx[i].connect("toggled",self.changeBody_tabStatus,(self.startScene-1),dev,i)
            self.chkbtn_tab[dev][i] = self.chkbx[i]
            self.chkbx[i].show()

        self.microContainers[x][y].pack_start(entry,False,False,0)
        for i in range(0,self.devices):
            self.microContainers[x][y].pack_start(self.chkbx[i],False,False,0)
    '''Pasek menu
        Menubar
    '''
    '''Change body_tab information while checkbutton is toggled'''
    def changeBody_tabStatus(self,widget,scene,device,led):
        if  widget.get_active():
            self.body_tab[self.startScene-1][device][led] = 1
            print self.canILive
            if(self.canILive==True):
                self.serial.serial.SerialSend(`device+2` + "." + `1` + "." + `led+1` + "." + `0` + ".")
                print(`device+2` + "." + `1` + "." + `led+1` + "." + `0` + ".")
        else:
            self.body_tab[self.startScene-1][device][led] = 0
            if (self.canILive == True):
                self.serial.serial.SerialSend(`device+2` + "." + `0` + "." + `led+1` + "." + `0` + ".")
                print(`device+2` + "." + `0` + "." + `led+1` + "." + `0` + ".")
        print self.body_tab
    '''Change status of CheckButtons using body_tab'''
    def changeChkbtnActive(self,scene):
        for i in range(self.head_tab[1]):
            for j in range(self.head_tab[2]):
                if self.body_tab[scene-1][i][j] == 1:
                    self.chkbtn_tab[i][j].set_active(True)
                else:
                    print self.chkbtn_tab
                    self.chkbtn_tab[i][j].set_active(False)

    def key_file_switch(self,x):
        return{
            "<Control>N": self.fileMenuitem[0],
            "<Control>O": self.fileMenuitem[1],
            "<Control>S": self.fileMenuitem[2],
            "<Control>E": self.fileMenuitem[3],
        }.get(x,x)
    def reactToKeyBoard(self,Widget,event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        print keyname
    def menuTool(self):
        self.fileMenusub = gtk.Menu()

        agr = gtk.AccelGroup()
        self.fileMenuitem = {}
        # self.fileMenuitem[0] = gtk.MenuItem("Nowy")
        self.fileMenuitem[0] = gtk.ImageMenuItem(gtk.STOCK_NEW, agr)
        key, mod = gtk.accelerator_parse("<Control>N")

        agr.connect_group(key,mod,gtk.ACCEL_VISIBLE, self.fileInterpret)

        self.fileMenuitem[0].add_accelerator("activate", agr, key,
                                             mod, gtk.ACCEL_VISIBLE)
        # self.fileMenuitem[1] = gtk.MenuItem("Otworz")
        self.fileMenuitem[1] = gtk.ImageMenuItem(gtk.STOCK_OPEN, agr)
        key, mod = gtk.accelerator_parse("<Control>O")
        self.fileMenuitem[1].add_accelerator("activate", agr, key,
                              mod, gtk.ACCEL_VISIBLE)
        # self.fileMenuitem[2] = gtk.MenuItem("Zapisz")
        self.fileMenuitem[2] =gtk.ImageMenuItem(gtk.STOCK_SAVE, agr)
        key, mod = gtk.accelerator_parse("<Control>S")
        self.fileMenuitem[2].add_accelerator("activate", agr, key,
                              mod, gtk.ACCEL_VISIBLE)
        # self.fileMenuitem[3] = gtk.MenuItem("Zamknij")
        self.fileMenuitem[3] = gtk.ImageMenuItem(gtk.STOCK_CLOSE, agr)
        key, mod = gtk.accelerator_parse("<Control>E")
        self.fileMenuitem[3].add_accelerator("activate", agr, key,
                                             mod, gtk.ACCEL_VISIBLE)

        self.deviceMenusub = gtk.Menu()
        self.deviceMenuItem = {}
        self.deviceMenuItem[0] = gtk.MenuItem("Wybierz urządzenie")
        self.deviceMenusub.append(self.deviceMenuItem[0])


        self.fileMenuitem[0].connect("activate", self.fileInterpret, 'new')
        self.fileMenuitem[1].connect("activate", self.fileInterpret, 'open')
        self.fileMenuitem[2].connect("activate", self.fileInterpret, 'save')
        self.fileMenuitem[3].connect("activate", gtk.main_quit)

        self.deviceMenuItem[0].connect("activate", self.setDevice)

        self.deviceMenu = gtk.MenuItem("Narzędzia")
        self.fileMenu = gtk.MenuItem("Plik")


        self.fileMenu.set_submenu(self.fileMenusub)
        self.deviceMenu.set_submenu(self.deviceMenusub)

        self.menu_bar = gtk.MenuBar()

        self.menu_bar.append(self.fileMenu)
        self.menu_bar.append(self.deviceMenu)

        self.fileMenu.show()
        self.fileMenusub.show()
        self.menu_bar.show()
        for i in range(0, len(self.fileMenuitem)):
            self.fileMenusub.append(self.fileMenuitem[i])
            self.fileMenuitem[i].show()
        self.deviceMenu.show()
        self.deviceMenusub.show()
        self.deviceMenuItem[0].show()



        return self.menu_bar
    #Method to set device with setDevice.serialWindow


    def setDevice(self,data):
        """
        :param data: Will import setDevice to set value on self.serial
        :return: nothing
        """
        self.serial = setDevice.serialWindow()
        self.serial.WALSIENARYJ__init__()
        print serial
        if(self.serial.chk_Activate == 1):
            self.serial.serial.SerialActivate(self.serial.getCombobox().get_active(),False)

    def fileInterpret(self,widget,option):
    # Main method to run all other methods responsible for files
    # Open and get file object
            if(option!='new'):
                self.File = self.fileOpen_Choose_Save(widget, option)
                if self.File != None:
                    print self.File
                    '''We will open file'''
                    if option == 'open':
                        '''Read all content'''
                        head = pickle.load(self.File['read'])
                        meta = pickle.load(self.File['read'])
                        names= pickle.load(self.File['read'])
                        body = pickle.load(self.File['read'])
                        '''Head = [number_of_scenes, colums_main,devices]'''
                        print head
                        print "Leci name"
                        print names
                        print body
                        '''Send it to fileParserOpen method which will interpret it'''
                        g = generateScene(colums_main=head[1],
                                          devices=head[2],
                                          number_of_scenes=head[0],
                                          body=body,
                                          meta=meta,
                                          names=names)
                        # self.napis = [[0 for x in range(self.checkInput(, ))] for y in
                        #               range()]
                        self.File['read'].close()
                    if option == 'save':
                        #saving all tables to file
                        pickle.dump(self.head_tab,self.File['save'])
                        pickle.dump(self.meta_tab,self.File['save'])
                        pickle.dump(self.names_tab,self.File['save'])
                        pickle.dump(self.body_tab,self.File['save'])
                        self.File['save'].close()
            if option == 'new':
                '''Still working..'''
                t1=Thread(name="New",target=self.threadNew())
                t1.daemon = True

                t1.start()
                t1.join()
    def threadNew(self):
        self.n = newWindowToGenerateScene.newWindowToGenerateScene(self.serial,self.window)
    #     t2 = Thread(target=self.loopNew)
    #     t2.daemon = True
    #     t2.start()
    #     t2.join()
    # def loopNew(self):
    #     while (True):
    #         time.sleep(1)
    #         print self.n.state
    #         if (self.n.state == True):
    #             return self.adj
    #         else:
    #             pass
# '''Close file at the end'''
# """
# import pickle
# text = open("lel.bin","wb")
# tab = [123,"32",'v',10.3]
# tab2 = [[0 for x in range(5)] for y in range(5)]
# tab2[0][0] = 1
# print tab2
# tab4 = [[]]
#
# i = 3
# #pickle.dump(tab,text)
# pickle.dump(tab2,text)
# tab3 =[[0 for x in range(5)]for y in range(5)]
# text.close()
# text = open("lel.bin","rb")
# tab3 = pickle.load(text)
# print "Unpickled"
# print tab3
#
#
# text.close()"""
    def fileOpen_Choose_Save(self,widget,option):
        '''Main method which open file in two other way. One is read-write other is append.
         It also set up action for dialog buttons'''
        chooser = self.switch_choose(option)
        response = chooser.run()
        self.file = {}
        if response == gtk.RESPONSE_OK:
            if(option == 'open'):
                name = chooser.get_filename()
                self.file['read'] = self.fileOpen(name,"rw")
            if(option == 'save'):
                name = chooser.get_filename()+".hsk"
                self.file['save'] = self.fileOpen(name,"w")
            # if(option == 'new'):
            #     self.file = chooser.get_filename()
            chooser.destroy()
            return self.file
        if response == gtk.RESPONSE_CANCEL:
            chooser.destroy()
            return None
        chooser.destroy()
        return 0
    def fileOpen(self, file,mode):
        return open(file,mode)
    def switch_choose(self,x):
        '''Switch to decide which dialog is suppose to call'''
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

    '''
    Function to add scene. It will add 1 more x value to body_tab
    '''
    def addScene(self,data):
        if(self.head_tab[0]!=0):
            print self.body_tab
            scenes = self.head_tab[0]
            scenes += 1
            self.head_tab[0] = scenes
            print scenes
            #creating new tabs
            body_tab_new = [[[0 for l in range(self.head_tab[2])]
                            for d in range(self.head_tab[1])]
                            for s in range(scenes)]
            meta_tab_new = [[0 for i in range(4)]
                            for l in range(self.head_tab[0])]

            #coping value from body to new tab
            for x in range(self.head_tab[0]-1):
                for y in range(self.head_tab[1]):
                    for z in range(self.head_tab[2]):
                        body_tab_new[x][y][z] = self.body_tab[x][y][z]
            #coping value from meta to new tab
            for x in range(self.head_tab[0]-1):
                for y in range(4):
                    meta_tab_new[x][y] = self.meta_tab[x][y]
            #Setting old tabs as new
            self.body_tab = body_tab_new
            self.meta_tab = meta_tab_new
            print self.body_tab
            self.changeSceneOnBottom(self.startScene,self.head_tab[0])

            #self.head_tab = [number_of_scenes, colums_main,devices]
    '''
    Function to del scene. Will remove 1 x from body_tab
    '''
    def delScene(self,data):
        if(self.head_tab[0]!=1 and self.head_tab[0]!=0):
            self.head_tab[0] -= 1
        #     print self.body_tab
        #     scenes = self.head_tab[0]
        #     scenes -= 1
        #     self.head_tab[0] = scenes
        #     print scenes
        #     body_tab_new = [[[0 for l in range(self.head_tab[2])]for d in range(self.head_tab[1])]for s in range(scenes)]
        #
        #     for x in range(self.startScene-1):
        #         print "X"
        #         print x
        #         for y in range(self.head_tab[1]):
        #             for z in range(self.head_tab[2]):
        #                 body_tab_new[x][y][z] = self.body_tab[x][y][z]
        #     difference = self.head_tab[0] - self.startScene
        #     if (difference != 0):
        #         for x in range(difference):
        #             print "X"
        #             print x+self.startScene
        #             for y in range(self.head_tab[1]):
        #                 for z in range(self.head_tab[2]):
        #                     body_tab_new[x+self.startScene-1][y][z] = self.body_tab[x+self.startScene][y][z]
        #     self.body_tab = body_tab_new
            self.body_tab.pop(self.startScene-1)
            self.meta_tab.pop(self.startScene-1)
            print self.body_tab
            if(self.startScene>self.head_tab[0]):
                self.startScene -=1
                self.changeSceneOnBottom(self.startScene, self.head_tab[0])
                self.changeChkbtnActive(self.startScene)
            else:
                self.changeSceneOnBottom(self.startScene, self.head_tab[0])
                self.changeChkbtnActive(self.startScene)

    '''
    Activate live mode. First check if serial is connected, if not program force select device
    '''
    def liveModeActive(self,data):
        if (data.get_active()):
            print self.serial
            if(self.serial != None):
                self.canILive = True
            elif(self.serial==None):
                self.setDevice(None)
                self.canILive = True
        if (data.get_active()!=True):
            self.serial = None
    def MainBottom(self):
        '''Bottom buttons'''
        self.container = gtk.HBox(gtk.FALSE,4)
        self.btnsWithoutEdit = {}
        '''Generate 6 objects for the first page'''
        self.btnsWithoutEdit["label"] = self.btnsWithoutEdit[0] = gtk.Label("-/-")
        self.btnsWithoutEdit["liveMode"] = self.btnsWithoutEdit[1] = gtk.CheckButton("Live Mode")
        self.btnsWithoutEdit["addScene"] = self.btnsWithoutEdit[2] = gtk.Button("Dodaj scenę")
        self.btnsWithoutEdit["delScene"] = self.btnsWithoutEdit[3] = gtk.Button("Usuń scenę")
        self.btnsWithoutEdit["leftbt"] = self.btnsWithoutEdit[4] = gtk.Button("<")
        self.btnsWithoutEdit["rightbt"] = self.btnsWithoutEdit[5] = gtk.Button(">")

        self.btnsWithoutEdit["rightbt"].connect("clicked", self.bottomArrowRight)
        self.btnsWithoutEdit["leftbt"].connect("clicked", self.bottomArrowLeft)
        self.btnsWithoutEdit["liveMode"].connect("toggled",self.liveModeActive)
        self.btnsWithoutEdit["addScene"].connect("clicked", self.addScene)
        self.btnsWithoutEdit["delScene"].connect("clicked", self.delScene)

        '''Add it to the container'''
        for i in range(0,6):
            self.btnsWithoutEdit[i].show()
            if(i!=1):
                self.container.pack_start(self.btnsWithoutEdit[i], False, False, 0)
            else:
                self.container.pack_start(self.btnsWithoutEdit[i], True, True, 0)

        self.btnsWithoutEdit["addScene"].set_size_request(-1, -1)
        self.btnsWithoutEdit["delScene"].set_size_request(-1, -1)
        self.btnsWithoutEdit["liveMode"].set_size_request(-1, -1)
        self.btnsWithoutEdit["label"].set_size_request(50, -1)
        self.btnsWithoutEdit["leftbt"].set_size_request(40, -1)
        self.btnsWithoutEdit["rightbt"].set_size_request(40, -1)

        self.container.show()

        '''set label on start'''

        self.changeSceneOnBottom(self.startScene,self.head_tab[0])
        return self.container
    '''react to right arrow on bottom'''
    def bottomArrowRight(self,widget):
        if(self.startScene==0):
            return 0
        if(self.startScene==self.head_tab[0]):
            self.startScene = 1
            self.changeSceneOnBottom(self.startScene, self.head_tab[0])
            self.changeChkbtnActive(self.startScene)
            return 0
        self.startScene +=1
        '''change label on bottom'''
        self.changeSceneOnBottom(self.startScene,self.head_tab[0])
        '''change status of all chkbtn's'''
        self.changeChkbtnActive(self.startScene)
    '''react to left arrow on bottom'''
    def bottomArrowLeft(self, widget):
        if (self.startScene == 0):
            return 0
        if (self.startScene == 1):
            self.startScene = self.head_tab[0]
            self.changeSceneOnBottom(self.startScene, self.head_tab[0])
            self.changeChkbtnActive(self.startScene)
            return 0
        self.startScene -= 1
        '''change label on bottom'''
        self.changeSceneOnBottom(self.startScene, self.head_tab[0])
        '''change status of all chkbtn's'''
        self.changeChkbtnActive(self.startScene)
def main(a,b,c,d = None):
    g = generateScene(a, b, c,serial = d)
    gtk.main()
if __name__ == "__main__":
    '''Runnig with 5,5,2 for example - can be run with nothing'''
    g = generateScene()
    gtk.main()