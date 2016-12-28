import gtk
class newWindowToGenerateScene:
    def __init__(self):
        self.window = gtk.Dialog("New Generate",
                                 None,
                                 gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                                 (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_APPLY,gtk.RESPONSE_ACCEPT))
        self.vbox = gtk.VBox(False,3)
        self.window.add(self.vbox)

        self.adj = [ gtk.Adjustment(1,1,100000,1)
                    ,gtk.Adjustment(1,1,100000,1)
                    ,gtk.Adjustment(1,1,100000,1)]
        #
        # self.scene = gtk.SpinButton(self.adj[0],0,0)
        # self.devices = gtk.SpinButton(self.adj[1],0,0)
        # self.led = gtk.SpinButton(self.adj[2],0,0)


        self.SPBtn = [   gtk.SpinButton(self.adj[0],0,0)
                        ,gtk.SpinButton(self.adj[1],0,0)
                        ,gtk.SpinButton(self.adj[2],0,0)]

        for i in range(2):
            self.SPBtn[i].show()
            self.vbox.pack_start(self.SPBtn[i], False, True)

        self.vbox.show()
        self.window.show()

n = newWindowToGenerateScene()
gtk.main()