import pygame
import sys
from botones import Button

# Inicialización de pygame
pygame.init()


# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Eusebio vs el Virus del Mal")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/niveles.png"), (1000, 700))

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
        PANTALLA.blit(EUSE,(0,0))

        TEXTO_MENU = obtener_fuente(60).render("Epidemic fight", True, "#DDFC42")
        RECTANGULO_TEXTO_MENU = TEXTO_MENU.get_rect(center=(500, 60))

        NIVEL1 = Button(image=None, pos=(750, 200), text_input="Nivel 1", font=obtener_fuente(30), base_color="#000000", hovering_color="#5F9EA0")
        NIVEL2 = Button(image=None, pos=(750, 280), text_input= "Nivel 2", font=obtener_fuente(30), base_color="#000000", hovering_color="#5F9EA0")
        NIVEL3 = Button(image=None, pos=(750, 360), text_input="Nivel 3", font=obtener_fuente(30), base_color="#000000", hovering_color="#5F9EA0")
        BOTON_SALIR = Button(image=None, pos=(80, 50), text_input="Salir", font=obtener_fuente(35), base_color="#000000", hovering_color="#DC143C")
        HISTORIA = Button(image=None, pos=(900, 450), text_input="HISTORIA", font=obtener_fuente(30), base_color="#000000", hovering_color="#DC143C")

        PANTALLA.blit(TEXTO_MENU, RECTANGULO_TEXTO_MENU)

        for boton in [NIVEL1, NIVEL2,NIVEL3, BOTON_SALIR, HISTORIA]:
            boton.changeColor(MOUSE_POS)
            boton.update(PANTALLA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL1.checkForInput(MOUSE_POS):
                    import nivel1
                    nivel1()

                if NIVEL2.checkForInput(MOUSE_POS):
                    import nivel2
                    nivel2()

                if NIVEL3.checkForInput(MOUSE_POS):
                    import nivel3
                    nivel3()

                if HISTORIA.checkForInput(MOUSE_POS):
                    import historia
                    historia()   

                if BOTON_SALIR.checkForInput(MOUSE_POS):
                    from menu import menu_principal
                    menu_principal()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

niveles()