from multiprocessing import Process, Queue
import interactiveSerial_nauka as inSer
from time import sleep


if __name__ == '__main__':
    print "TEST"
    global popcorn
    popcorn = inSer.interactiveSerial()
    popcorn.start()

    popcorn.changeState(False)
    sleep(3)
    popcorn.changeState(True)