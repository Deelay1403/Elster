from multiprocessing import Process, Queue
import interactiveSerial as inSer
from time import sleep


if __name__ == '__main__':
    print "TEST"
    global popcorn
    popcorn = inSer.interactiveSerial("ok")
    popcorn.start()
    popcorn.send(":P")
    sleep(3)
    popcorn.send("XD")
    while   True:
        print "POPCORN"
        sleep(3)