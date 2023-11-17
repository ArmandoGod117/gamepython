import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/recepcion.png"), (1200, 700))

# Cargar imágenes de botones
IMG_NIVEL1 = pygame.transform.scale(pygame.image.load("img2/btondificil1.png"), (180, 80))
IMG_NIVEL2 = pygame.transform.scale(pygame.image.load("img2/btondificil2.png"), (180, 80))
IMG_NIVEL3 = pygame.transform.scale(pygame.image.load("img2/btondificil3.png"), (180, 80))
IMG_CONTROLES2 = pygame.transform.scale(pygame.image.load("img2/btncontrol.png"), (100, 80))
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonrojo.png"), (100, 80))


# Variables para el movimiento del fondo
posicion_fondo = -200
desplazamiento = 1
direccion = 1  # 1 representa hacia la derecha, -1 hacia la izquierda

# Música de fondo y control de volumen
pygame.mixer.music.load('musica/nivel1.mp3')
volumen = 0.5  
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

def dibujar_barra_volumen(surface, volumen):
    bar_width = 200
    bar_height = 20
    position = (50, 650)
    inner_width = bar_width * volumen
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], bar_width, bar_height), 2)
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], inner_width, bar_height))

def dificil1():
    global posicion_fondo, direccion, volumen

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        # Desplazamiento del fondo
        posicion_fondo += desplazamiento * direccion
        if posicion_fondo >= 0:
            direccion = -1
        elif posicion_fondo <= -200:
            direccion = 1
        
        PANTALLA.blit(EUSE, (posicion_fondo, 0))
        
        TEXTO_MENU = obtener_fuente(60).render("Epidemic fight", True, "#00000000")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        NIVEL11 = Button(image=IMG_NIVEL1, pos=(500, 250))
        NIVEL22 = Button(image=IMG_NIVEL2, pos=(500, 350))
        NIVEL33 = Button(image=IMG_NIVEL3, pos=(500, 450))
        CONTROLES2 = Button(image=IMG_CONTROLES2, pos=(900, 580))
        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))

        for boton in [NIVEL11, NIVEL22, NIVEL33, BOTON_SALIR, CONTROLES2]:
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
                if NIVEL11.checkForInput(MOUSE_POS):
                    from nivel11 import nivel_11
                    nivel_11()
                elif NIVEL22.checkForInput(MOUSE_POS):
                    from nivel22 import nivel_22
                    nivel_22()
                elif NIVEL33.checkForInput(MOUSE_POS):
                    from nivel33 import nivel_33
                    nivel_33()
                elif CONTROLES2.checkForInput(MOUSE_POS):
                    from controles2 import controles_2
                    controles_2()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from niveles import niveles1

                    niveles1()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)
                    
        pygame.display.update()

dificil1()