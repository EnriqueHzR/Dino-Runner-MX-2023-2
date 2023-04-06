from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)
    

class HammerProjectile:
    def __init__(self, x, y):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, speed):
        self.rect.x += self.speed + speed
        