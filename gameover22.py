import pygame
import sys
from botones import Button

pygame.init()

PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

EUSE = pygame.transform.scale(pygame.image.load("img/perdiste.png"), (1000, 700))

IMG_NIVEL22 = pygame.transform.scale(pygame.image.load("img2/Reiniciar.png"), (100, 80))
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonsalida3.png"), (100, 80))

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

def gameover_22():
    global volumen

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.blit(EUSE, (0, 0))
        
        TEXTO_MENU = obtener_fuente(60).render("", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        NIVEL22 = Button(image=IMG_NIVEL22, pos=(490, 650))
        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))

        for boton in [NIVEL22, BOTON_SALIR]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL22.checkForInput(MOUSE_POS):
                    from nivel22 import nivel_22
                    nivel_22
                    ()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from dificil import dificil1
                    dificil1()
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

gameover_22()
