import cv2
import pygame
import sys
from botones import Button  # Asegúrate de tener el archivo botones.py en tu directorio

# Inicializa la variable global
window_opened = False

def historia2():
    global window_opened

    # Verifica si la ventana ya se ha abierto antes
    if window_opened:
        return False

    window_opened = True

    video = cv2.VideoCapture("img/historia2.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window_size = (1000, 700)
    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()
    background_color = (0, 0, 255)

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

    pygame.quit()
    
    # Restablece la variable al finalizar
    window_opened = False
    
    # Devolver True si el video se reprodujo completamente, False de lo contrario
    return not run

def main():
    pygame.init()

    # Lógica para la pantalla anterior
    # ...

    # Llamar a la función que reproduce el video
    video_reproducido_completamente = historia2()

    # Lógica para volver a la pantalla anterior después de que termina el video
    if video_reproducido_completamente:
        # Aquí puedes poner el código para volver a la pantalla anterior
        from historia import historia_1
        historia_1()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
