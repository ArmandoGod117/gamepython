import pygame
import random

# Configuraciones
WIDTH = 1000
HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
ENEMY_SPAWN_RATE = 900

def koka():
    # Iniciar pygame
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Epidemic fight")

    # Cargar recursos
    def load_image(path):
        image = pygame.image.load(path).convert_alpha()
        return image

    background_img = load_image('img/nivel1.png')
    background_img = pygame.transform.scale(background_img, (2 * WIDTH, HEIGHT))
    background_x = 0

    player_images = {
        "left": [load_image(f'img/walk_left{i}.png') for i in range(1, 8)],
        "right": [load_image(f'img/walk_right{i}.png') for i in range(1, 8)],
    }

    enemy_img = load_image('img/viruz.png')

    pygame.mixer.music.load('musica/musicafondo.mp3')
    pygame.mixer.music.play(-1)

    # Clase Player
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(player_images["right"][0], (20, 50))
            self.rect = self.image.get_rect(center=(WIDTH // 3.5, HEIGHT - 140))
            self.speed = PLAYER_SPEED
            self.health = 100
            self.direction = "right"
            self.animation_index = 0
            self.last_animation_time = pygame.time.get_ticks()
            self.animation_delay = 50

        def move_left(self):
            nonlocal background_x
            if self.rect.x <= WIDTH // 3 and background_x < 0:
                background_x += self.speed
            elif self.rect.x > 0:
                self.rect.x -= self.speed

            current_time = pygame.time.get_ticks()
            if current_time - self.last_animation_time > self.animation_delay:
                self.last_animation_time = current_time
                self.animation_index = (self.animation_index + 1) % 7
            self.image = pygame.transform.scale(player_images["left"][self.animation_index], (60, 90))
            self.direction = "left"

        def move_right(self):
            nonlocal background_x
            if self.rect.x >= (2 * WIDTH) // 3 and background_x > -(background_img.get_width() - WIDTH):
                background_x -= self.speed
            elif self.rect.x < WIDTH - self.rect.width:
                self.rect.x += self.speed

            current_time = pygame.time.get_ticks()
            if current_time - self.last_animation_time > self.animation_delay:
                self.last_animation_time = current_time
                self.animation_index = (self.animation_index + 1) % 7
            self.image = pygame.transform.scale(player_images["right"][self.animation_index], (60, 90))
            self.direction = "right"

        def take_damage(self, damage):
            self.health -= damage
            if self.health < 0:
                self.health = 0

    # Clase Enemy
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

    player = Player()
    enemies = pygame.sprite.Group()

    # Bucle principal del juego
    clock = pygame.time.Clock()
    enemy_spawn_timer = pygame.time.get_ticks()
    running = True

    initial_time_ms = 2 * 60 * 1000 

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
                from gameover1 import niveles1
                niveles1()
                pygame.quit()

        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.take_damage(25)
            if player.health >= 20:
                from winner1 import niveles1
                niveles1()
                pygame.quit()

        window.blit(background_img, (background_x, 0))
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

koka()