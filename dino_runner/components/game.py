import pygame, random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.clouds import Clouds
from .skill_checks.skill_checks_manager import SkillCheckManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from .power_ups.powerup_manager import PowerUpManager
from dino_runner.components import text_utils
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.clouds = [Clouds()]
        self.obstacles_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.skill_check_manager = SkillCheckManager()
        self.points = 0
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            if not self.skill_check_manager.event_skill:
                self.player.update(user_input)
                if random.randint(1, 100) < 5:
                    self.clouds.append(Clouds())
                for cloud in self.clouds:
                    cloud.move(self.game_speed)
                    if cloud.off_screen():
                        self.clouds.remove(cloud)
                self.obstacles_manager.update(self.game_speed, self.player)
                self.powerup_manager.update(self.game_speed,self.points, self.player)
                self.points += 1
                if self.points % 300 == 0:
                    self.game_speed += 1
                if self.player.dead:
                    self.skill_check_manager.event_skill = True
            self.skill_check_manager.update(user_input, self.player)
            if self.player.dead and not self.skill_check_manager.event_skill:
                self.playing = False
                self.death_count += 1
            if self.skill_check_manager.res_event:
                points = self.points
                game_speed = self.game_speed
                self.reset()
                self.game_speed = game_speed
                self.points = points
                self.death_count += 1
                self.playing = True
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            for cloud in self.clouds:
                cloud.draw(self.screen)
            self.player.draw(self.screen)
            if self.player.powerup != None:
                self.player.powerup.draw(self.screen)
            self.obstacles_manager.draw(self.screen)
            self.powerup_manager.draw(self.screen)
            self.skill_check_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        score, score_rect = text_utils.get_message('Points: ' + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)
    
    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death_count == 0:
            text, text_rect = text_utils.get_message('Press any key to start', 30)
            self.screen.blit(text, text_rect)
            #pruebas
        else:
            text, text_rect = text_utils.get_message('Press any key to restart', 30)
            score, score_rect = text_utils.get_message('Score: ' + str(self.points), 30, height= SCREEN_HEIGHT//2 + 50)
            intents, intents_rect = text_utils.get_message('Intents: ' + str(self.death_count), 30, height= SCREEN_HEIGHT//2 + 100)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(intents, intents_rect)

    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.clouds = [Clouds()]
        self.obstacles_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.skill_check_manager = SkillCheckManager()
        self.points = 0