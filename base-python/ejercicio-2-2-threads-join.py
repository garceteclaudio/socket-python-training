import threading
import time

# Registrar tiempo de inicio
tiempo_inicio = time.time()

def tarea1(numero):
    print(f"Iniciando metodo tarea 1 con número {numero}")
    time.sleep(numero)
    print(f"Tarea 1 terminada")

def tarea2():
    print("Iniciando metodo tarea 2...")
    time.sleep(2)
    print("Tarea 2 terminada")

def tarea3():
    print("Iniciando metodo tarea 3..")
    time.sleep(4)
    print("Tarea 3 terminada")

print("-----------Creando e iniciando hilos-----------")
#crea el thread
hilo1 = threading.Thread(target=tarea1, args=(7,))
hilo2 = threading.Thread(target=tarea2)
hilo3 = threading.Thread(target=tarea3)

print("-----------Empiezan los  hilos-----------")
#inicia el thread
hilo1.start()
hilo2.start()
hilo3.start()

# Obtener el id de los dos hilos
print(f"ID del hilo 1: {hilo1.native_id}")
print(f"ID del hilo 2: {hilo2.native_id}") 
print(f"ID del hilo 3: {hilo3.native_id}")

print("-----------Programa sigue ejecutándose-----------")

# join() sirve para esperar a que los hilos terminen antes de continuar
# Sin join(), el programa terminaría antes de que los hilos completen su trabajo
# Bloquea la ejecucion el join
print("\nEsperando a que todos los hilos terminen...")
hilo1.join()
hilo2.join()
hilo3.join()

print("Todos los hilos han terminado. Programa finalizado.")




# Calcular y mostrar tiempo total de ejecución
tiempo_fin = time.time()
tiempo_total = tiempo_fin - tiempo_inicio
print(f"\nTiempo total de ejecución: {tiempo_total:.2f} segundos")