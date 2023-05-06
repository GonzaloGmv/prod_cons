
from queue import Queue
import time
from threading import Thread, Semaphore

cola = Queue()
semaforo = Semaphore(0)

def productor():
    i = 1
    while True:
        cola.put(i)
        cola.join()
        print(f"Producto {i} producido")
        i += 1
        semaforo.release()
        time.sleep(1)

def consumidor():
    while True:
        semaforo.acquire()
        producto = cola.get()
        print(f"Producto {producto} consumido")
        cola.task_done()
        time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=productor)
    t2 = Thread(target=consumidor)
    t1.start()
    t2.start()
