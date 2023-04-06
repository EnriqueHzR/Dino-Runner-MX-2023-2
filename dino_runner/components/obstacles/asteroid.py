from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import ASTEROID
import random

class Asteroid(Obstacles):
    Y_POS_BIRD = [100,300]
    NAME = "asteroid"
    
    def __init__(self):
        self.image = ASTEROID
        super().__init__(self.image)
        self.rect.y = random.randint(self.Y_POS_BIRD[0], self.Y_POS_BIRD[1])
        self.step_index = 0
    
    def fly(self):
        self.image = ASTEROID
        x_pos = self.rect.x
        y_pos = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos