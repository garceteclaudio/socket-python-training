import socket
import threading
import pickle
import time

HOST = "127.0.0.1"
PORT = 5555

# Crear socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor iniciado...")

# Diccionarios de estado global
clients = {}        # {pid: socket}
players = {}        # {pid: (x, y)}
bullets = []        # [ {owner, x, y, dx, dy} ]
damaged = {}        # {pid: tiempo_de_fin}


player_id = 0


# -----------------------------
# HILO QUE ACTUALIZA BALAS
# -----------------------------
def update_bullets():
    global bullets, damaged, players

    while True:
        time.sleep(0.016)  # ~60 FPS

        new_bullets = []
        for b in bullets:
            # mover bala
            b["x"] += b["dx"]
            b["y"] += b["dy"]

            # fuera de pantalla → eliminar
            if b["x"] < 0 or b["x"] > 600 or b["y"] < 0 or b["y"] > 400:
                continue

            # colisiones con jugadores
            hit = False
            for pid, pos in players.items():
                if pid == b["owner"]:
                    continue

                px, py = pos

                # Simple AABB
                if px < b["x"] < px + 30 and py < b["y"] < py + 30:
                    damaged[pid] = time.time() + 2  # 2 segundos rojo
                    hit = True
                    break

            if not hit:
                new_bullets.append(b)

        bullets = new_bullets

        # limpiar jugadores ya sanados
        now = time.time()
        for pid in list(damaged.keys()):
            if damaged[pid] <= now:
                del damaged[pid]


# -------------------------------------
# HILO PARA CADA CLIENTE
# -------------------------------------
def handle_client(conn, pid):
    global bullets, players, damaged

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            packet = pickle.loads(data)

            # Actualizar posición
            players[pid] = packet["pos"]

            # Añadir nuevas balas
            for b in packet["bullets"]:
                bullets.append(b)

            # Preparar estado para enviar
            full_state = {
                "players": players,
                "bullets": bullets,
                "damaged": damaged
            }

            blob = pickle.dumps(full_state)

            # Enviar estado a todos los clientes
            for c in clients.values():
                c.sendall(blob)

    except Exception as e:
        print("Error con cliente:", e)

    finally:
        print(f"Jugador {pid} desconectado")

        # Limpieza
        if pid in clients: del clients[pid]
        if pid in players: del players[pid]
        if pid in damaged: del damaged[pid]

        conn.close()


# -------------------------------------
# INICIAR HILO DE BALAS
# -------------------------------------
threading.Thread(target=update_bullets, daemon=True).start()


# -------------------------------------
# LOOP PRINCIPAL DEL SERVIDOR
# -------------------------------------
while True:
    conn, addr = server.accept()
    print(f"Cliente conectado desde {addr}")

    # Enviar PID al cliente
    conn.sendall(pickle.dumps({"pid": player_id}))

    # Registrar datos iniciales
    clients[player_id] = conn
    players[player_id] = (100, 100)

    # Iniciar hilo del cliente
    threading.Thread(
        target=handle_client,
        args=(conn, player_id),
        daemon=True
    ).start()

    player_id += 1
