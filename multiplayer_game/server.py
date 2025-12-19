import socket
import threading
import pickle

# IP y puerto del servidor
HOST = "127.0.0.1"
PORT = 5555

# Crear socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar IP y puerto
server.bind((HOST, PORT))

# Escuchar conexiones entrantes
server.listen()

print("Servidor iniciado...")

# Diccionario de clientes conectados
clients = {}

# Diccionario de posiciones de jugadores
positions = {}

# ID incremental para jugadores
player_id = 0


def handle_client(conn, pid):
    """Maneja la comunicación con un cliente"""
    try:
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)

            # Si no hay datos, el cliente se desconectó
            if not data:
                break

            # Convertir bytes a posición (x, y)
            # Recibes bytes del cliente y los conviertes en una tupla (x, y).
            positions[pid] = pickle.loads(data)
            #print(f"Posicion {pid}: ", positions[pid])

            ## Enviar todas las posiciones a todos los clientes
            #for c in clients.values():
                ## pickle.dumps() convierte un objeto en una secuencia de bytes
                #c.sendall(pickle.dumps(positions))

            #Serializar SOLO una vez por frame/actualización, ahorra cpu
            data = pickle.dumps(positions)
            for c in clients.values():
                c.sendall(data)
    except:
        pass
    finally:
        # Limpieza al desconectarse
        print(f"Jugador {pid} desconectado")
        del clients[pid]
        del positions[pid]
        conn.close()


# Bucle principal del servidor
while True:
    # Esperar conexión de un cliente
    conn, addr = server.accept()
    print(f"Cliente conectado desde {addr}")

    # Registrar cliente
    clients[player_id] = conn
    positions[player_id] = (100, 100)

    # Crear hilo para el cliente
    threading.Thread(
        target=handle_client,
        args=(conn, player_id),
        daemon=True
    ).start()

    # Incrementar ID del jugador
    player_id += 1
