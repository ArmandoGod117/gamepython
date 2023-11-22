import cv2
import pygame
import sys
from botones import Button  # Asegúrate de tener el archivo botones.py en tu directorio

def historia1():
    video = cv2.VideoCapture("img/historia1.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window_size = (1000, 700)
    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    background_color = (0, 0, 255)

    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

        success, video_image = video.read()
        if success:
            x = (window_size[0] - video_image.shape[1]) // 2
            y = (window_size[1] - video_image.shape[0]) // 2

            window.fill(background_color)
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
            window.blit(video_surf, (x, y))
            pygame.display.flip()
        else:
            run = False

    video.release()
    pygame.quit()

    return not run

def main():
    pygame.init()

    video_reproducido_completamente = historia1()

    if video_reproducido_completamente:
        from historia import historia_1
        historia_1()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
