from threading import Semaphore
from queue import Queue
import time

cola = Queue()

def productor():
    i = 1
    while True:
        cola.put(i)
        cola.join()
        print(f"Producto {i} producido")
        i += 1
        time.sleep(1)

def consumidor():
    while True:
        producto = cola.get()
        print(f"Producto {producto} consumido")
        cola.task_done()
        time.sleep(1)
