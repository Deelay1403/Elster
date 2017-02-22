from multiprocessing import Process, Queue
from time import sleep
import serial
import gtk

class interactiveSerial:
    def __init__(self, port):
        print "ROZPOCZETO"
        self.serPort = port
        self.queue = Queue()
        self.objects = {}
        print "inicjacja zakonczona"

    def stopListen(self):
        self.queue.put(['STOP_LISTENING', ''])

    def startListen(self, q, endLineChar = ';'):
        while True:
            try:
                daneOdebrane = q.get_nowait()
                if (daneOdebrane[0] == "STOP_LISTENING"):
                    print "STOP!"
                    break
            except Exception:
                daneOdebrane = "pusto"

            if (daneOdebrane[0] == 'SEND'):
                try:
                    #self.serPort.write(daneOdebrane[1])
                    print "WYSLANO " + daneOdebrane[1]
                except serial.serialutil.SerialException:
                    print 'Blad zapisu'
                    return "ERR01"

            try:
                print "ODBIERAM"
                #lineOfData = self.serPort.read_until(endLineChar)
                lineOfData = "BAT_4_517"
                print lineOfData
                lineOfData = lineOfData.strip("\r\n")
                print lineOfData

                if lineOfData.startswith('BAT_'):  # szuka odpowiedzniej komendy
                    raw = lineOfData.strip('BAT_;\n')  # "oczyszcza" ja
                    print 'komenda ' + raw
                    infoBattery = raw.split('_')
                    batteryObject = self.getObject('battery')
                    print "__________________________________"
                    print batteryObject
                    if (batteryObject != 'ERIS01' and batteryObject != 'ERIS02'):
                        print "TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUEEEEEEEEEEEE"
                        print "ID:" + infoBattery[0]
                        print "VAL:" + infoBattery[1]
                        # self.objects['battery'].update(4,699)
                        #testuje
                        self.updateBattery(4,100)
                        self.objects["battery"].update(5,300)
                        self.objects["bettery"].update(ID=2,level=300)



                        while gtk.events_pending():
                            gtk.main_iteration()
                        print "OK!"

                elif lineOfData.startswith('ER_'):
                    raw = lineOfData.strip('ER_;\n')  # "oczyszcza" ja
                    print 'komenda ' + raw
                    infoError = raw.split('_')
                    print "ERROR"
                    print  infoError

            except serial.serialutil.SerialException:
                print 'Blad odczytu'
                return "ERR02"
            pass

            print "co odbieram " + daneOdebrane[0] + " " + daneOdebrane[1]
            sleep(1)
            break

    def updateBattery(self, ID, LVL):
        self.objects['battery'].update(ID, LVL)

    def send(self, whatSend):
        if not self.serPort == 'NO_PORTS':
            self.queue.put(['SEND', whatSend])
        else:
            print('EMULATING')
            #TODO: SIMULATING SCENES
        pass

    def addObject(self, name, object):
        self.objects[name] = object
        # self.updateBattery(4,100)
        #print self.objects

    def getObject(self, name):
        try:
            if (self.objects[name]):
                return self.objects[name]
            else:
                return "ERIS01"
                print "brak obiektu dla " + name
        except KeyError:
            return "ERIS02"
            print "brak obiektu dla " + name
    def jebacTo(self, ID, LVL):
        self.updateBattery(ID, LVL)

    def start(self, endLineChar = ';'):
        print "START!"
        #p = Process(target=self.startListen, args=(self.queue, endLineChar,)).start()
        p = Process(target=self.jebacTo, args=(5,500,)).start()
        print "OKK!"


if __name__ == "__main__":
    popcorn = interactiveSerial('tty/=/1')
    popcorn.start()

    popcorn.addObject('bateria','tak')

    popcorn.getObject('bateria')

    sleep(5)
    popcorn.send("OK!")
    sleep(5)
    popcorn.send("NACHOS!")