import pygame.font
from pygame.sprite import Group
from ship import Ship
class scoreboaed():
    def __init__(self,screen,ai_setting,stats):
        self.ships = Group()
        self.screen=screen
        self.ai_setting=ai_setting
        self.stats=stats
        self.screen_rect=screen.get_rect()

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
    def prep_score(self):
        round_score=round(self.stats.score,-1)
        score_str="{:,}".format(round_score)
        self.score_imge=self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        self.score_rect=self.score_imge.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20


    def prep_high_score(self):
        round_high_score=round(self.stats.high_score,-1)
        high_score_str="{:,}".format(round_high_score)
        self.high_score_imge=self.font.render(high_score_str,True,self.text_color,self.ai_setting.bg_color)
        self.high_score_imge_rect=self.high_score_imge.get_rect()
        self.high_score_imge_rect.top=self.screen_rect.top
        self.high_score_imge_rect.centerx=self.screen_rect.centerx
    def prep_level(self):
        self.level_imge=self.font.render(str(self.stats.level),True,self.text_color,self.ai_setting.bg_color)
        self.level_imge_rect=self.level_imge.get_rect()
        self.level_imge_rect.top=self.screen_rect.top+100
        self.level_imge_rect.right=self.screen_rect.right-20
    def prep_ships(self):
        self.ships = Group()
        for Ship_num in range(self.stats.ship_left):
            ship=Ship(self.ai_setting, self.screen)
            ship.rect.top=10
            ship.rect.x=20+Ship_num*ship.rect.width
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_imge, self.score_rect)
        self.screen.blit(self.high_score_imge, self.high_score_imge_rect)
        self.screen.blit(self.level_imge, self.level_imge_rect)
        self.ships.draw(self.screen)
