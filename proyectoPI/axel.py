import pygame
import random
import math
import sys
import os

from pygame.locals import *

pygame.init()

#aqui configuras el ancho de la pantalla
Ancho, Alto = 900, 680
screen = pygame.display.set_mode((Ancho, Alto))

# Títulos de juego
pygame.display.set_caption('Fishing Road')
icono = pygame.image.load("img/walk_left1.png")
pygame.display.set_icon(icono)

# Carga de imágenes y música
lago = pygame.image.load("img/nivel1.png").convert_alpha()
lago = pygame.transform.scale(lago, (900, 680))

pygame.mixer.music.load('musica/musicafondo.mp3')
pygame.mixer.music.play(-1)

# Jugador
jugadors = pygame.image.load('img/walk_left2.png').convert_alpha()

# Bucle del juego principal
def gameloop():
    jugadorX = 50
    jugadorY = 50
    jugadorx_change = 0
    
    # Puntuación
    score = 0
    myfont = pygame.font.Font(None, 32)  # Utilizando una fuente predeterminada

    # Basura
    basuras_img = pygame.image.load('img/viruz.png').convert_alpha()
    basuras = []
    for i in range(10):  # Crear 10 basuras
        basuras.append({
            'x': random.randint(0, 736),
            'y': random.randint(0, 150),
            'x_change': 5,
            'y_change': 20,
            'img': basuras_img
        })
#inicio de bucle
    running = True
    while running:
        screen.blit(lago, (0, 0))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugadorx_change = -5
                elif event.key == pygame.K_RIGHT:
                    jugadorx_change = 5
            elif event.type == pygame.KEYUP:
                jugadorx_change = 0

        # Mover jugador
        jugadorX += jugadorx_change
        jugadorX = max(0, min(jugadorX, 736))  # Asegurate de que el jugador no salga de la pantalla
        
        # Mostrar jugador
        screen.blit(jugadors, (jugadorX, jugadorY))

        # Mostrar y mover basuras
        for basura in basuras:
            screen.blit(basura['img'], (basura['x'], basura['y']))
            basura['x'] += basura['x_change']
            basura['y'] += basura['y_change']
            
            # Si la basura sale de la pantalla, reinicia su posición
            if basura['y'] > Alto:
                basura['y'] = 0
                basura['x'] = random.randint(0, 736)

        # Mostrar puntuación
        score_value = myfont.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))

        pygame.display.update()
        pygame.time.Clock().tick(120)  #aqui estan los fotogramas

# Ejecutar el bucle de juego
gameloop()
pygame.quit()
