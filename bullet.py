# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Creat a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        
        # Creat a bullet rect at (0,0) and then set correct position. 
        #先於(0,0)建立出矩形，在將矩形移至正確的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
       
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor 
        # Update the rect position
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        