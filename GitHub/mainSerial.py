#import ConfigWindow
import serial
import sys
import glob
import time
class serialComunnication():
    '''__init__() Funkcja wyszukuje urzadzenie podpiete pod port szeregowy zaleznie od wersji systemu'''
    def __init__(self):
        # print "WYSZUKUJEE"
        # Windows
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        # Linux
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        # Mac OS X
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        self.portsOpen = []
        for port in ports:
            try:
                # Trying if ports are open
                s = serial.Serial(port, 115200, timeout=0.5)
                print port
                print s
                time.sleep(2) #TODO zastanowic sie czy 2 sekundy to nie za duzo (czas boot dla arduino)8
                s.write("99,8") #PING
                print "zapisano"
                line = s.read_until(';')
                print "LECI LINE"
                print line
                print "odczytano"
                line = line.strip("\r\n")
                #self.portsOpen.append(port)
                print line
                if line.startswith('ACK_OK'): # akceptujemy tylko nasze urzadzenia, a nie jakies modemy xD
                    s.close()
                    self.portsOpen.append(port)
                    print "MAMY TO!"
            # if OS is diferent it pass program without connect serial
            except (OSError, serial.SerialException):
                pass
        x = 1
        print "PORTS OPEN"
        print self.portsOpen

        # Prawdopodobine wypisuje nazwy portow szeregowych
        for situation in self.portsOpen:
            print str(x) + ": " + situation
            x += 1

        self.serialIndex = -1 # jako brak wyboru / 28.01.2018 kiedy to sie dzieje?
        self.portOpen = False

    '''Funkcja jezeli moze otwiera port przypisuje jako obiejt do self.ser'''
    # w pewnej z funckji jako argument dial jest podany index, czyli pozycja wybranego portu szeregowego z listy
    def SerialActivate(self, dial, mode):
        print "SERIAL active"
        print "DIAL"
        print dial
        print "MODE"
        print mode
        print self.portsOpen
        print "END"


        #TODO poznac co robi MODE i co to DIAL
        #dial - wartosc z listy z portami szeregowymi
        if not self.portsOpen:
            print "BRAK PORTOW NA STATKI"
            self.ser = "NO_PORTS"
            print self.ser
            #dial = ConfigWindow.serialWindow()
        else: #  jezeli jakis port jest
            if mode: #domyslam sie ze mode jest powiazany z oknem podczas generatora scen
                #dial = ConfigWindow.serialWindow()
                whichIndex = dial.getIndex()
                print "FUUUUUUUUUUUCK!"
            else:
                whichIndex = dial

            if whichIndex > -1:
                print whichIndex
                print self.portsOpen[whichIndex]
                print "KURWA"
                if not self.portOpen:
                    self.ser = serial.Serial(self.portsOpen[whichIndex], 115200, timeout=5)
                    self.portOpen = True
                    from time import sleep
                    sleep(2) #czas po ktorym arduino sie ogarnia, mozna temu zapobiec wylaczajac bootloader
                else:
                    print "port byl otwarty"
                print "MAM TO"
            else: # dzieje sie wtedy gdy zaden port nie zostanie wybrany
                print "BRAK PORTOW NA STATKII"
                self.ser = "NO_PORTS"
                print self.ser
                print "GDZIE SA STATKI"

    '''Funkcja zamyka (?) port szeregowy'''
    def SerialClose(self):
        self.portOpen = False
        self.portsOpen = []
        self.ser = ""
        pass

    '''Funkcja zwraca liste portow szeregowych, pusta - gdy brak'''
    def GetAvailablePorts(self):
        return self.portsOpen
        pass

    '''Funkcja zwraca obiekt portu szeregowego i NO_PORTS gdy portu brak'''
    def GetOpenPort(self):
        return self.ser
        # pass

    #TODO poznac co robi ta funkcja
    def SetSerialIndex(self, index):
        self.serialIndex = index
        pass

    '''Funkcja wysyla dane na port szeregowy, jezeli jest otwraty, jezeli nie EMULATING'''
    #w przypadku bledu wypisuje Blad zapisu i zwraca ERR01
    def SerialSend(self, whatSend):
        if not self.ser == 'NO_PORTS':
            try:
                self.ser.write(whatSend)
                print whatSend
            except serial.serialutil.SerialException:
                print 'Blad zapisu'
                return "ERR01"
        else:
            print('EMULATING')
            #TODO: SIMULATING SCENES
        pass

    '''Zwraca dane z portu szeregowego do tego co jest podane jako what'''
    def ReadUntil(self, what):
        try:
            return self.ser.read_until(what)
        except serial.serialutil.SerialException:
            print 'Blad odczytu'
            return "ERR02"
        pass