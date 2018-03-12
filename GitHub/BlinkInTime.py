import gtk
class blinkInTime():
    def __init__(self,zmienna):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("elSter - blinkInTime")
        self.window.connect('destroy', gtk.main_quit)
        self.window.connect('delete-event', gtk.main_quit)
        # self.window.connect('close',gtk.main_quit)
        self.window.set_border_width(10)
        self.container = gtk.HBox(gtk.FALSE, zmienna)
        self.window.add(self.container)
        self.vBox = {}
        self.startBT = {}
        self.HzAdjustment = {}
        self.Spinbutton = {}
        for num in range(1, zmienna + 1):
            self.vBox[num] = gtk.VBox(gtk.FALSE, zmienna)
            self.startBT[num] = gtk.ToggleButton("Start")
            self.HzAdjustment[num] = gtk.Adjustment(1, 1, 60, 1)
            self.Spinbutton[num] = gtk.SpinButton(self.HzAdjustment[num], 0, 0)

            self.container.add(self.vBox[num])
            self.vBox[num].show()

            self.vBox[num].add(self.Spinbutton[num])
            self.vBox[num].add(self.startBT[num])

            self.Spinbutton[num].show()
            self.startBT[num].show()
        self.container.show()
        self.window.show()

