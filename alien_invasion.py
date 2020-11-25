# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:21:21 2020

@author: ghost

work: alien_invasion
"""
import pygame # 開發遊戲
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and creat a screen object
    pygame.init() # 
    ai_settings = Settings()
    screen = pygame.display.set_mode( # 建立名為screen的顯示視窗，指定視窗大小寬1200、高800像素 
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion") # 建立顯示視窗的標題 (遊戲名稱)
    
    # Make the ship.
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in.
    bullets = Group()
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        

run_game()
