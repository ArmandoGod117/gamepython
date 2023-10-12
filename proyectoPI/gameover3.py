import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()


# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
gameover3 = pygame.transform.scale(pygame.image.load("img/gameover.jpg"), (1200, 700))

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
        PANTALLA.blit(gameover3,(0,0))

        TEXTO_MENU = obtener_fuente(50).render("Epidemic fight", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(600, 80))

        REINICIAR = Button(image=None, pos=(600, 620), text_input="REINICIAR", font=obtener_fuente(50), base_color="#5F9EA0", hovering_color="#DC143C")
        BOTON_SALIR = Button(image=None, pos=(50, 30), text_input="SALIR", font=obtener_fuente(30), base_color="#5F9EA0", hovering_color="#DC143C")

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
                    import nivel3
                    nivel3()

                if BOTON_SALIR.checkForInput(MOUSE_POS):
                    from niveles import niveles
                    niveles()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

niveles()
