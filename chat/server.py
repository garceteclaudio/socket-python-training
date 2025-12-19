import socket

# Dirección y puerto
HOST = "127.0.0.1"   # localhost
PORT = 5000

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar IP y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones (solo 1 cliente)
server_socket.listen(1)

print("Servidor esperando conexión...")

# Aceptar cliente  bloquea el proceso y espera a una conexión entrante
conn, addr = server_socket.accept()
print(f"Cliente conectado desde {addr}")

nombre_cliente = conn.recv(1024)
print("El cliente que se conecto se llama:", nombre_cliente.decode())

#- espera cliente
#- crea socket nuevo (conn)
#- devuelve IP y puerto (addr)
#- bloquea el programa

# server_socket = escuchar conexiones
#conn = intercambiar datos

# Loop principal (sin hilos)
while True:
    # Recibir mensaje del cliente
    data = conn.recv(1024)

    if not data:
        print(f"{nombre_cliente.decode()} desconectado")
        break

    mensaje = data.decode()
    print(f"{nombre_cliente.decode()}:", mensaje)

    # Respuesta del servidor
    respuesta = input("Servidor: ")
    conn.send(respuesta.encode())

# Cerrar conexiones
conn.close()
server_socket.close()
