"""
drop module stores Drop class,
    which contains all behaviors of rain drops
"""

import pygame
from random import randint


class Drop():
    """Initialize a rain drop and its starting position"""

    def __init__(self, ai_settings, screen):
        """Construct a rain drop"""
        self.ai_settings = ai_settings
        self.screen = screen

        far = randint(1,3)
        if far == 1:
            self.drop_width = 1
            self.drop_height = randint(10,17)
            self.speed = 2
        elif far == 2:
            self.drop_width = 2
            self.drop_height = randint(20,30)
            self.speed = 5
        else:
            self.drop_width = 3
            self.drop_height = randint(33, 43)
            self.speed = 8


        self.rect = pygame.Rect(
            0, 0, self.drop_width, self.drop_height)
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.top
        self.rect.x = randint(0, ai_settings.screen_width)

        self.color = ai_settings.drop_color

        self.y = float(self.rect.y)

    def update(self):
        """Update drop's position each time through the loop"""
        self.y += self.speed
        self.rect.y = self.y

    def draw_drop(self):
        """Draw the drop to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)