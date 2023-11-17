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
IMG_NIVEL1 = pygame.transform.scale(pygame.image.load("img2/botonnivel1.png"), (180, 80))
IMG_NIVEL2 = pygame.transform.scale(pygame.image.load("img2/botonnivel2.png"), (180, 80))
IMG_NIVEL3 = pygame.transform.scale(pygame.image.load("img2/botonnivel3.png"), (180, 80))
IMG_CONTROLES1 = pygame.transform.scale(pygame.image.load("img2/btncontrol.png"), (100, 80))
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



def facil1():
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

        NIVEL1 = Button(image=IMG_NIVEL1, pos=(500, 250))
        NIVEL2 = Button(image=IMG_NIVEL2, pos=(500, 350))
        NIVEL3 = Button(image=IMG_NIVEL3, pos=(500, 450))
        CONTROLES1 = Button(image=IMG_CONTROLES1, pos=(900, 580))
        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))

        for boton in [NIVEL1, NIVEL2, NIVEL3, BOTON_SALIR, CONTROLES1]:
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
                if NIVEL1.checkForInput(MOUSE_POS):
                    from nivel1 import nivel_1
                    nivel_1()
                elif NIVEL2.checkForInput(MOUSE_POS):
                    from nivel2 import nivel_2
                    nivel_2()
                elif NIVEL3.checkForInput(MOUSE_POS):
                    from nivel3 import nivel_3
                    nivel_3()
                elif CONTROLES1.checkForInput(MOUSE_POS):
                    from controles1 import controles_1
                    controles_1()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from niveles import niveles1
                    niveles1()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
      
        pygame.display.update()

facil1()