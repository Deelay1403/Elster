import multiprocessing
import inyeractiveSerial

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(i,))
    p.start()