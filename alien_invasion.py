# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:21:21 2020

@author: ghost

work: alien_invasion
"""
import sys # 結束遊戲
import pygame # 開發遊戲

from settings import Settings 

def run_game():
    # Initialize game and creat a screen object
    pygame.init() # 初始化背景設定
    screen = pygame.display.set_mode((1200,500)) # 建立名為screen的顯示視窗，指定視窗大小寬1200、高800像素 
    pygame.display.set_caption("Alien Invasion") # 建立顯示視窗的標題 (遊戲名稱)
    
    # Set the background color
    bg_color = (230,230,230)
    
    # Start the main loop for the game
    while True:
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redrawn the sreen during each pass through the loop
        screen.fill(bg_color) # 將螢幕填滿該顏色
        
        # Mark the most recently drawn screen visible
        pygame.display.flip() # 會不斷更新畫面，留下新繪製的畫面而擦掉舊的
        

run_game()
