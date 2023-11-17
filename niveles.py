
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
IMG_FACIL = pygame.transform.scale(pygame.image.load("img2/facil3.png"), (150, 100))
IMG_DIFICIL = pygame.transform.scale(pygame.image.load("img2/dificil3.png"), (150, 100))
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonrojo.png"), (100, 80))
IMG_HISTORIA = pygame.transform.scale(pygame.image.load("img2/historieta.png"), (100, 100))
IMG_CONTROLES = pygame.transform.scale(pygame.image.load("img2/btncontrol.png"), (100, 80))


# Variables para el movimiento del fondo
posicion_fondo = -200
desplazamiento = 1
direccion = 1  

# Música de fondo y control de volumen
pygame.mixer.music.load('musica/nivel1.mp3')
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
    pygame.draw.rect(surface, (255, 0, 0), (position[0], position[1], inner_width, bar_height))

def niveles1():
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

        FACIL = Button(image=IMG_FACIL, pos=(500, 300))
        DIFICIL = Button(image=IMG_DIFICIL, pos=(500, 450))
        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))
        HISTORIA = Button(image=IMG_HISTORIA, pos=(910, 460))
        CONTROLES = Button(image=IMG_CONTROLES, pos=(900, 580))

        for boton in [FACIL, DIFICIL, BOTON_SALIR, HISTORIA, CONTROLES]:
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
                if FACIL.checkForInput(MOUSE_POS):
                    from facil import facil1
                    facil1()
                elif DIFICIL.checkForInput(MOUSE_POS):
                    from dificil import dificil1
                    dificil1()
                elif HISTORIA.checkForInput(MOUSE_POS):
                    from historia import historia_1
                    historia_1()
                elif CONTROLES.checkForInput(MOUSE_POS):
                    from controles import controles1
                    controles1()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from menu import menu_principal
                    menu_principal()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)
                    
        pygame.display.update()

niveles1()