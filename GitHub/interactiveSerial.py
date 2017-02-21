from multiprocessing import Process, Queue
from time import sleep
import serial

class interactiveSerial:
    def __init__(self, port):
        print "ROZPOCZETO"
        self.serPort = port
        self.queue = Queue()
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
                lineOfData = "BAT_4_1024"
                print lineOfData
                lineOfData = lineOfData.strip("\r\n")
                print lineOfData

                if lineOfData.startswith('BAT_'):  # szuka odpowiedzniej komendy
                    raw = lineOfData.strip('BAT_;\n')  # "oczyszcza" ja
                    print 'komenda ' + raw
                    infoBattery = raw.split('_')
                    print infoBattery
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

    def send(self, whatSend):
        if not self.serPort == 'NO_PORTS':
            self.queue.put(['SEND', whatSend])
        else:
            print('EMULATING')
            #TODO: SIMULATING SCENES
        pass

    def addObject(self, name, object):
        self.objects

    def start(self, endLineChar = ';'):
        print "START!"
        p = Process(target=self.startListen, args=(self.queue,endLineChar,)).start()
        print "OKK!"


if __name__ == "__main__":
    popcorn = interactiveSerial('tty/=/1')
    popcorn.start()
    sleep(5)
    popcorn.send("OK!")
    sleep(5)
    popcorn.send("NACHOS!")