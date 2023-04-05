from dino_runner.components.obstacles.cactus import Cactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles.append(Cactus())
        self.max_obstacles = 2

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            chance = random.randint(0, 2)
            if chance == 0:
                self.obstacles.append(Cactus())
            elif chance == 1:
                self.obstacles.append(LargeCactus())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            if obstacle.NAME == "bird":
                obstacle.fly()
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)