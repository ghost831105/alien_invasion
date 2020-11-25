# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:33:34 2020

@author: ghost
"""
import pygame

class Ship():
    
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship2.png") # 載入圖片
        self.rect = self.image.get_rect() # 取得圖片的矩形
        self.screen_rect = screen.get_rect() # 取得螢幕的矩形
        
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect) 