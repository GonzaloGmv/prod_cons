from queue import Queue
import time
from threading import Semaphore

cola = Queue()
semaforo = Semaphore(0)

def prod_con():
    i = 1
    while True:
        cola.put(i)
        print(f"Producto {i} producido")
        i += 1
        semaforo.release()
        time.sleep(1)

def cons_con():
    while True:
        semaforo.acquire()
        producto = cola.get()
        print(f"Producto {producto} consumido")
        cola.task_done()
        time.sleep(1)