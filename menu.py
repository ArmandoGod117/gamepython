import pygame
import sys
import random

# Inicialización y configuración
pygame.init()
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")
pygame.mixer.music.load('musica/musicafondo.mp3')
volumen = 0.5  # Asume que el volumen inicial es 0.5 (50%)
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

# Carga de imágenes y fuentes
EUSE = pygame.transform.scale(pygame.image.load("img/hospi2.png"), (1000, 700))
ENEMIGO_IMG = pygame.transform.scale(pygame.image.load("img/virus2.png"), (50, 50))
BOTON_INICIAR_IMG = pygame.image.load("img2/play3.png")
BOTON_INICIAR_PRESS_IMG = pygame.transform.scale(pygame.image.load("img2/play3_2.png"), (152, 98))
BOTON_SALIR_IMG = pygame.image.load("img2/btonsalida3.png")
BOTON_SALIR_PRESS_IMG = pygame.transform.scale(pygame.image.load("img2/salir_2.png"), (102, 82))
def obtener_fuente(tamaño):
    return pygame.font.Font("img/Dead Kansas.ttf", tamaño)

def dibujar_barra_volumen(surface, volumen):
    bar_width = 100
    bar_height = 20
    position = (50, 650)
    inner_width = bar_width * volumen
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], bar_width, bar_height), 2)
    pygame.draw.rect(surface, (255, 0, 0), (position[0], position[1], inner_width, bar_height))

class Enemigo:
    def __init__(self):
        self.image = ENEMIGO_IMG
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.velocidad = 15

    def mover(self):
        self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

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

def menu_principal():
    global volumen

    enemigos = []
    contador_enemigos = 0

    BOTON_INICIAR = Button(BOTON_INICIAR_IMG, BOTON_INICIAR_PRESS_IMG, 425, 510)
    BOTON_SALIR = Button(BOTON_SALIR_IMG, BOTON_SALIR_PRESS_IMG, 10, 5)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(EUSE, (0, 0))

        TEXTO_MENU = obtener_fuente(55).render("Epidemic fight", True, "#00000000")
        PANTALLA.blit(TEXTO_MENU, TEXTO_MENU.get_rect(center=(500, 60)))

        BOTON_INICIAR.update(PANTALLA)
        BOTON_SALIR.update(PANTALLA)

        contador_enemigos += 1
        if contador_enemigos >= 100:
            enemigos.append(Enemigo())
            contador_enemigos = 0

        for enemigo in enemigos[:]:
            enemigo.mover()
            enemigo.dibujar(PANTALLA)
            if enemigo.rect.y > 700:
                enemigos.remove(enemigo)

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
                if BOTON_INICIAR.check_for_input(MOUSE_POS):
                    from niveles import niveles1
                    niveles1()
                if BOTON_SALIR.check_for_input(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)

        # Verifica si el mouse está sobre el botón "Salir" y actualiza la imagen
        if BOTON_SALIR.check_for_input(MOUSE_POS):
            BOTON_SALIR.image = BOTON_SALIR_PRESS_IMG
        else:
            BOTON_SALIR.image = BOTON_SALIR_IMG

        if BOTON_INICIAR.check_for_input(MOUSE_POS):
            BOTON_INICIAR.image = BOTON_INICIAR_PRESS_IMG
        else:
            BOTON_INICIAR.image = BOTON_INICIAR_IMG
        
        pygame.display.update()

menu_principal()
