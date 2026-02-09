import threading
import time

def tarea():
    print("Hilo: iniciando tarea...")
    time.sleep(3)
    print("Hilo: tarea terminada")

hilo = threading.Thread(target=tarea)

hilo.start()

print("Main: el programa principal terminó")