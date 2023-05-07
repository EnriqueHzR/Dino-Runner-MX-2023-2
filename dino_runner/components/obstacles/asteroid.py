from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import ASTEROID
import random

class Asteroid(Obstacles):
    Y_POS_ASTEROID = [100,300]
    NAME = "asteroid"
    
    def __init__(self):
        self.image = ASTEROID
        super().__init__(self.image)
        self.rect.y = random.randint(self.Y_POS_ASTEROID[0], self.Y_POS_ASTEROID[1])
        