# -*- coding: utf-8 -*-
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring information."""
    
    def __init__(self, ai_settings, screen, stats):
        """Initailize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 28)
        
        # Prepare the initail score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """Trun the score into a rendered image."""
        rounded_score = round(self.stats.score, -1) # 取到十位數之整數
        score_str = "{:,}".format(rounded_score) # 使輸出1,000,000格式
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 10
    
    def prep_high_score(self):
        """Trun the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, 
                                                 self.ai_settings.bg_color)
        
        # Display the high score at top canter of the screen
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = 10
    
    def prep_level(self):
        """Trun the level into a rendered image."""
        self.level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True,
                                           self.text_color, 
                                           self.ai_settings.bg_color)
        # Display the level
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centerx =  self.high_score_image_rect.left / 2
        self.level_image_rect.top = 10
        
    def prep_ships(self):
        """show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            self.ships.add(ship)
            
    def show_score(self):
        # Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        
        # Draw ships
        self.ships.draw(self.screen)
        
        
        
        