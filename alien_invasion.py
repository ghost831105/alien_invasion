# -*- coding: utf-8 -*-
"""work: alien_invasion"""
import pygame # 開發遊戲
from pygame.sprite import Group

from settings import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and creat a screen object
    pygame.init() # 
    ai_settings = Settings()
    screen = pygame.display.set_mode( # 建立名為screen的顯示視窗，指定視窗大小寬1200、高800像素 
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion") # 建立顯示視窗的標題 (遊戲名稱)
    
    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Creat an instance to store game statistics and creat a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make the ship.
    ship = Ship(ai_settings, screen)
    
    # Make groups to store bullets and aliens in.
    bullets = Group()
    aliens = Group()
    
    # Make a alien or make aliens.
    #alien = Alien(ai_settings, screen) # Make the alien.
    gf.creat_fleet(ai_settings, screen, ship, aliens) # Make the aliens.
    
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets,
                        play_button, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, aliens,
                              bullets, sb)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets,
                             sb)
            
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button, sb)
            

run_game()
