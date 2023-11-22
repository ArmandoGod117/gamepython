import pygame
import sys

# Inicialización de pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Epidemic fight")

# Carga de imágenes
EUSE = pygame.transform.scale(pygame.image.load("img/fondomenu.png"), (1000, 700))

#configuraciones de la musica
pygame.mixer.music.load('musica/musicafondo.mp3')
volumen = 0.5  # Asume que el volumen inicial es 0.5 (50%)
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

# Cargar imágenes de botones
IMG_SALIR = pygame.transform.scale(pygame.image.load("img2/btonrojo.png"), (100, 80))
IMG_SALIR_PRESS = pygame.transform.scale(pygame.image.load("img2/botonrojo_2.png"), (102, 82))
IMG_HISTORIA1 = pygame.transform.scale(pygame.image.load("img2/btonhistoria1.png"), (145, 85))
IMG_HISTORIA1_PRESS = pygame.transform.scale(pygame.image.load("img2/boton_1.png"), (147, 87))
IMG_HISTORIA2 = pygame.transform.scale(pygame.image.load("img2/btonhistoria2.png"), (145, 85))
IMG_HISTORIA2_PRESS = pygame.transform.scale(pygame.image.load("img2/boton_2.png"), (147, 87))
IMG_HISTORIA3 = pygame.transform.scale(pygame.image.load("img2/btonhistoria3.png"), (145, 85))
IMG_HISTORIA3_PRESS = pygame.transform.scale(pygame.image.load("img2/boton_3.png"), (147, 87))
IMG_HISTORIA4 = pygame.transform.scale(pygame.image.load("img2/btonhistoria4.png"), (145, 85))
IMG_HISTORIA4_PRESS = pygame.transform.scale(pygame.image.load("img2/btonhistoria_4.png"), (147, 87))

def dibujar_barra_volumen(surface, volumen):
    bar_width = 100
    bar_height = 20
    position = (50, 650)
    inner_width = bar_width * volumen
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], bar_width, bar_height), 2)
    pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1], inner_width, bar_height))

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

def historia_1():
    global volumen

    BOTON_SALIR = Button(IMG_SALIR, IMG_SALIR_PRESS, 80, 50)
    HISTORIA1 = Button(IMG_HISTORIA1, IMG_HISTORIA1_PRESS, 425, 80)
    HISTORIA2 = Button(IMG_HISTORIA2, IMG_HISTORIA2_PRESS, 425, 230)
    HISTORIA3 = Button(IMG_HISTORIA3, IMG_HISTORIA3_PRESS, 425, 380)
    HISTORIA4 = Button(IMG_HISTORIA4, IMG_HISTORIA4_PRESS, 425, 530)
        

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(EUSE, (0, 0))

        BOTON_SALIR.update(PANTALLA)
        HISTORIA1.update(PANTALLA)
        HISTORIA2.update(PANTALLA)
        HISTORIA3.update(PANTALLA)
        HISTORIA4.update(PANTALLA)

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
                if HISTORIA1.check_for_input(MOUSE_POS):
                    from historia1 import main
                    main()
                if HISTORIA2.check_for_input(MOUSE_POS):
                    from historia2 import main
                    main()
                if HISTORIA3.check_for_input(MOUSE_POS):
                    from historia3 import main
                    main()
                if HISTORIA4.check_for_input(MOUSE_POS):
                    from historia4 import main
                    main()
                
                elif BOTON_SALIR.check_for_input(MOUSE_POS):
                    from niveles import niveles1
                    niveles1()
                    pygame.quit()
                    sys.exit()

        # Dibuja la barra de volumen
        dibujar_barra_volumen(PANTALLA, volumen)

        if BOTON_SALIR.check_for_input(MOUSE_POS):
            BOTON_SALIR.image = IMG_SALIR_PRESS
        else:
            BOTON_SALIR.image = IMG_SALIR

        if HISTORIA1.check_for_input(MOUSE_POS):
            HISTORIA1.image = IMG_HISTORIA1_PRESS
        else:
            HISTORIA1.image = IMG_HISTORIA1

        if HISTORIA2.check_for_input(MOUSE_POS):
            HISTORIA2.image = IMG_HISTORIA2_PRESS
        else:
            HISTORIA2.image = IMG_HISTORIA2
        
        if HISTORIA3.check_for_input(MOUSE_POS):
            HISTORIA3.image = IMG_HISTORIA3_PRESS
        else:
            HISTORIA3.image = IMG_HISTORIA3

        if HISTORIA4.check_for_input(MOUSE_POS):
            HISTORIA4.image = IMG_HISTORIA4_PRESS
        else:
            HISTORIA4.image = IMG_HISTORIA4

        pygame.display.update()

historia_1()
