"""
This module stores all functions needed for run_rain
"""

import pygame
import sys
from drop import Drop


def check_events():
    """Respond to keypresses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()


def update_fleet(ai_settings, screen, drops):
    """Update more rain drops if previous fleet fall a distance"""

    for drop in drops[:]:
        drop.update()
        if drop.y >= ai_settings.screen_height:
            drops.remove(drop)
    if drops[-1].y >= 2:
        for counter in range(0, 30):
            new_drop = Drop(ai_settings, screen)
            drops.append(new_drop)


def update_screen(ai_settings, screen, drops):
    screen.fill(ai_settings.bg_color)

    for drop in drops:
        drop.draw_drop()

    pygame.display.flip()