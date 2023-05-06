from threading import Semaphore
from queue import Queue
import time



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
