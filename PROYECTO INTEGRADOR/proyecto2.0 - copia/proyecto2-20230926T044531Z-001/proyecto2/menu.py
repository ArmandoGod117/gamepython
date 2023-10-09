import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/fondomenu.png"), (1000, 700))
# Función para obtener una fuente con el tamaño deseado
def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

#musica de fondo
pygame.mixer.music.load('musica/nivel1.mp3')
pygame.mixer.music.play(-1)  

# Función para mostrar el menú principal
def menu_principal():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(EUSE ,(0,0))

        TEXTO_MENU = obtener_fuente(50).render("Epidemic fight", True, "#00000000")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 150))

        BOTON_INICIAR = Button(image=None, pos=(480, 350), text_input="Iniciar", font=obtener_fuente(45), base_color="#00000000", hovering_color="#708090")
        BOTON_SALIR = Button(image=None, pos=(480, 450), text_input="Salir", font=obtener_fuente(45), base_color="#00000000", hovering_color="#708090")

        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        for boton in [BOTON_INICIAR, BOTON_SALIR]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_INICIAR.checkForInput(MOUSE_POS):
                    from niveles import niveles
                    niveles()

                if BOTON_SALIR.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


menu_principal()