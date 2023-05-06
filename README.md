# prod_cons

El link a este repositorio es: [github](https://github.com/GonzaloGmv/prod_cons)

En este proyecto habia que simular el problema de los productores y consumidores. Yo lo he resuelto con semáforos y sin semáforos.

El código es el siguiente:

### Código sin semáforos
```
from queue import Queue
import time

cola = Queue()

def prod_sin():
    i = 1
    while True:
        cola.put(i)
        cola.join()
        print(f"Producto {i} producido")
        i += 1
        time.sleep(1)

def cons_sin():
    while True:
        producto = cola.get()
        print(f"Producto {producto} consumido")
        cola.task_done()
        time.sleep(1)
```

### Código con semáforos
```
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
```        

### Lanzador
```
from threading import Thread
from codigo.sin_semaforos import prod_sin, cons_sin
from codigo.con_semaforos import prod_con, cons_con
import time

def main():
    n = input("Presione 1 si quiere ejecutarlo sin semaforos y 2 si quiere ejecutarlo con semaforos: ")
    if n == "1":
        print("Ejecutando sin semaforos...",'\n')
        time.sleep(1)
        t1 = Thread(target=prod_sin)
        t2 = Thread(target=cons_sin)
        t1.start()
        t2.start()
    elif n == "2":
        print("Ejecutando con semaforos...",'\n')
        time.sleep(1)
        t1 = Thread(target=prod_con)
        t2 = Thread(target=cons_con)
        t1.start()
        t2.start()
```

### Main
```
from lanzador import main

if __name__ == '__main__':
    main()
```    
