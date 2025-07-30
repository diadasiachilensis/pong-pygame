#https://www.mclibre.org/consultar/python/lecciones/pygame-pong.html

#importacion de librerias
import pygame
from pygame.locals import *
import sys

# Constantes para la inicialización de la superficie de dibujo
## Dimesiones de la ventana 
# Va en mayuscula porque son varaibles globales que no se cambian
SCREEN_WIDTH = 800 # Ancho de la ventana
SCREEN_HEIGHT = 600 # Alto de la ventana
## Fotogramas por segundo
FPS = 60
## Color del fondo de la ventana (RGB)
WHITE = (255,255,255)

# Inicialización de Pygame
def main():
    # Inicilización de Pygame
    pygame.init()

    #Inicialización de la superficie de dibujo (display surface)
    window_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Pong from Atari")

    #Bucle principal 
    jugando=True
    while jugando:
        window_surface.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    
    pygame.quit()

## --- PELOTA --- ##


if __name__ == "__main__":
    main()