import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()


# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Eusebio vs el Virus del Mal")

# Carga de imágenes
gameover1 = pygame.transform.scale(pygame.image.load("img/win1.png"), (1200, 700))

#musica de fondo
pygame.mixer.music.load('musica/nivel1.mp3')
pygame.mixer.music.play(-1)  



# Función para obtener una fuente con el tamaño deseado
def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

# Función para mostrar el menú principal
def niveles():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(gameover1,(0,0))

        TEXTO_MENU = obtener_fuente(50).render(".", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(600, 80))

        REINICIAR = Button(image=None, pos=(700, 430), text_input="VOLVER A JUGAR", font=obtener_fuente(35), base_color="#00000000", hovering_color="#5F9EA0")
        BOTON_SALIR = Button(image=None, pos=(50, 30), text_input="SALIR", font=obtener_fuente(30), base_color="#DC143C", hovering_color="#5F9EA0")

        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        for boton in [REINICIAR, BOTON_SALIR]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REINICIAR.checkForInput(MOUSE_POS):
                    import nivel1
                    nivel1()

              
                if BOTON_SALIR.checkForInput(MOUSE_POS):
                    from niveles import niveles
                    niveles()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

niveles()