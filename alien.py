# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:14:01 2020

@author: ghost
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represnt a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien3.png")
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width # alien與左側間距為外星人寬度
        self.rect.y = self.rect.height # alien與上側間距為外星人長度
        
        # Store the alien's the position.
        self.x = float(self.rect.x)
        
        self.speed_factor = ai_settings.alien_speed_factor
        self.fleet_direction = ai_settings.fleet_direction
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
             
    def update(self):
        """Move the alien right or left."""
        # Update the decimal posittion of the aliens
        self.x += self.speed_factor * self.fleet_direction
        # Update the rect position
        self.rect.x = self.x
        
        
    def blitme(self):
        """Draw the alien at its current location. """
        self.screen.blit(self.image, self.rect) 
        
        
        
        
        
        
        
        
        
        
        