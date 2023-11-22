import pygame
import sys
import random

#Variables
#tamaño de la ventama
WIDTH = 1000
HEIGHT = 700

#Velocidad del juego
FPS = 60
#velocidad del jugador
PLAYER_SPEED = 3
#cantidad de medicina y enemigos que spawnean
ENEMY_SPEED_RATE = 1000
MEDICINE_SPAWN_RATE = 5000

#inicio de pygame y de la musica
pygame.init()
pygame.init()
pygame.mixer.init()

#importacion de imagenes
icon = pygame.image.load("img/virus2.png")
life = pygame.image.load("img2/life.png")
sound = pygame.image.load("img2/volumen.png")
mute= pygame.image.load("img2/mute.png")
time = pygame.image.load("img2/tiempo.png")

#mostrar ventana, nombre de la ventana y icono
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epidemic fight")
pygame.display.set_icon(icon)

#importar musica, volumen de la musica y repeticion
pygame.mixer.music.load('musica/nivel1.mp3')
volumen = 0.5
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

#fuente y tamaño del texto
font = pygame.font.SysFont(None, 25)
font_sound = pygame.font.SysFont(None, 15)

#ubicacion del fondo al quitar la pausa
background_x = 0

# Estado de la pausa
paused = False
# Variables para controlar la barra de sonido
mostrar_barra = False
tiempo_mostrar_barra = 0

#barra de volumen 
def dibujar_barra_volumen(surface, volumen):
    #ubicacion de la imagen de estado del volumen
    ubi_sound = (970, 270)
    if volumen>=0.1:
        window.blit(sound, ubi_sound)
    else:
        window.blit(mute, ubi_sound)

    #ubicacion de la barra de sonido
    bar_width = 20
    bar_height = 100
    position = (970, 300)
    inner_height = bar_height * volumen
    inner_position = (position[0], position[1] + (bar_height - inner_height))

    #como se dibuja la barra de sonido
    pygame.draw.rect(surface, (255, 255, 255), (position[0]-3, position[1], bar_width+6, bar_height), 0, border_radius=10)
    pygame.draw.rect(surface, (0, 0, 255), (inner_position[0]-3, inner_position[1], bar_width+6, inner_height), 0, border_radius=10)

    # Mostrar porcentaje del volumen
    percentage_text = font_sound.render(f"{int(volumen * 100)}%", True, (0, 0, 0))
    text_rect = percentage_text.get_rect(center=(position[0] + bar_width // 2, position[1] + bar_height // 2))
    surface.blit(percentage_text, text_rect)

    
def load_pause_image():
    #se importa la imagen de pausa y se escala
    pause_image = pygame.image.load("img2/pausaverde1.png").convert_alpha()
    pause_image = pygame.transform.scale(pause_image, (WIDTH, HEIGHT))

    #ubicacion en la que se mostrara la imagen
    new_width = WIDTH // 2
    new_height = HEIGHT // 2
    pause_image = pygame.transform.scale(pause_image, (new_width, new_height))
    return pause_image

pause_img = load_pause_image()

def load_unpaused_image():
    unpause_image = pygame.image.load("img2/pausaverde.png").convert_alpha()
    unpause_image = pygame.transform.scale(unpause_image, (WIDTH // 10, HEIGHT // 10))
    return unpause_image

unpause_img = load_unpaused_image()

#funcion para pausar el juego
def pause(window, player, enemies, background_img, background_x):
    global paused, volumen, mostrar_barra, tiempo_mostrar_barra
    paused = True
    pause_img_rect = pause_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(pause_img, pause_img_rect)
    pygame.display.flip()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    window.blit(background_img, (background_x, 0))
                    enemies.draw(window)
                    window.blit(player.image, player.rect)
                    unpause_img_rect = unpause_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    window.blit(unpause_img, unpause_img_rect)
                    pygame.display.flip()
                    pygame.time.wait(1000)

                elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                    if event.key == pygame.K_UP:
                        volumen += 0.1
                        if volumen > 1:
                            volumen = 1
                    elif event.key == pygame.K_DOWN:
                        volumen -= 0.1
                        if volumen < 0:
                            volumen = 0
                    pygame.mixer.music.set_volume(volumen)

                    # Mostrar la barra de volumen y actualizar el tiempo
                    mostrar_barra = True

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dibujar_barra_volumen(window, volumen)
        pygame.display.flip()

def load_image(path):
    pygame.init()
    image =pygame.image.load(path).convert_alpha()
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self, player_images):
        super().__init__()
        self.image = pygame.transform.scale(player_images["right"][0], (60, 90))
        self.rect = self.image.get_rect(center=(WIDTH // 1.9, HEIGHT - 155))
        self.speed = PLAYER_SPEED
        self.health = 100
        self.direction = "right"
        self.animation_index = 0
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_delay = 50
        self.player_images = player_images

    def move_left(self):
        self.rect.x -= self.speed
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.animation_delay:
            self.last_animation_time = current_time
            self.animation_index = (self.animation_index + 1) % 7
        self.image = pygame.transform.scale(self.player_images["left"][self.animation_index], (60, 90))
        self.direction = "left"

    def move_right(self):
        self.rect.x += self.speed
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.animation_delay:
            self.last_animation_time = current_time
            self.animation_index = (self.animation_index + 1) % 7
        self.image = pygame.transform.scale(self.player_images["right"][self.animation_index], (60, 90))
        self.direction = "right"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def draw_health_bar(self, surface):
        bar_width = 100
        bar_height = 20
        health_bar_position = (35, 10)

        pygame.draw.rect(surface, (255, 0, 0), (*health_bar_position, bar_width, bar_height), 0, border_radius=20)
        pygame.draw.rect(surface, (0, 255, 0), (*health_bar_position, int((self.health / 100.0) * bar_width), bar_height), 0, border_radius=20)

        # Mostrar porcentaje de vida sobre la barra
        font = pygame.font.SysFont(None, 25)
        percentage_text = font.render(f"{int(self.health)}%", True, (255, 255, 255))
        text_rect = percentage_text.get_rect(center=(health_bar_position[0] + bar_width // 2, health_bar_position[1] + bar_height // 2))
        surface.blit(percentage_text, text_rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 50))
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 50), -50))
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.kill()

class Medicine(pygame.sprite.Sprite):
    def __init__(self, medicine_img):
        super().__init__()
        self.image = pygame.transform.scale(medicine_img, (70, 70))
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 30), -30))
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.kill()

