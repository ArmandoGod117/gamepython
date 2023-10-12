import pygame
import sys
import random  # <- No olvides importar random

# [El resto del código anterior permanece igual]

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # <- Nuevo color
WIDTH = -50
HEIGHT= -50
# [El resto del código anterior permanece igual]

# Definir posición inicial del bloque azul
blue_x, blue_y = random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50)

# Iniciar el bucle del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    
    # Lógica de colisión
    if (x < blue_x + 50 and x + 50 > blue_x and
            y < blue_y + 50 and y + 50 > blue_y):
        blue_x, blue_y = random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50)

    # Dibujar en pantalla
    window.fill(WHITE)
    pygame.draw.rect(window, RED, (x, y, 50, 50))
    pygame.draw.rect(window, BLUE, (blue_x, blue_y, 50, 50))  # <- Dibujar el bloque azul

    # Actualizar la ventana
    pygame.display.flip()
    
    # Limitar la tasa de frames
    pygame.time.Clock().tick(30)

# Finalizar Pygame
pygame.quit()
sys.exit()
