# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:05:00 2020

@author: ghost
"""
import sys

import pygame

from bullet import Bullet

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
        
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #print(event.key)
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen. """
    # Redrawn the sreen during each pass through the loop
    screen.fill(ai_settings.bg_color) # 將螢幕填滿該顏色
    
    # Redrawn all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # 繪製太空船於螢幕上
     
    # Mark the most recently drawn screen visible
    pygame.display.flip() # 會不斷更新畫面，留下新繪製的畫面而擦掉舊的
    
def update_bullets(bullets):
    """Update position of bullets and get rid of bullets that have disapeared."""
    # Update bullest positions. 
    bullets.update()
        
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))




# =============================================================================
# 不論使用者甚麼時候按下按建都會 pygame.event.get() 登陸註冊成一個 KEYDOWN 事件
# 太空船的 rect.centerx 為 x 軸，右移 → x 增加
# 太空船的 rect.bottom 為 y 軸，上移 → y 增加
# =============================================================================
