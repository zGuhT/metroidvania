# engine/camera.py
import pygame
from engine.settings import *

class Camera:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.camera_rect = pygame.Rect(0, 0, map_width, map_height)

    def update(self, target):
        # NOTE: The "center" of the camera in screen-space is now in the region below HUD_HEIGHT!
        x = target.rect.centerx - SCREEN_WIDTH // 2
        y = target.rect.centery - (SCREEN_HEIGHT - HUD_HEIGHT) // 2

        # Clamp as before, but only allow scrolling within playable area (i.e. don't show above the top row)
        x = max(0, min(x, self.map_width - SCREEN_WIDTH))
        y = max(0, min(y, self.map_height - (SCREEN_HEIGHT - HUD_HEIGHT)))

        # But most importantly: draw the room in the area (0, HUD_HEIGHT, width, height)
        self.camera_rect = pygame.Rect(x, y, SCREEN_WIDTH, SCREEN_HEIGHT - HUD_HEIGHT)