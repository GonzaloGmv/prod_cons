# prod_cons

El link a este repositorio es: [github](https://github.com/GonzaloGmv/prod_cons)

En este proyecto habia que simular el problema de los productores y consumidores. Yo lo he resuelto mediente hilos y colas, pero hay más formas.

El código es el siguiente:

### Código principal
```
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
```

### Lanzador
```
from threading import Thread
from prodycons import productor, consumidor

def main():
    t1 = Thread(target=productor)
    t2 = Thread(target=consumidor)
    t1.start()
    t2.start()
```

### Main
```
from lanzador import main

if __name__ == '__main__':
    main()
```    
