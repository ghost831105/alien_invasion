# -*- coding: utf-8 -*-
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        # ship.rect.centerx += 1 # 玩家按一次按建，船動一次
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
       
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet.""" 
    # Creat a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)       

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False   
        
def check_events(ai_settings, screen, stats, ship, aliens, bullets,
                 play_button):
    """Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #print(event.key)
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, ship, aliens,
                              bullets, play_button, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, ship, aliens, bullets,
                      play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Creat a new fleet and center the ship
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
def update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                  play_button):
    """Update images on the screen and flip to the new screen. """
    # Redrawn the sreen during each pass through the loop
    screen.fill(ai_settings.bg_color) # 將螢幕填滿該顏色
    
    # Redrawn all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # 繪製太空船於螢幕上
    aliens.draw(screen) # 繪製一堆外星人於螢幕上
 
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    
    # Mark the most recently drawn screen visible
    pygame.display.flip() # 會不斷更新畫面，留下新繪製的畫面而擦掉舊的
    
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of bullets that have disapeared."""
    # Update bullest positions. 
    bullets.update()
        
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)
    
def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens,True, True)
    
    if len(aliens) == 0:
        # Destory existing bullets, speed up game and creat new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        creat_fleet(ai_settings, screen, ship, aliens)
        
    
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        alien.fleet_direction *= -1
  
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def ship_hit(ai_settings, screen, stats, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ship_left > 0:
        # Decrement ship_left
        stats.ship_left -= 1
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Creat a new fleet and center the ship
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # Pause
        sleep(0.5) 
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # 當遊戲結束時，將隱藏的滑鼠游標顯示出來
    
    
def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
       if alien.rect.bottom >= screen_rect.bottom:
           ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
           break
    
def update_aliens(ai_settings, screen, stats, ship, aliens, bullets):
    """Update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
        print("Ship hit!!!")
    
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets) 

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creat an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

    
def creat_fleet(ai_settings, screen, ship, aliens):
    """Creat a full fleet of aliens."""
    # Creat an alien and find the number of aliens in a row.   
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                 alien.rect.height)
    # Creat the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)
    
# =============================================================================
# 不論使用者甚麼時候按下按建都會 pygame.event.get() 登陸註冊成一個 KEYDOWN 事件
# 太空船的 rect.centerx 為 x 軸，右移 → x 增加
# 太空船的 rect.bottom 為 y 軸，上移 → y 增加
# =============================================================================
# 繪製 aliens 時可使用兩種方式，
# 但 bullets 卻不能使用bullets.draw(screen)，因為 bullet 非 image 
# for alien in aliens.sprites():
#         alien.blitme()
# ------------與上方等價-----------
#  aliens.draw(screen)
# =============================================================================
