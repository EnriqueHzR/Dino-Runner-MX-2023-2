from .shield import Shield
from .hammer import Hammer
import random
class PowerUpManager:
    POINTS = 200

    def __init__(self):
        self.powerups = []

    def update(self,game_speed,points, player):
        if len(self.powerups) == 0 and points % self.POINTS == 0:
            self.powerups.append(random.choice([Shield(), Hammer()]))
        for powerup in self.powerups:
            if powerup.used or powerup.rect.x < -powerup.rect.width:
                self.powerups.pop()
            if powerup.used:
                player.set_power_up(powerup)
            powerup.update(game_speed, player)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)