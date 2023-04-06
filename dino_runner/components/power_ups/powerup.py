from dino_runner.utils.constants import SCREEN_WIDTH
import pygame

class PowerUp:
    Y_POS = 125
    POWERUP_DURATION = 5000
    def __init__(self, image, type, name = "default"):
        self.image = image
        self.type = type
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.Y_POS
        self.start_time = 0
        self.time_up = 0
        self.used = False

    def update(self, speed, player):
        self.rect.x -= speed
        if self.rect.colliderect(player.dino_rect):
            self.start_time = pygame.time.get_ticks()
            self.time_up = self.start_time + self.POWERUP_DURATION
            if self.name == "heart" and self.used == False:
                player.hearts += 1
            self.used = True
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)
