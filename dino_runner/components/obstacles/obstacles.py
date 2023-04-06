from dino_runner.utils.constants import SCREEN_WIDTH
import pygame
class Obstacles:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.active = True

    def update(self, game_speed, player):
        if self.NAME == "asteroid":
            self.rect.x -= game_speed + 5
        else:
            self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect) and not player.shield and self.active == True:
            if player.hearts > 0:
                player.hearts -= 1
                self.active = False
            if player.hearts == 0:
                player.die()
                pygame.time.delay(300)
                player.dead = True
        if player.powerup != None:
            if self.rect.colliderect(player.powerup.rect) and self.active == True:
                self.active = False
                player.powerup = None
                self.rect.x = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)