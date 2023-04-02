#Dibujar las nubes en la pantalla.
import pygame
import random
from dino_runner.utils.constants import CLOUD, SCREEN_HEIGHT, SCREEN_WIDTH

class Clouds:
    #Hacer las contantes Y y X que se pondra los limites de donde pueden aparecer las nubes.
    Y_POS = [0,310]
    X_POS = [SCREEN_WIDTH]
    VEL = 5
    def __init__(self):
        self.img = CLOUD
        self.x_pos = self.X_POS[0]
        self.set_Y_POS()
        self.img_react = self.img.get_rect()
        self.img_react.x = self.x_pos
        self.img_react.y = self.y_pos

    def set_Y_POS(self):
        self.y_pos = random.randint(self.Y_POS[0], self.Y_POS[1])

    def draw(self, win):
        win.blit(self.img, self.img_react)

    def move(self, vel):
        self.x_pos -= vel
        self.img_react.x = self.x_pos
        
    def off_screen(self):
        # Comprobando si la nube está fuera de la pantalla.
        return self.x_pos < 0
