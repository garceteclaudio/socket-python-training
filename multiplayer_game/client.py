import pygame
import socket
import pickle

WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cliente Multiplayer")

clock = pygame.time.Clock()

# Fuente para mostrar texto
font = pygame.font.SysFont("Arial", 20)

# Conexión al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

x, y = 100, 100
speed = 5

running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # -------------------
    # Movimiento WASD
    # -------------------
    if keys[pygame.K_a]:   # izquierda
        x -= speed
    if keys[pygame.K_d]:   # derecha
        x += speed
    if keys[pygame.K_w]:   # arriba
        y -= speed
    if keys[pygame.K_s]:   # abajo
        y += speed

    # Enviar posición al servidor
    client.sendall(pickle.dumps((x, y)))

    # Recibir todas las posiciones
    data = client.recv(4096)
    positions = pickle.loads(data)

    # Dibujar jugadores
    for pid, pos in positions.items():
        pygame.draw.rect(screen, (0, 200, 255), (*pos, 30, 30))

    # -----------------------------
    # Mostrar la posición x, y
    # -----------------------------
    text = font.render(f"X: {x}   Y: {y}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()
client.close()
