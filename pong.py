#https://www.mclibre.org/consultar/python/lecciones/pygame-pong.html

#importacion de librerias
import pygame
from pygame.locals import QUIT
import sys

# Constantes para la inicialización de la superficie de dibujo
## Dimesiones de la ventana 
screen_width = 800 # Ancho de la ventana
screen_height = 600 # Alto de la ventana
## Fotogramas por segundo
FPS = 60
## Color del fondo de la ventana (RGB)
white = (255,255,255)

# Inicialización de Pygame
def main():
    # Inicilización de Pygame
    pygame.init()

    #Inicialización de la superficie de dibujo (display surface)
    window_surface = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Pong from Atari")

    #Bucle principal 
    jugando=True
    while jugando:
        window_surface.fill(white)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()