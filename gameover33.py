import pygame
import sys
from botones import Button

pygame.init()

PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

EUSE = pygame.transform.scale(pygame.image.load("img/perdiste.png"), (1000, 700))

IMG_NIVEL33 = pygame.transform.scale(pygame.image.load("img2/Reiniciar.png"), (100, 80))
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonsalida3.png"), (100, 80))

#Música de fondo y control de volumen
pygame.mixer.music.load('musica/musicaperder.mp3')
volumen = 0.5  
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

def gameover_33():
    global volumen

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.blit(EUSE, (0, 0))
        
        TEXTO_MENU = obtener_fuente(60).render("", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))
        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        NIVEL33 = Button(image=IMG_NIVEL33, pos=(490, 650))
        BOTON_SALIR = Button(image=IMG_SALIR, pos=(80, 50))

        for boton in [NIVEL33, BOTON_SALIR]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL33.checkForInput(MOUSE_POS):
                    from nivel33_español import nivel33_español
                    pygame.mixer.stop()
                    nivel33_español()
                elif BOTON_SALIR.checkForInput(MOUSE_POS):
                    from dificil import dificil1
                    dificil1()
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

gameover_33()


