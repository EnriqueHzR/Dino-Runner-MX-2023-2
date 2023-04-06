from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import SPRINT, SPRINT_TYPE
#??? no se como aplicarlo
class Sprint(PowerUp):
    def __init__(self):
        self.image = SPRINT
        self.type = SPRINT_TYPE
        super().__init__(self.image, self.type)
