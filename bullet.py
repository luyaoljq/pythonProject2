import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,screen,ship,ai_setting):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_high)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor


    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
