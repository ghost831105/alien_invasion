# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship2.png") # 載入圖片
        self.rect = self.image.get_rect() # 取得圖片的矩形
        self.screen_rect = screen.get_rect() # 取得螢幕的矩形
                
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
       
        # Movement flag
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down =False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.centerx -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect) 
        
    def center_ship(self):
        """Center the ship on the screen."""
        # reset the ship to center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # reset center position of ship
        # 若沒重置centerx,centery，在ship.update()會使用到舊的位置
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
     
       
        