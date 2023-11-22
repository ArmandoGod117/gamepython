import pygame
import sys

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
PANTALLA2 = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/recepcion.png"), (1200, 700))

# Cargar imágenes de botones
IMG_FACIL = pygame.transform.scale(pygame.image.load("img2/facil3.png"), (150, 100))
IMG_FACIL_PRESS = pygame.transform.scale(pygame.image.load("img2/facil3_2.png"), (152, 102))
IMG_DIFICIL = pygame.transform.scale(pygame.image.load("img2/dificil3.png"), (150, 100))
IMG_DIFICIL_PRESS = pygame.transform.scale(pygame.image.load("img2/dificil3_2.png"), (152, 102))
IMG_SALIR = pygame.image.load("img2/btonrojo.png")
IMG_SALIR_PRESS = pygame.transform.scale(pygame.image.load("img2/botonrojo_2.png"), (101, 82))
IMG_HISTORIA = pygame.transform.scale(pygame.image.load("img2/historieta.png"), (100, 100))
IMG_HISTORIA_PRESS = pygame.transform.scale(pygame.image.load("img2/historieta_2.png"), (102, 102))
IMG_CONTROLES = pygame.transform.scale(pygame.image.load("img2/btncontrol.png"), (100, 80))
IMG_CONTROLES_PRESS = pygame.transform.scale(pygame.image.load("img2/btncontrol_2.png"), (102, 82))

# Variables para el movimiento del fondo
posicion_fondo = -200
desplazamiento = 1
direccion = 1  

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
    pygame.draw.rect(surface, (255, 0, 0), (position[0], position[1], inner_width, bar_height))    

class Button:
    def __init__(self, default_image, hover_image, x, y):
        self.default_image = default_image
        self.hover_image = hover_image
        self.image = default_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def check_for_input(self, pos):
        return self.rect.collidepoint(pos)

def niveles1():
    global posicion_fondo, direccion, volumen

    # Crear el botón salir fuera del bucle para evitar el UnboundLocalError
    BOTON_SALIR = Button(IMG_SALIR, IMG_SALIR_PRESS, 20, 20)
    FACIL = Button(IMG_FACIL, IMG_FACIL_PRESS, 425, 250)
    DIFICIL = Button(IMG_DIFICIL, IMG_DIFICIL_PRESS, 425, 400)
    HISTORIA = Button(IMG_HISTORIA, IMG_HISTORIA_PRESS, 890, 460)
    CONTROLES = Button(IMG_CONTROLES, IMG_CONTROLES_PRESS, 880, 580)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        # Desplazamiento del fondo
        posicion_fondo += desplazamiento * direccion
        if posicion_fondo >= 0:
            direccion = -1
        elif posicion_fondo <= -200:
            direccion = 1
        
        PANTALLA.blit(EUSE, (posicion_fondo, 0))

        BOTON_SALIR.update(PANTALLA)
        FACIL.update(PANTALLA)
        DIFICIL.update(PANTALLA)
        HISTORIA.update(PANTALLA)
        CONTROLES.update(PANTALLA)

        TEXTO_MENU = obtener_fuente(60).render("Epidemic fight", True, "#00000000")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

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
                if FACIL.check_for_input(MOUSE_POS):
                    from facil import facil1
                    facil1()
                elif DIFICIL.check_for_input(MOUSE_POS):
                    from dificil1 import dificil1
                    dificil1()
                elif HISTORIA.check_for_input(MOUSE_POS):
                    from historia import historia_1
                    historia_1()
                elif CONTROLES.check_for_input(MOUSE_POS):
                    from controles import controles1
                    controles1()
                elif BOTON_SALIR.check_for_input(MOUSE_POS):
                    from menu import menu_principal
                    menu_principal()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)


        if BOTON_SALIR.check_for_input(MOUSE_POS):
            BOTON_SALIR.image = IMG_SALIR_PRESS
        else:
            BOTON_SALIR.image = IMG_SALIR
        if FACIL.check_for_input(MOUSE_POS):
            FACIL.image = IMG_FACIL_PRESS
        else:
            FACIL.image = IMG_FACIL
        if HISTORIA.check_for_input(MOUSE_POS):
            HISTORIA.image = IMG_HISTORIA_PRESS
        else:
            HISTORIA.image = IMG_HISTORIA
        if CONTROLES.check_for_input(MOUSE_POS):
            CONTROLES.image = IMG_CONTROLES_PRESS
        else:
            CONTROLES.image = IMG_CONTROLES
        if DIFICIL.check_for_input(MOUSE_POS):
            DIFICIL.image = IMG_DIFICIL_PRESS
        else:
            DIFICIL.image = IMG_DIFICIL
                    
        pygame.display.update()

niveles1()
