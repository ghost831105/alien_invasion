# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:05:00 2020

@author: ghost
"""
import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen. """
    # Redrawn the sreen during each pass through the loop
    screen.fill(ai_settings.bg_color) # 將螢幕填滿該顏色
    ship.blitme() # 繪製太空船於螢幕上
     
    # Mark the most recently drawn screen visible
    pygame.display.flip() # 會不斷更新畫面，留下新繪製的畫面而擦掉舊的