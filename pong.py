#https://www.mclibre.org/consultar/python/lecciones/pygame-pong.html

#importacion de librerias
import pygame
from pygame.locals import *
import sys
import random

# Constantes para la inicialización de la superficie de dibujo
## Dimesiones de la ventana 
# Va en mayuscula porque son varaibles globales que no se cambian
SCREEN_WIDTH = 800 # Ancho de la ventana
SCREEN_HEIGHT = 600 # Alto de la ventana
## Fotogramas por segundo
FPS = 60
## Color del fondo de la ventana (RGB)
SCREEN_BLACK = (0,0,0)


## --- PELOTA --- ##
class PelotaPong:
    # --- Atributos de la Clase --- 
    def __init__(self):
        #Imagen de la Pelota
        self.lado = 10
        self.color = (255,255,255) #color Blanco

        #Posicion de la pelota
        # Punto centro de la pelota
        self.x = SCREEN_WIDTH  // 2
        self.y = SCREEN_HEIGHT // 2

        #Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5,5])
        self.dir_y = random.choice([-5,5])
    
    # -- METODO -- Comportamiento del objeto
    def mover(self):
        self.x = self.dir_x
        self.y = self.dir_y

    # -- METODO -- Dibujo de la pelota
    def dibujar(self,surface):
        pygame.draw.rect(surface, self.color, (int(self.x), int(self.y), self.lado, self.lado))

    # -- METODO -- Rebotar la pelota
    def rebotar(self):
        pass


# Inicialización de Pygame
def main():
    # Inicilización de Pygame
    pygame.init()

    #Inicialización de la superficie de dibujo (display surface)
    window_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Pong from Atari")
    clock = pygame.time.Clock()

    #Creacion pelota
    pelota = PelotaPong()

    #Bucle principal 
    jugando=True
    while jugando:

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
        
        pelota.mover()

        window_surface.fill(SCREEN_BLACK)
        pelota.dibujar(window_surface)

        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()