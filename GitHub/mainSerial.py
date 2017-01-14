import ConfigWindow
import serial
import sys
import glob
import time
class serialComunnication():
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
                s = serial.Serial(port, timeout=0.5)
                print port
                time.sleep(1.5)
                s.write("99,8") #PING
                print "zapisano"
                line = s.read_until(';')
                print line
                print "odczytano"
                line = line.strip("\r\n")
                #self.portsOpen.append(port)
                print line
                if line.startswith('ACK_OK'): #akceptujemy tylko nasze urzadzenia, a nie jakies modemy xD
                    s.close()
                    self.portsOpen.append(port)
                    print "MAMY TO!"
            # if OS is diferent it pass program without connect serial
            except (OSError, serial.SerialException):
                pass
        x = 1
        print "PORTS OPEN"
        print self.portsOpen

        for situation in self.portsOpen:
            print str(x) + ": " + situation
            x += 1

        self.serialIndex = -1 #jako brak wyboru
        self.portOpen = False

    def SerialActivate(self, dial, mode):

        print "SERIAL active"
        print "DIAL"
        print dial
        print "MODE"
        print mode
        print self.portsOpen
        print "END"


        if not self.portsOpen:
            print "BRAK PORTOW NA STATKI"
            self.ser = "NO_PORTS"
            print self.ser
            #dial = ConfigWindow.serialWindow()
        else:
            if mode:
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
                    self.ser = serial.Serial(self.portsOpen[whichIndex], 9600, timeout=1)
                    self.portOpen = True
                else:
                    print "port byl otwarty"
                print "MAM TO"
            else:
                print "BRAK PORTOW NA STATKII"
                self.ser = "NO_PORTS"
                print self.ser
                print "GDZIE SA STATKI"

    def SerialClose(self):
        self.portOpen = False
        self.portsOpen = []
        self.ser = ""
        pass

    def GetAvailablePorts(self):
        return self.portsOpen
        pass

    def GetOpenPort(self):
        return self.ser
        # pass
    def SetSerialIndex(self, index):
        self.serialIndex = index
        pass

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

    def ReadUntil(self, what):
        try:
            return self.ser.read_until(what)
        except serial.serialutil.SerialException:
            print 'Blad odczytu'
            return "ERR02"
        pass