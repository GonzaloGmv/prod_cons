from threading import Thread
from prodycons import productor, consumidor

def main():
    t1 = Thread(target=productor)
    t2 = Thread(target=consumidor)
    t1.start()
    t2.start()