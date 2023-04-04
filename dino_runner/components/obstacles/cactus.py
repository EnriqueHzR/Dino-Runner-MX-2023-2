from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random
class Cactus(Obstacles):
    Y_POS_CACTUS = 325
    NAME = "cactus"
    def __init__(self):
        self.image = random.choice(SMALL_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS

class LargeCactus(Obstacles):
    Y_POS_CACTUS = 300
    NAME = "cactus"
    def __init__(self):
        self.image = random.choice(LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS