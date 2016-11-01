import gtk


# TODO: 1.Make changebutton responsible to call -> Throw it to the table
# TODO: 2.Create method to read/write file and generate window
# TODO: 3.Make it look better
# TODO: 4.Drink coffee - You deserve :)
# TODO: 5.Talk with Popcorator
class generateScene():
    def __init__(self, colums_main, devices):
        horizontalValue = 5
        self.microContainers = [[0 for x in range(self.checkInput(colums_main, horizontalValue))] for y in
                                range(horizontalValue)]
        self.devices = devices

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy",gtk.main_quit)
        self.main_window_col = gtk.VBox(gtk.FALSE,3)
        self.window.add(self.main_window_col)
        #self.line_window_bottom = gtk.HBox(gtk.FALSE,4)
        self.table = gtk.Table(self.checkInput(colums_main,horizontalValue), horizontalValue, True)
        self.main_window_col.pack_start(self.menuTool(),False,False,0)

        self.napis = [[0 for x in range(self.checkInput(colums_main, horizontalValue))] for y in range(colums_main)]
        for x in range(0,colums_main):
            for y in range(0, self.checkInput(colums_main,horizontalValue)):
                self.napis[x][y] = gtk.Button("Test")
                self.napis[x][y].show()

        for x in range(0,self.checkInput(colums_main,horizontalValue)):
            print str(x) + " " + str(colums_main)
            if(colums_main>5):
                for y in range(0, horizontalValue):
                    self.generateSingleContainer(y, x)
                    self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)
                    colums_main-=1
            elif (colums_main <= 5):
                for y in range(0, colums_main):
                    self.generateSingleContainer(y, x)
                    self.table.attach(self.microContainers[y][x], y, y + 1, x, x + 1)


        # for x in range(0,colums_main):
        #     for y in range(0, self.checkInput(colums_main,horizontalValue)):
        #         self.generateSingleContainer(x, y)
        #         self.table.attach(self.microContainers[x][y],x,x+1,y,y+1)
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

        self.firstMenuitem[3].connect("activate", gtk.main_quit)
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

        self.container.show()
        return self.container

if __name__ == "__main__":
    g = generateScene(5, 2)
    gtk.main()


