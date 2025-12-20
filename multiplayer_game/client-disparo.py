import pygame
import socket
import pickle

WIDTH, HEIGHT = 600, 400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# -------------------------
#   CONEXIÓN AL SERVIDOR
# -------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

# recibir PID asignado por el servidor
data = client.recv(1024)
my_pid = pickle.loads(data)["pid"]
print("Mi PID:", my_pid)

# -------------------------
#   VARIABLES DEL CLIENTE
# -------------------------
x, y = 100, 100
speed = 5

# dirección hacia donde mira el jugador
look_dx = 1
look_dy = 0

# lista temporal de balas nuevas
new_bullets = []

# -------------------------
#        LOOP PRINCIPAL
# -------------------------
running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # disparo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            b = {
                "owner": my_pid,
                "x": x + 15,
                "y": y + 15,
                "dx": look_dx * 10,
                "dy": look_dy * 10
            }
            new_bullets.append(b)

    # --- Movimiento ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= speed
        look_dx, look_dy = -1, 0

    if keys[pygame.K_d]:
        x += speed
        look_dx, look_dy = 1, 0

    if keys[pygame.K_w]:
        y -= speed
        look_dx, look_dy = 0, -1

    if keys[pygame.K_s]:
        y += speed
        look_dx, look_dy = 0, 1

    # --- Enviar paquete al servidor ---
    packet = {
        "pos": (x, y),
        "bullets": new_bullets
    }
    client.sendall(pickle.dumps(packet))

    # limpiar balas luego de enviar
    new_bullets = []

    # --- Recibir estado global ---
    data = client.recv(8192)
    state = pickle.loads(data)

    players = state["players"]
    bullets = state["bullets"]
    damaged = state["damaged"]

    # --- Dibujar jugadores ---
    for pid, pos in players.items():
        px, py = pos
        color = (255, 0, 0) if pid in damaged else (0, 200, 255)
        pygame.draw.rect(screen, color, (px, py, 30, 30))

    # --- Dibujar balas ---
    for b in bullets:
        pygame.draw.circle(screen, (255, 255, 0), (int(b["x"]), int(b["y"])), 5)

    # --- Posición en pantalla ---
    text = font.render(f"X:{x} Y:{y}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()
client.close()
