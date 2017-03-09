"""
settings module stores default settings for rain simulator
"""

import pygame


class Settings():
    """Settings class store default settings as attributes"""
    def __init__(self):
        """Initialize all settings"""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Drop settings
        self.drop_color = (18,183,191)
        
