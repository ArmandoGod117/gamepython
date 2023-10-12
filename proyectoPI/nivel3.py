import pygame
import random

# Configuraciones
WIDTH = 900
HEIGHT = 600
FPS = 80
PLAYER_SPEED = 3
ENEMY_SPAWN_RATE = 1000  

# Iniciar pygame
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epidemic fight")

# Cargar recursos
background_img = pygame.image.load('img/nivel3.png').convert_alpha()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

player_images = {
    "left": [pygame.image.load('img/walk_left1.png').convert_alpha(), pygame.image.load('img/walk_left2.png').convert_alpha(), pygame.image.load('img/walk_left3.png').convert_alpha(),
            pygame.image.load('img/walk_left4.png').convert_alpha(), pygame.image.load('img/walk_left5.png').convert_alpha(), pygame.image.load('img/walk_left6.png').convert_alpha(),
            pygame.image.load('img/walk_left7.png').convert_alpha(),],
    "right": [pygame.image.load('img/walk_right1.png').convert_alpha(), pygame.image.load('img/walk_right2.png').convert_alpha(), pygame.image.load('img/walk_right3.png').convert_alpha(), 
              pygame.image.load('img/walk_right4.png').convert_alpha(), pygame.image.load('img/walk_right5.png').convert_alpha(), pygame.image.load('img/walk_right6.png').convert_alpha(), 
              pygame.image.load('img/walk_right7.png').convert_alpha()],
}

enemy_img = pygame.image.load('img/viruz.png').convert_alpha()
pygame.mixer.music.load('musica/musicafondo.mp3')
pygame.mixer.music.play(-1)

# Definir clases
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_images["left"][0], (50, 80))
        self.rect = self.image.get_rect(center=(WIDTH // 4, HEIGHT - 120))
        self.speed = PLAYER_SPEED
        self.health = 100
        self.direction = "left"
        self.animation_index = 0
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_delay = 300

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_animation_time > self.animation_delay:
                self.last_animation_time = current_time
                self.animation_index = (self.animation_index + 1) % 7
            self.image = pygame.transform.scale(player_images["left"][self.animation_index], (80, 80))
            self.direction = "left"

    def move_right(self):
        if self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_animation_time > self.animation_delay:
                self.last_animation_time = current_time
                self.animation_index = (self.animation_index + 1) % 7
            self.image = pygame.transform.scale(player_images["right"][self.animation_index], (80, 80))
            self.direction = "right"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 50))
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 50), -50))
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.kill()

# Crear instancias y grupos
player = Player()
enemies = pygame.sprite.Group()

# Bucle principal del juego
clock = pygame.time.Clock()
enemy_spawn_timer = pygame.time.get_ticks()
running = True

initial_time_ms = 3 * 60 * 1000

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    current_time = pygame.time.get_ticks()
    if current_time - enemy_spawn_timer > ENEMY_SPAWN_RATE:
        enemy_spawn_timer = current_time
        enemy = Enemy()
        enemies.add(enemy)

    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        player.take_damage(20)
        if player.health <= 0:
            running = False
            print("GAME OVER")

    window.blit(background_img, (0, 0))
    enemies.update()
    enemies.draw(window)
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

pygame.quit()

