import pygame

class Button:

    def __init__(self, surface, rect, active_surface):
        self.surface = surface
        self.rect = rect
        self.active_surface = active_surface

    def create(self):
        return self.surface

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    pause_button = Button(
        pygame.image.load("img/pausa2.png"),
        pygame.Rect((50, 50), (50, 50)),
        pygame.image.load("img/pausa.png")
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.is_clicked(event.pos):
                    pause()

        screen.fill((0, 0, 0))
        pause_button.draw(screen)
        pygame.display.flip()

    pygame.quit()


def pause():
    global running
    running = False


if __name__ == "__main__":
    main()