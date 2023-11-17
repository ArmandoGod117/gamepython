import pygame
import sys
from botones import Button

pygame.init()

PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

EUSE = pygame.transform.scale(pygame.image.load("img/youwin.png"), (1000, 700))

IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonsalida3.png"), (100, 80))
IMG_NIVEL11 = pygame.transform.scale(pygame.image.load("img2/siguiente2.png"), (100, 80))

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)


def winner_3():
    global volumen

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.blit(EUSE, (0, 0))
        
        TEXTO_MENU = obtener_fuente(60).render("", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))
        NIVEL11 = Button(image=IMG_NIVEL11, pos=(500, 650))

        for boton in [BOTON_SALIR, NIVEL11]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL11.checkForInput(MOUSE_POS):
                    from nivel11 import nivel_11
                    nivel_11()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from facil import facil1
                    facil1()
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

winner_3()