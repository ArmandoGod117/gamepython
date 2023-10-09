import pygame
import json


# Cargar imágenes
BG = pygame.transform.scale(pygame.image.load("img/nivel1.png"), (1280, 720))
OPCION = pygame.transform.scale(pygame.image.load("img/nivel1.png"), (1280, 720))
IDIOMA = pygame.transform.scale(pygame.image.load("img/nivel1.png"),(1280, 720))
VOLUMENB = pygame.transform.scale(pygame.image.load("img/nivel1.png"), (1280, 720))
CREADOR = pygame.transform.scale(pygame.image.load("img/nivel1.png"), (1280, 720))

# Configuración inicial de volumen
volumen = 0.5
pygame.mixer.init()
pygame.mixer.music.set_volume(volumen)
musica = pygame.mixer.music.load("musica/nivel1.mp3")
pygame.mixer.music.play()

# Función para obtener una fuente
def get_font(size):
    return pygame.font.Font("assets/AlumniSansInlineOne-Italic.ttf", size)

# Función para cargar el idioma desde un archivo JSON
def cargar_idioma(idioma):
    idioma_actual = {}
    idioma_file = f"idiomas/{idioma}.txt"
    with open(idioma_file, "r", encoding="utf-8") as file:
        idioma_actual = json.load(file)
    return idioma_actual

# Función para cambiar el idioma
def cambiar_idioma(nuevo_idioma):
    global idioma_actual
    idioma_actual = cargar_idioma(nuevo_idioma)

# Variable global para almacenar el idioma actual
idioma_actual = cargar_idioma("espanol")

cambio_idioma_realizado = False  # Variable para rastrear si se ha realizado un cambio de idioma