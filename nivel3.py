import pygame
import random

# Configuraciones
WIDTH = 1000
HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
ENEMY_SPAWN_RATE = 1000
MEDICINE_SPAWN_RATE = 5000
BACKGROUND_SPEED = 1  # Velocidad de movimiento del fondo

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epidemic fight")

# Cargar imagen de pausa
def load_pause_image():
    pause_image = pygame.image.load('img2/pausa.png').convert_alpha()  
    pause_image = pygame.transform.scale(pause_image, (WIDTH, HEIGHT))  

    new_width = WIDTH // 2
    new_height = HEIGHT // 2
    
    pause_image = pygame.transform.scale(pause_image, (new_width, new_height))
    
    return pause_image

pause_img = load_pause_image()

# Cargar imagen de despausado
def load_unpause_image():
    unpause_image = pygame.image.load('img2/pausaverde.png').convert_alpha()
    unpause_image = pygame.transform.scale(unpause_image, (WIDTH // 10, HEIGHT // 10))  
    return unpause_image

unpause_img = load_unpause_image()

def pause(window, clock, player, enemies, background_img, background_x):
    paused = True
    pause_img_rect = pause_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  
    window.blit(pause_img, pause_img_rect)  
    pygame.display.flip()  
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    # Muestra la imagen de despausado por un breve momento al salir de la pausa
                    window.blit(background_img, (background_x, 0))  
                    enemies.draw(window)  # Redibuja los enemigos
                    window.blit(player.image, player.rect)  # Redibuja el jugador
                    unpause_img_rect = unpause_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    window.blit(unpause_img, unpause_img_rect)
                    pygame.display.flip()
                    pygame.time.wait(1000)  # Pausa el juego por 1 segundo, ajusta este tiempo como prefieras

                    # Redibujar la pantalla completa con todos los elementos del juego después de la imagen de despausado
                    window.blit(background_img, (background_x, 0))
                    player.update()
                    enemies.update()
                    window.blit(player.image, player.rect)
                    enemies.draw(window)
                    # ... Redibuja cualquier otro elemento de la interfaz aquí ...

                    pygame.display.flip()  # Actualiza la pantalla completa
                    clock.tick(1)  # Pausa el juego brevemente antes de continuar

            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Cargar recursos
def load_image(path):
    image = pygame.image.load(path).convert_alpha()
    return image

# Clase Player
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

# Clase Enemy
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

# Clase Medicine
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

def nivel_2():
    pygame.mixer.music.load('musica/nivel1.mp3')
    pygame.mixer.music.play(-1)

    background_img = load_image('img/nivel3angel.png')
    
    background_x = 0

    player_images = {
        "left": [load_image(f'img/walk_left{i}.png') for i in range(1, 8)],
        "right": [load_image(f'img/walk_right{i}.png') for i in range(1, 8)],
    }

    enemy_img = load_image('img/viru3.png')
    medicine_img = load_image('img2/naranja.png')

    player = Player(player_images)
    enemies = pygame.sprite.Group()
    medicines = pygame.sprite.Group()

    clock = pygame.time.Clock()
    enemy_spawn_timer = pygame.time.get_ticks()
    medicine_spawn_timer = pygame.time.get_ticks()
    running = True
    initial_time_ms = 2 * 60 * 1000

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause(window, clock, player, enemies, background_img, background_x)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            player.move_left()
        if keys[pygame.K_RIGHT] and player.rect.x < WIDTH - player.rect.width:
            player.move_right()

        current_time = pygame.time.get_ticks()
        if current_time - enemy_spawn_timer > ENEMY_SPAWN_RATE:
            enemy_spawn_timer = current_time
            enemies.add(Enemy(enemy_img))

        if player.health < 100 and current_time - medicine_spawn_timer > MEDICINE_SPAWN_RATE:
            medicine_spawn_timer = current_time
            medicines.add(Medicine(medicine_img))

        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.take_damage(20)
            if player.health <= 0:
                from gameover1 import gameover_1
                gameover_1()
                running = False

        medicine_hits = pygame.sprite.spritecollide(player, medicines, True)
        for medicine in medicine_hits:
            player.health += 10
            player.health = min(player.health, 100)

        

        window.blit(background_img, (background_x, 0))
        window.blit(background_img, (background_x + WIDTH, 0))

        enemies.update()
        medicines.update()

        enemies.draw(window)
        medicines.draw(window)
        window.blit(player.image, player.rect)

        pygame.draw.rect(window, (255, 0, 0), (10, 10, 100, 20))
        pygame.draw.rect(window, (0, 255, 0), (10, 10, player.health, 20))

        elapsed_time_ms = pygame.time.get_ticks()
        remaining_time_ms = initial_time_ms - elapsed_time_ms
        remaining_time_ms = max(remaining_time_ms, 0)
        remaining_seconds = remaining_time_ms // 1000
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        font = pygame.font.SysFont(None, 25)
        timer_text = font.render(f"Tiempo: {str(minutes).zfill(2)}:{str(seconds).zfill(2)}", True, (255, 255, 255))
        window.blit(timer_text, (WIDTH - 120, 10))

        pygame.display.flip()

        if remaining_time_ms == 0:
            if player.health >= 20:
                from winner1 import winner_1
                winner_1()
                initial_time_ms = 2 * 60 * 1000
            else:
                from gameover1 import gameover_1
                gameover_1()
                running = False

    pygame.quit()

nivel_2()