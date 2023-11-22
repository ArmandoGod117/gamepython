import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/controles.png"), (1000, 700))

# Cargar imágenes de botones
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonrojo.png"), (100, 80))

# Música de fondo y control de volumen
pygame.mixer.music.load('musica/musicafondo.mp3')
volumen = 0.5  
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

def dibujar_barra_volumen(surface, volumen):
    bar_width = 100
    bar_height = 20
    position = (50, 650)
    inner_width = bar_width * volumen
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], bar_width, bar_height), 2)
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], inner_width, bar_height))

def controles_1():
    global volumen

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        # Calculate the position to center the image
        img_x = (PANTALLA.get_width() - EUSE.get_width()) / 2
        img_y = (PANTALLA.get_height() - EUSE.get_height()) / 2

        PANTALLA.blit(EUSE, (img_x, img_y))

        TEXTO_MENU = obtener_fuente(60).render("", True, "#00000000")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))

        for boton in [BOTON_SALIR]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Ajustar el volumen con las teclas de flecha
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    volumen += 0.1
                    if volumen > 1:
                        volumen = 1
                    pygame.mixer.music.set_volume(volumen)
                elif event.key == pygame.K_DOWN:
                    volumen -= 0.1
                    if volumen < 0:
                        volumen = 0
                    pygame.mixer.music.set_volume(volumen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_SALIR.checkForInput(MOUSE_POS):
                    from facil import facil1
                    facil1()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        #dibujar_barra_volumen(PANTALLA, volumen)
                    
        pygame.display.update()

controles_1()
