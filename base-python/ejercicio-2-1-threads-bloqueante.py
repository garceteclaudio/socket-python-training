import time

# Programa sin threads (bloqueante)

def tarea():
    time.sleep(2)
    print("Tarea terminada")

tarea()
tarea()