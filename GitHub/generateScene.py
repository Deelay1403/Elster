import gtk

class generateScene():
    def __init__(self,colums_main,line_main):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy",gtk.main_quit)
        self.main_window_col = gtk.VBox(gtk.FALSE,3)
        self.window.add(self.main_window_col)
        self.line_window_bottom = gtk.HBox(gtk.FALSE,4)
        self.menu = gtk.MenuItem()
        self.main_window_col.add(self.menu)
        self.x_Box = gtk.HBox(gtk.FALSE,line_main)
        self.y_Box = {}
        for x in range(0,3):
            self.y_Box[x] = gtk.VBox(gtk.FALSE, colums_main)

        self.napis = [[1 for x in range(3)] for y in range(3)]
        for x in range(0,3):
            for y in range(0,3):
                self.napis[x][y] = gtk.Label("Test")
                self.napis[x][y].show()

        self.main_window_col.add(self.x_Box)

        for num in range(0,3):
            self.x_Box.add(self.y_Box[num])
            self.y_Box[num].show()
            for i in range(0,3):
                self.y_Box[num].add(self.napis[num][i])
          #  for i in range(0,3):
           #     self.y_Box[num].add(self.napis)

        self.main_window_col.add(self.MainBottom())

        self.window.show()
        self.main_window_col.show()
        self.line_window_bottom.show()
        self.menu.show()
        self.x_Box.show()

    def MainBottom(self):
        self.container = gtk.HBox(gtk.FALSE,4)
        self.obj = {}

        self.obj["label"] = self.obj[0] = gtk.Label("-/-")
        self.obj["edit"] = self.obj[1] = gtk.Button("Edytuj")
        self.obj["leftbt"] = self.obj[2] = gtk.Button("<")
        self.obj["rightbt"] = self.obj[3] = gtk.Button(">")

        for i in range(0,4):
            self.obj[i].show()
            self.container.add(self.obj[i])

        self.container
        self.container.show()
        return self.container

if __name__ == "__main__":
    g = generateScene(3,3)
    gtk.main()


