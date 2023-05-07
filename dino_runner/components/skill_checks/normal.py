from .skill_check import SkillCheck
import random
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
class Normal(SkillCheck):
    def __init__(self):
        height = random.randint(10,400)
        width = random.randint(0, SCREEN_WIDTH-300)
        super().__init__(height,width,15,5)
