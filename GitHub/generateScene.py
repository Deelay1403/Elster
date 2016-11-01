import gtk

class generateScene():
    def __init__(self, colums_main, devices):


        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy",gtk.main_quit)
        self.main_window_col = gtk.VBox(gtk.FALSE,3)
        self.window.add(self.main_window_col)
        #self.line_window_bottom = gtk.HBox(gtk.FALSE,4)
        self.table = gtk.Table(devices, colums_main, True)

        self.main_window_col.pack_start(self.MenuTool(),False,False,0)

        self.napis = [[1 for x in range(devices)] for y in range(colums_main)]
        for x in range(0,colums_main):
            for y in range(0, devices):
                self.napis[x][y] = gtk.Button("Test")
                self.napis[x][y].show()

        for x in range(0,colums_main):
            for y in range(0, devices):
                self.table.attach(self.napis[x][y],x,x+1,y,y+1)
        self.table.show()
        self.main_window_col.pack_start(self.table,True,True,0)

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

    def checkInput(self, number,column):
        if(number%column==0):
            return (number/column)
        else:
            return ((number/column)+1)
    # def checkInput(self,number):
    #     tableXY = {}
    #     tableXY['x'] = 0
    #     tableXY['y'] = 0
    #     while(number!=0):
    #         if(number<5):
    #             if(tableXY['y']==0&tableXY['x']==0):
    #                 tableXY['x'] = 5
    #                 tableXY['y'] = 1
    #             return tableXY
    #             number=0
    #         elif(number>5):
    #             number-=5
    #             if(tableXY['y']!=2):
    #                 ++tableXY['y']
    #                 tableXY['x'] = number
    #             else:
    #                 tableXY['y']=2
    #                 tableXY['x']=number
    #         elif(number>20):
    #             number-=20
    #             if((tableXY['y']!=2)&(tableXY['x']==0)):
    #                 tableXY['x']=10
    #                 ++tableXY['y']
    #             elif(tableXY['y']!=2&tableXY['x']>0):
    #                 if((tableXY['x']+number)<10):
    #                     tableXY['x']+=number
    #                     ++tableXY['y']
    #                 else:
    #                     tableXY['x']=(10-(tableXY['x']+number))
    #                     ++tableXY['y']




    def MenuTool(self):
        self.menu = gtk.Menu()
        self.firstMenuitem = {}
        self.firstMenuitem[0] = gtk.MenuItem("Nowy")
        self.firstMenuitem[1] = gtk.MenuItem("Otworz")
        self.firstMenuitem[2] = gtk.MenuItem("Zapisz")
        self.firstMenuitem[3] = gtk.MenuItem("Zamknij")
        for i in range(0,len(self.firstMenuitem)):
            self.menu.append(self.firstMenuitem[i])
            self.firstMenuitem[i].show()


        self.root = gtk.MenuItem("Plik")

        self.root.show()
        self.root.set_submenu(self.menu)
        self.menu_bar = gtk.MenuBar()
        self.menu_bar.show()
        self.menu_bar.append(self.root)

        self.menu.show()

        return self.menu_bar

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

        self.container
        self.container.show()
        return self.container

if __name__ == "__main__":
    g = generateScene(5,5)
    print g.checkInput(6,5)
    gtk.main()


