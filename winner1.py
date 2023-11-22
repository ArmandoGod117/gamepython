import pygame
import sys

pygame.init()

PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

EUSE = pygame.transform.scale(pygame.image.load("img/youwin.png"), (1000, 700))

IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonsalida3.png"), (100, 80))
IMG_SALIR_PRESS = pygame.transform.scale(pygame.image.load("img2/salir_2.png"), (102, 82))
IMG_NIVEL2 = pygame.transform.scale(pygame.image.load("img2/siguiente2.png"), (100, 80))
IMG_NIVEL2_PRESS = pygame.transform.scale(pygame.image.load("img2/siguiente2_2.png"), (102, 82))

#Música de fondo y control de volumen
pygame.mixer.music.load('musica/musicaganar.mp3')
volumen = 0.5  
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

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

def winner_1():
    global volumen

    BOTON_SALIR = Button(IMG_SALIR, IMG_SALIR_PRESS, 20, 20)
    NIVEL2 = Button(IMG_NIVEL2, IMG_NIVEL2_PRESS, 450, 620)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.blit(EUSE, (0, 0))
        
        BOTON_SALIR.update(PANTALLA)
        NIVEL2.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL2.check_for_input(MOUSE_POS):
                    from nivel2_español import nivel_2
                    nivel_2()
                elif BOTON_SALIR.check_for_input(MOUSE_POS):
                    from facil import facil1
                    facil1()
                    pygame.quit()
                    sys.exit()

        if BOTON_SALIR.check_for_input(MOUSE_POS):
            BOTON_SALIR.image = IMG_SALIR_PRESS
        else:
            BOTON_SALIR.image = IMG_SALIR
        if NIVEL2.check_for_input(MOUSE_POS):
            NIVEL2.image = IMG_NIVEL2_PRESS
        else:
            NIVEL2.image = IMG_NIVEL2
                    
        pygame.display.update()

winner_1()