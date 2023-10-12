import pygame
import sys

# Inicializar Pygame
pygame.init()

# Establecer dimensiones de la ventana
window_size = (500, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Cronómetro")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar el reloj y fuente
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def display_time(milliseconds):
    """Función para mostrar el tiempo en la ventana."""
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    
    # Formatear el tiempo como M:SS:mm (min:sec:msec)
    time_string = "{:0>2}:{:0>2}.{:0>2}".format(minutes, seconds, milliseconds//10)
    
    # Render y mostrar el tiempo
    time_text = font.render(time_string, True, BLACK)
    window.blit(time_text, (250 - time_text.get_width() // 2, 150 - time_text.get_height() // 2))

# Variables para controlar el tiempo
start_ticks = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Calcular milisegundos transcurridos
    elapsed_milliseconds = pygame.time.get_ticks() - start_ticks
    
    # Limpia la ventana
    window.fill(WHITE)
    
    # Mostrar el tiempo
    display_time(elapsed_milliseconds)
    
    # Actualizar la ventana
    pygame.display.flip()
    
    # Limitar los FPS
    clock.tick(60)

pygame.quit()
sys.exit()
