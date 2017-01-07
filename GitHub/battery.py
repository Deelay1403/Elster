import pygtk
pygtk.require('2.0')
import gtk

class batteryWindow:

	def __init__(self, port, howManyInRow=3, buttonFunction=False, maxLevel=1024, maxBar=6):
		self.port = port
		self.buttonFunction = buttonFunction
		self.howManyInRow = howManyInRow
		self.maxLevel = maxLevel
		self.maxBar = maxBar

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("elSter - battery mannager")
		self.window.set_border_width(10)
    
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)

		self.glownyVKontener = gtk.VBox(gtk.FALSE, 10)
		self.glownyVKontener.show()
		self.window.add(self.glownyVKontener)
		self.kontenerH3 = {}
		self.podkontenerH = {}
		self.battery = {}
		self.battery_icon = {}
		if self.buttonFunction: self.battery_button = {}
		self.battery_ID_label = {}
		self.battery_poziom_label = {}
		self.addresses = {}
		self.howMany = 0
		self.level = {}
		self.level_old = {}

	def __call__(self):
		self.show()

	def add(self, ID, name):
		if self.port == "NO_PORTS":
			print "I:------------ batterry.py BRAK PORTOW NA STATKII!"

		if ID not in self.addresses:
			self.addresses[ID] = self.howMany
		else:
			print "E:------- ERROR THE SAME ID (" + str(ID) + ") IN LIST FOR " + str(self.addresses[ID]) + "! (cloudn't add '" + str(name) + "')"
			return

		if not self.howMany%self.howManyInRow:
			self.obecne_ID_kontenera = self.howMany
			self.podkontenerH[self.addresses[ID]] = gtk.HBox(gtk.FALSE, 10)
			self.podkontenerH[self.addresses[ID]].show()
			self.glownyVKontener.add(self.podkontenerH[self.addresses[ID]])

		
		self.battery[self.addresses[ID]] = gtk.VBox(gtk.FALSE, 10)

		self.battery_icon[self.addresses[ID]] = gtk.Image()
		self.obraz = "./img/battW" + str(6) + ".png"
		self.battery_icon[self.addresses[ID]].set_from_file(self.obraz)
		self.battery_icon[self.addresses[ID]].show()

		if self.buttonFunction:
			self.battery_button[self.addresses[ID]] = gtk.Button()
			self.battery_button[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
			self.battery_button[self.addresses[ID]].connect("clicked", self.update, ID)
			self.battery_button[self.addresses[ID]].show()

		self.battery_ID_label[self.addresses[ID]] = gtk.Label("Bateria " + str(name))
		self.battery_ID_label[self.addresses[ID]].show()
		self.battery_poziom_label[self.addresses[ID]] = gtk.Label("100%")
		self.battery_poziom_label[self.addresses[ID]].show()

		if self.buttonFunction: 
			self.battery[self.addresses[ID]].add(self.battery_button[self.addresses[ID]])
		else:
			self.battery[self.addresses[ID]].add(self.battery_icon[self.addresses[ID]])
		self.battery[self.addresses[ID]].add(self.battery_ID_label[self.addresses[ID]])
		self.battery[self.addresses[ID]].add(self.battery_poziom_label[self.addresses[ID]])

		self.battery[self.addresses[ID]].show()
		self.podkontenerH[self.obecne_ID_kontenera].add(self.battery[self.addresses[ID]])
		self.howMany = self.howMany + 1


		self.level[self.addresses[ID]] = 0


		# print self.howMany
		# print self.obecne_ID_kontenera
		# print ID
		# print name
		# print self.addresses

	def delete_event(self, widget, event, data=None):
		# If you return FALSE in the "delete_event" signal handler,
		# GTK will emit the "destroy" signal. Returning TRUE means
		# you don't want the window to be destroyed.
		# This is useful for popping up 'are you sure you want to quit?'
		# type dialogs.
		print "delete event occurred"

		# Change FALSE to TRUE and the main window will not be destroyed
		# with a "delete_event".
		return False

	def destroy(self, widget, data=None):
		print "destroy signal occurred"
		gtk.main_quit()

	def info(self, ID):
		# a horizontal box to hold the battery_buttons
	

		# create several images with data from files and load images into
		# battery_buttons
		if ID == 0:
			self.ID_OLD = 6
		else:
			self.ID_OLD = 6

		self.ID_OLD = ID
		self.image = gtk.Image()
		self.update(1, ID)
		self.image.show()
		# a battery_button to contain the image widget
		self.button = gtk.button()
		self.button.add(self.image)
		self.button.show()
		self.hbox.pack_start(self.button)
		self.button.connect("clicked", self.update, ID)
		pass

	def updateOLD(self, widget, ID):
		if self.level[self.addresses[ID]] == 0:
			self.level[self.addresses[ID]] = 6
		self.level_old[self.addresses[ID]] = self.level[self.addresses[ID]] - 1
		self.level[self.addresses[ID]] = self.level_old[self.addresses[ID]]
		obraz = "./img/battW" + str(self.level[self.addresses[ID]]) + ".png"
		self.battery_icon[self.addresses[ID]].set_from_file(obraz)
		pass


	def update(self, ID, level, maxLevel=None, maxBar=None):
		if maxLevel == None:
			maxLevel = self.maxLevel
		if maxBar == None:
			maxBar = self.maxBar

		ileBelek = 0;
		while ileBelek <= maxBar:
			procentLvl = self.obliczProcent(level, maxLevel)
			procentBelka = self.obliczProcent(ileBelek, maxBar)
			if (procentLvl >= procentBelka) & (procentLvl <= self.obliczProcent(ileBelek+1, maxBar)):
				print "BELKI: " + str(procentLvl) + " " + str(ileBelek)
				obraz = "./img/battW" + str(ileBelek) + ".png"

				self.battery_poziom_label[self.addresses[ID]].set_text(str(procentLvl) + "%")
				self.battery_icon[self.addresses[ID]].set_from_file(obraz)
				return
			ileBelek = ileBelek + 1
			print ""
		pass

	def obliczProcent(self, level, maxLevel):
		return round(((100*float(level))/maxLevel), 1)
		pass

	def changeName(self, ID, name):
		self.battery_ID_label[self.addresses[ID]].set_text("Bateria " + str(name))
		pass

	def show(self):
		#self.pokaz()
		self.window.show()
 		gtk.main()
		pass

if __name__ == "__main__":

	bateriAa = batteryWindow('COM1', 3, True, 1024, 6)
	bateriAa.add(5,"pioruny")
	bateriAa.update(5, 555)
	bateriAa.changeName(5, "chuuuj")
	bateriAa.show()
	