import sys
import pygame

import setting
from time import sleep
import ship
from Alien import Alien
from bullet import Bullet


def check_play_button(ai_setting,aliens,screen,play_button,stats,ship,bullets,mouse_x, mouse_y,sb):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active=True
        stats.reset_stats()
        sb.prep_level()
        sb.prep_score()
        sb.prep_high_score()
        aliens.empty()
        bullets.empty()
        ai_setting.int__dynamic()
        creat_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()
        sb.prep_ships()
        sb.show_score()


def check_events(ai_setting,aliens,screen,play_button,stats,ship,bullets,sb):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_setting,aliens,screen,play_button,stats,ship,bullets,mouse_x, mouse_y,sb)

def update_screen(ai_setting,screen,stats,sb,ship,bullets,aliens,
                  play_button):

    screen.fill(ai_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
def update_aliens(ai_setting,screen,ship,aliens,bullets,stats,sb):
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
    #     print("hit")
        ship_hit(ai_setting,screen,ship,aliens,bullets,stats,sb)
        print(stats.ship_left)
    check_aliens_bottom(ai_setting,stats, screen, ship, aliens,bullets,sb)

def check_keydown_events(event,ai_setting,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()
def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_aliens_bottom(ai_setting,stats, screen, ship, aliens,bullets,sb):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_setting, screen, ship, aliens, bullets, stats,sb)
            break

def update_bullets(ai_setting,screen,ship,aliens,bullets,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_aliens_bullets_collisions(ai_setting, screen, ship, aliens, bullets, stats, sb)
def check_aliens_bullets_collisions(ai_setting, screen, ship, aliens,bullets,stats,sb):
    collection = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collection:
        for alien in collection.values():
            stats.score += ai_setting.aliens_point*len(alien)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        sb.stats.level+=1
        sb.prep_level()
        ai_setting.increace_speed()
        bullets.empty()
        creat_fleet(ai_setting, screen, ship, aliens)

def check_high_score(stats,sb):
    if stats.score>=stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
def fire_bullet(ai_setting,screen,ship,bullets):
    if len(bullets) < 3:
        new_bullet = Bullet(screen, ship, ai_setting)
        bullets.add(new_bullet)
def creat_fleet(ai_setting,screen,ship,aliens):
    alien=Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height,
                                  alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_setting, screen, aliens, alien_number,
                         row_number)

def get_number_aliens_x(ai_setting, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def get_number_rows(ai_setting, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_setting.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def creat_alien(ai_setting,screen,aliens,alien_num,row_num):
    alien = Alien(ai_setting, screen)
    alien.x = alien_num * alien.rect.width * 2 + alien.rect.width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)
def check_fleet_edges(ai_setting,aliens):
    for alien in  aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break
def change_fleet_direction(ai_setting,aliens):
    ai_setting.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y+=ai_setting.fleet_droop_speed
def ship_hit(ai_setting, screen, ship, aliens,bullets,stats,sb):
    if stats.ship_left>0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active=False



