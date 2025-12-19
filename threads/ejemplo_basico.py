import threading
import time

def tarea(nombre):
    print(f"Inicio de {nombre}")
    time.sleep(0.5)
    print(f"Fin de {nombre}")

# Crear threads
thread1 = threading.Thread(target=tarea, args=("Hilo 1",))
thread2 = threading.Thread(target=tarea, args=("Hilo 2",))
thread3 = threading.Thread(target=tarea, args=("Hilo 3",))
thread4 = threading.Thread(target=tarea, args=("Hilo 4",))

# Iniciar threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()


# Esperar a que terminen
thread1.join()
thread2.join()
thread3.join()
thread4.join()


print("Programa terminado")
