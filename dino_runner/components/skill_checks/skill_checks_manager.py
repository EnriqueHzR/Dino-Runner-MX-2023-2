from .normal import Normal
import random
class SkillCheckManager:
    POINTS = {"Fail": -7, "Regular": 5, "Excellent": 10}
    def __init__(self):
        self.skill_check = None
        self.score = 0
        self.event_skill = False
        self.res_event = None

    def update(self,player_input,player):
        if self.event_skill:
            if player.dead and self.skill_check == None:
                self.skill_check = Normal()
            else:
                if not self.skill_check.end:
                    self.skill_check.update(player_input)
                else:
                    self.score += self.POINTS[self.skill_check.res]
                    self.skill_check = None
            if self.score <=-1:
                self.event_skill = False
                self.res_event = False
            if self.score >= 30:
                self.res_event = True
                self.event_skill = False
                player.dead = False

    def draw(self, screen):
        if self.skill_check != None:
            self.skill_check.draw(screen)