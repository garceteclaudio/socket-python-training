import socket

# Dirección del servidor
HOST = "127.0.0.1"
PORT = 5000

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
client_socket.connect((HOST, PORT))
print("Conectado al servidor")

nombre = input("Tu nombre: ")
client_socket.send(nombre.encode()) 

while True:
    mensaje = input(f"{nombre}: ")
    # Enviar mensaje al servidor
    client_socket.send(mensaje.encode())

    if mensaje.lower() == "salir":
        break

    # Recibir respuesta del servidor
    data = client_socket.recv(1024)
    print("Servidor:", data.decode())

# Cerrar conexión
client_socket.close()
