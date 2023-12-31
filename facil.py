import pygame
import sys

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/recepcion.png"), (1200, 700))

# Cargar imágenes de botones
IMG_NIVEL1 = pygame.transform.scale(pygame.image.load("img2/botonnivel1.png"), (180, 80))
IMG_NIVEL1_PRESS = pygame.transform.scale(pygame.image.load("img2/1_2.png"), (182, 82))
IMG_NIVEL2 = pygame.transform.scale(pygame.image.load("img2/botonnivel2.png"), (180, 80))
IMG_NIVEL2_PRESS = pygame.transform.scale(pygame.image.load("img2/2_2.png"), (182, 82))
IMG_NIVEL3 = pygame.transform.scale(pygame.image.load("img2/botonnivel3.png"), (180, 80))
IMG_NIVEL3_PRESS = pygame.transform.scale(pygame.image.load("img2/3_2.png"), (182, 82))
IMG_CONTROLES1 = pygame.transform.scale(pygame.image.load("img2/btncontrol.png"), (100, 80))
IMG_CONTROLES1_PRESS = pygame.transform.scale(pygame.image.load("img2/btncontrol_2.png"), (102, 82))
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonrojo.png"), (100, 80))
IMG_SALIR_PRESS = pygame.transform.scale(pygame.image.load("img2/botonrojo_2.png"), (102, 82))

# Variables para el movimiento del fondo
posicion_fondo = -200
desplazamiento = 1
direccion = 1  # 1 representa hacia la derecha, -1 hacia la izquierda

# Música de fondo y control de volumen
pygame.mixer.music.load('musica/musicafondo.mp3')
volumen = 0.5  
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

def dibujar_barra_volumen(surface, volumen):
    bar_width = 100
    bar_height = 20
    position = (50, 650)
    inner_width = bar_width * volumen
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], bar_width, bar_height), 2)
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], inner_width, bar_height))

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

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

def facil1():
    global posicion_fondo, direccion, volumen

    BOTON_SALIR = Button(IMG_SALIR, IMG_SALIR_PRESS, 20, 20)
    CONTROLES1 = Button(IMG_CONTROLES1, IMG_CONTROLES1_PRESS, 880, 580)
    NIVEL1 = Button(IMG_NIVEL1, IMG_NIVEL1_PRESS, 400, 250)
    NIVEL2 = Button(IMG_NIVEL2, IMG_NIVEL2_PRESS, 400, 350)
    NIVEL3 = Button(IMG_NIVEL3, IMG_NIVEL3_PRESS, 400, 450)

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
        CONTROLES1.update(PANTALLA)
        NIVEL1.update(PANTALLA)
        NIVEL2.update(PANTALLA)
        NIVEL3.update(PANTALLA)
        
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
                if NIVEL1.check_for_input(MOUSE_POS):
                    from nivel1_español import nivel_1
                    nivel_1()
                elif NIVEL2.check_for_input(MOUSE_POS):
                    from nivel2_español import nivel_2
                    nivel_2()
                elif NIVEL3.check_for_input(MOUSE_POS):
                    from nivel3_español import nivel_3
                    nivel_3()
                elif CONTROLES1.check_for_input(MOUSE_POS):
                    from controles1 import controles_1
                    controles_1()
                elif BOTON_SALIR.check_for_input(MOUSE_POS):
                    from niveles import niveles1
                    niveles1()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)

        if BOTON_SALIR.check_for_input(MOUSE_POS):
            BOTON_SALIR.image = IMG_SALIR_PRESS
        else:
            BOTON_SALIR.image = IMG_SALIR
        if CONTROLES1.check_for_input(MOUSE_POS):
            CONTROLES1.image = IMG_CONTROLES1_PRESS
        else:
            CONTROLES1.image = IMG_CONTROLES1

        if NIVEL1.check_for_input(MOUSE_POS):
            NIVEL1.image = IMG_NIVEL1_PRESS
        else:
            NIVEL1.image = IMG_NIVEL1
        if NIVEL2.check_for_input(MOUSE_POS):
            NIVEL2.image = IMG_NIVEL2_PRESS
        else:
            NIVEL2.image = IMG_NIVEL2
        if NIVEL3.check_for_input(MOUSE_POS):
            NIVEL3.image = IMG_NIVEL3_PRESS
        else:
            NIVEL3.image = IMG_NIVEL3

        pygame.display.update()

facil1()