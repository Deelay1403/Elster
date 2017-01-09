import ConfigWindow
import serial
import sys
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
                s.write("99,7") #PING
                print "zapisano"
                line = s.read_until(';')
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
                self.ser = serial.Serial(self.portsOpen[whichIndex], 9600)
            else:
                print "BRAK PORTOW NA STATKII"
                self.ser = "NO_PORTS"

    def GetAvailablePorts(self):
        return self.portsOpen
        pass

    def GetOpenPort(self):
        return self.ser
        pass

    def SerialSend(self, whatSend):
        if not ser == 'NO_PORTS':
            try:
                self.ser.write(`receiver` + "." + `state` + "." + `led` + "." + `option` + ".")
                raise 
            except serial.serialutil.SerialException:
                print 'Blad zapisu'
        else:
            print('EMULATING')
            #TODO: SIMULATING SCENES
        pass
