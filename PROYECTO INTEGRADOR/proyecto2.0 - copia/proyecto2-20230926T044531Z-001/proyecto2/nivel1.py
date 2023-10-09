import pygame
import random

# Configuraciones
WIDTH = 1000
HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
ENEMY_SPAWN_RATE = 1000

def koka():
    # Iniciar pygame
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Eusebio vs el Virus del Mal")

    # Cargar recursos
    def load_image(path):
        image = pygame.image.load(path).convert_alpha()
        return image

    background_img = load_image('img/nivel1.png')
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

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
            if self.rect.x > 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_animation_time > self.animation_delay:
                    self.last_animation_time = current_time
                    self.animation_index = (self.animation_index + 1) % 7
                self.image = pygame.transform.scale(player_images["left"][self.animation_index], (60, 90))
                self.direction = "left"

        def move_right(self):
            if self.rect.x < WIDTH - self.rect.width:
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

    # Crear instancias y grupos
    player = Player()
    enemies = pygame.sprite.Group()

    # Bucle principal del juego
    clock = pygame.time.Clock()
    enemy_spawn_timer = pygame.time.get_ticks()
    running = True

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
            player.take_damage(25)
            if player.health <= 0:
                running = False
                from gameover1 import niveles1
                niveles1()
                pygame.quit()
   
        window.blit(background_img, (0, 0))
        enemies.update()
        enemies.draw(window)
        window.blit(player.image, player.rect)

        pygame.draw.rect(window, (255, 0, 0), (10, 10, 100, 20))
        pygame.draw.rect(window, (0, 255, 0), (10, 10, player.health, 20))

        elapsed_time = pygame.time.get_ticks() // 1500
        font = pygame.font.SysFont(None, 25)
        timer_text = font.render(f"Tiempo: {elapsed_time}", True, (255, 255, 255))
        window.blit(timer_text, (WIDTH - 100, 10))

        pygame.display.flip()

    pygame.quit()
koka()