def load_level_2_images():
    background_img = load_image('img/nivel2angel.png')
    player_images = {
        "left": [load_image(f'img/walk_left1{i}.png') for i in range(1, 8)],
        "right": [load_image(f'img/walk_right1{i}.png') for i in range(1, 8)],
    }
    enemy_img = load_image('img/virus2.png')
    medicine_img = load_image('img2/cubrebocas2.png')
    return background_img, player_images, enemy_img, medicine_img

def nivel_2():
    global paused, volumen, mostrar_barra, tiempo_mostrar_barra

    #importacion de imagenes
    player_images = {
        "left": [load_image(f'img/walk_left{i}.png') for i in range(1, 8)],
        "right": [load_image(f'img/walk_right{i}.png') for i in range(1, 8)],
    }
    background_img = load_image('img/nivel2angel.png')
    enemy_img = load_image('img/virus2.png')
    medicine_img = load_image('img2/cubrebocas2.png')
    player = Player(player_images)
    
    enemies = pygame.sprite.Group()
    medicines = pygame.sprite.Group()
    clock = pygame.time.Clock()
    enemy_spawn_timer = pygame.time.get_ticks()
    medicine_spawn_timer = pygame.time.get_ticks()

    #tiempo el juego en segundos
    time_left = 121

    #estado del juego
    running = True

    while running:
        clock.tick(FPS)
        #hace que al presionar salir se cierre la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #hace que el juego se pause cuando se presiona la tecla espacio
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = pause(window, player, enemies, background_img, background_x)
                
                #sube el volumen cuando se presiona la tecla hacia arriba y hace que se muestre la barra de volumen
                if event.key == pygame.K_UP:
                    volumen += 0.1
                    if volumen > 1:
                        volumen = 1
                    pygame.mixer.music.set_volume(volumen)
                    mostrar_barra = True
                    tiempo_mostrar_barra = pygame.time.get_ticks()

                #baja el volumen cuando se presiona la tecla abajo y hace que se muestre la barra de volumen
                elif event.key == pygame.K_DOWN:
                    volumen -= 0.1
                    if volumen < 0:
                        volumen = 0
                    pygame.mixer.music.set_volume(volumen)
                    mostrar_barra = True
                    tiempo_mostrar_barra = pygame.time.get_ticks()

        #que hacer en caso de que la pausa no este activa
        if not paused:
            time_left -= 1 / FPS
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.rect.x > 0:
                player.move_left()
            if keys[pygame.K_RIGHT] and player.rect.x < WIDTH - player.rect.width:
                player.move_right()

            current_time = pygame.time.get_ticks()
            if current_time - enemy_spawn_timer > ENEMY_SPEED_RATE:
                enemy_spawn_timer = current_time
                enemies.add(Enemy(enemy_img))

            if player.health < 100 and current_time - medicine_spawn_timer > MEDICINE_SPAWN_RATE:
                medicine_spawn_timer = current_time
                medicines.add(Medicine(medicine_img))

            hits = pygame.sprite.spritecollide(player, enemies, True)
            for hit in hits:
                player.take_damage(20)


            medicine_hits = pygame.sprite.spritecollide(player, medicines, True)
            for medicine in medicine_hits:
                player.health += 10
                player.health = min(player.health, 100)

            #convierte los 120 segundos a minutos y segundos
            minutes = int(time_left // 60)
            seconds = int(time_left % 60)
            #como se debe ver el tiempo en pantalla
            timer_text = font.render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))

            #actualiza la posicion de los objetos que caen 
            enemies.update()
            medicines.update()

        #muestra la imagen de pausa si el juego esta pausado
        else:
            window.blit(pause_img, (0, 0))

        #dibuja el fondo
        window.blit(background_img, (0, 0))

        # Dibujar enemigos y medicinas
        enemies.draw(window)
        medicines.draw(window)
        window.blit(player.image, player.rect)


        # Dibujar la imagen life y la barra de vida
        life_position = (0, 0)
        window.blit(life, life_position)
        player.draw_health_bar(window)

        #dibujar la imagen del reloj y el cronometro
        window.blit(timer_text, (WIDTH - 50, 10))
        time_position=(915,5)
        window.blit(time, time_position)

        #muestra la barra de sonido por 5 segundos
        if mostrar_barra:
            dibujar_barra_volumen(window, volumen)
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_mostrar_barra > 5000:
                mostrar_barra = False

        #muestra la pantalla winner o gameover
        pygame.display.flip()
        if time_left <= 1:
            from winner2 import winner_2
            winner_2()
        elif player.health <= 0:
            from gameover2 import gameover_2
            gameover_2()
            running = False

    pygame.quit()

nivel_2()