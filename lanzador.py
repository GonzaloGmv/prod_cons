from threading import Thread
from sin_semaforos import prod_sin, cons_sin
from con_semaforos import prod_con, cons_con
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