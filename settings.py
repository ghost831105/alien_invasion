# -*- coding: utf-8 -*-
import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initailize the game's settings"""
        # mouse is visiable
        pygame.mouse.set_visible(True)
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 2 # 壽命
        
        # Bullet settings
        self.bullet_width = 100 #3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10 
        
        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.5
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.alien_speed_factor = 0.3
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_points = 50
         # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed_factor *= self.speedup_scale 
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_points = int(self.alien_points * self.score_scale)
        print("alien's point: ", self.alien_points)