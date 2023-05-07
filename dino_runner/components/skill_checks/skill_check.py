from dino_runner.utils.constants import SCREEN_WIDTH
import pygame
import random

class SkillCheck:
    BACKGROUND_COLOR = (0,0,0)
    BORDER_COLOR = (255,255,255)
    POINTER_COLOR = (255,0,0)
    REGULAR_AREA_COLOR = (128,128,128)
    EXCELLENT_AREA_COLOR = (255,255,255)

    def __init__(self, posy, posx, cooldown, vel):
        self.posx = posx
        self.posy = posy
        self.time = pygame.time.get_ticks() 
        self.cooldown = cooldown
        self.vel = vel
        self.res = None
        self.end = False
        self.gen_skill()

    def update(self, player_input):
        if self.time <= pygame.time.get_ticks():
            if player_input[pygame.K_r] and not self.end:
                if self.pointer.colliderect(self.excellent_area):
                    self.res = "Excellent"
                elif self.pointer.colliderect(self.regular_area):
                    self.res = "Regular"
                else:
                    self.res = "Fail"
                self.end = True
            if not self.end:
                if self.pointer.x >= self.regular_area.x + 60:
                    self.res = "Fail"
                    self.end = True
                self.pointer.x += self.vel
            else:
                pygame.time.delay(100)
    
    def draw(self,screen):
        if not self.end:
            pygame.draw.rect(screen,self.BACKGROUND_COLOR, self.background,5)
            pygame.draw.rect(screen,self.REGULAR_AREA_COLOR,self.regular_area)
            pygame.draw.rect(screen,self.EXCELLENT_AREA_COLOR, self.excellent_area)
            pygame.draw.rect(screen, self.POINTER_COLOR, self.pointer)

    def gen_skill(self):
        #Pruebas
        self.background = pygame.Rect(self.posx, self.posy, 300,25)
        area_skill = random.randint(self.posx + 5,self.posx + 300-60)
        self.regular_area = pygame.Rect(area_skill, self.posy, 60,25)
        self.excellent_area = pygame.Rect(area_skill, self.posy, 15,25)
        self.pointer = pygame.Rect(self.posx, self.posy, 3,25)