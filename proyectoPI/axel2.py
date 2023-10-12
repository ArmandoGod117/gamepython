import pygame
import random
import math
import sys
import os

from pygame.locals import *


pygame.init()



Ancho, Alto = 900, 680

screen = pygame.display.set_mode((Ancho, Alto))




def resource_path(relative_path):

    try:

        base_path = sys._MEIPASS

    except Exception:

        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pygame.display.set_caption('Fishing Road')

icono = pygame.image.load("img/walk_left1.png")
pygame.display.set_icon(icono)

lago = pygame.image.load("img/nivel1.png")

lago = pygame.transform.scale(lago, (900, 680))
screen.blit(lago, (0, 0))



musica = resource_path('musica/musicafondo.mp3')

musica = pygame.mixer.music.load(musica)


jugador_a = resource_path('img/walk_left2.png')

jugadors = pygame.image.load(jugador_a)



puntaje_a = resource_path('img/viruz.png')



pygame.mixer.music.play(-1)


clock = pygame.time.Clock()



jugadorX = 370

jugadorY = 470

jugadorx_change = 0


basuras = []

basuraX = []

basuraY = []

basuraX_change = []

basuraY_change = []

no_of_basura = 10


for i in range(no_of_basura):

    basura1 = resource_path('img/viruz.png')

    basuras.append(pygame.image.load(basura1))

    basuraX.append(random.randint(0, 736))

    basuraY.append(random.randint(0, 150))

    basuraX_change.append(5)

    basuraY_change.append(20)



cañaX = 0

cañaY = 480

cañaX_change = 0

cañaY_change = 10

caña_state = "ready"

score = 0



# Funciones

def show_score():

  try:
    myfont = pygame.font.Font(puntaje_a, 32)
except IOError:
    print(f"Cannot load font: {puntaje_a}")
    # Utiliza una fuente predeterminada en lugar de salir del juego
    myfont = pygame.font.Font(None, 32)

    screen.blit(score_value, (10, 10))



def jugador(x, y):

    screen.blit(jugadors, (x, y))



def basura(x, y, i):

    screen.blit(basuras[i], (x, y))



def caña_hilo(x, y):

    global caña_state

    caña_state = "bajar"

    # Necesitamos una imagen para caña

    # screen.blit(caña, (x + 16, y + 10))



def colision(basuraX, basuraY, cañaX, cañaY):

    distance = math.sqrt((math.pow(basuraX - cañaX, 2)) +

                         (math.pow(basuraY - cañaY, 2)))

    return distance < 27



# Función principal del juego

def gameloop():

    global score, jugadorX, jugadorx_change, cañaX, cañaY, caña_state


    in_game = True

    while in_game:

        screen.fill((0, 0, 0))
        screen.blit(lago, (0, 0))


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                in_game = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    jugadorx_change = -5

                elif event.key == pygame.K_RIGHT:

                    jugadorx_change = 5

                elif event.key == pygame.K_SPACE and caña_state == "ready":

                    cañaX = jugadorX

                    caña_hilo(cañaX, cañaY)

            elif event.type == pygame.KEYUP:

                jugadorx_change = 0


        jugadorX += jugadorx_change


        if jugadorX <= 0:

            jugadorX = 0

        elif jugadorX >= 736:

            jugadorX = 736


        for i in range(no_of_basura):

            if basuraY[i] > 440:

                for j in range(no_of_basura):

                    basuraY[j] = 2000

            #... Resto del código de movimiento de basuras


        jugador(jugadorX, jugadorY)

        show_score()

        pygame.display.update()


        clock.tick(120)


gameloop()

