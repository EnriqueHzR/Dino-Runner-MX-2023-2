from dino_runner.utils.constants import SCREEN_WIDTH
import pygame
class Obstacles:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            player.die()
            pygame.time.delay(300)
            player.dead = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)