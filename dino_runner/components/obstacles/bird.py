from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacles):
    Y_POS_BIRD = [250, 200, 150]
    NAME = "bird"
    
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.Y_POS_BIRD)
        self.step_index = 0
    
    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        x_pos = self.rect.x
        y_pos = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0