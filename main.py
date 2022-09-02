# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import sys
import pygame
from Alien import Alien
from Scoreboard import scoreboaed
from button import Button
from ship import Ship
from setting import settings
import game_functions as gf
from  pygame.sprite import Group
from game_stats import Game_stats
def run_game():
    pygame.init()
    ai_setting=settings()


    screen=pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height,))
    pygame.display.set_caption("alien invasion")
    play_button=Button(screen,ai_setting,"PLAY")
    ship=Ship(ai_setting,screen)
    bg_color = (230, 230, 230)
    bullets=Group()
   # alien=Alien(ai_setting,screen)
    aliens=Group()
    gf.creat_fleet(ai_setting, screen, ship, aliens)
    stats=Game_stats(ai_setting)
    sb=scoreboaed(screen,ai_setting,stats)
    while True:
       # screen.fill(ai_setting.bg_color)
       # ship.blitme()
       # for event in pygame.event.get():
       #     if event.type == pygame.QUIT:
       #         sys.exit()

      # pygame.display.flip()

       gf.check_events(ai_setting,aliens,screen,play_button,stats,ship,bullets,sb)
       if stats.game_active:
           ship.update()
           gf.update_bullets(ai_setting, screen, ship, aliens, bullets,stats,sb)

           gf.update_aliens(ai_setting, screen, ship, aliens, bullets, stats,sb)
       #print(len(bullets))

       gf.update_screen(ai_setting, screen, stats,sb ,ship, bullets, aliens,
                     play_button)

     #  gf.creat_fleet(ai_setting,screen,ship,aliens)
run_game()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
