import queue

#es una cola FIFO: el primer elemento en entrar es el primero en salir
q = queue.Queue()

q.put("Hola")
q.put("Mundo")
q.put("Como")
q.put("estan")

print(q.get())
print(q.get())
print(q.get()) 
print(q.get()) 

while not q.empty():
    print(q.get())