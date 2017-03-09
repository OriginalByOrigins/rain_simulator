"""
Simulate raining
"""

import pygame
from settings import Settings
import simulator_functions as sf
from drop import Drop


def run_rain():
    """Initialize rain simulator, settings and loop"""
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Rain Simulation')

    drops = [Drop(ai_settings, screen)]

    while True:
        sf.check_events()
        pygame.mouse.set_visible(False)
        sf.update_fleet(ai_settings, screen, drops)
        sf.update_screen(ai_settings, screen, drops)


run_rain()
