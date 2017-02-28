from multiprocessing import Process, Queue
from time import sleep
import interactiveSerial_nauka as inSer

class interactiveSerial:
    def __init__(self):
        print "ROZPOCZETO"
        self.queue = Queue()
        print "inicjacja zakonczona"

    def startLoop(self,q):
        while True:
            try:
                daneOdebrane = q.get_nowait()
                if daneOdebrane[0] == "POP":
                    print ":P"
            except Exception:
                daneOdebrane = "pusto"

            print "co odbieram " + daneOdebrane[1]
            if (daneOdebrane == "START"):
                print "OK"
            else:
                print "!OK"

            print ";_;"

            print "ARRRDUINO"
            sleep(1)


    def changeState(self, state):
        if state:
            self.queue.put(["POP", "CORN"])
        else:
            self.queue.put(["POP", "CORN"])

        print "zmieniono "
        print state

    def start(self):
        print "START!"
        p = Process(target=self.startLoop, args=(self.queue,)).start()
        print "OKK!"


if __name__ == "__main__":
    global popcorn
    popcorn = inSer.interactiveSerial()
    popcorn.start()

    popcorn.changeState(True)
    sleep(3)
    popcorn.changeState(False)
    sleep(2)
    popcorn.changeState(True)