# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:49:43 2020

@author: ghost

work: settings
"""
class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initailize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed_factor = 0.5
        
        # Bullet settings
        self.bullet_speed_factor = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        
        # Alien settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
        
        
        
        