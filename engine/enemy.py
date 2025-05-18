# engine/enemy.py
import pygame
from engine.settings import *
class Enemy:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], TILE_SIZE, TILE_SIZE)
        self.vel = pygame.Vector2(-50, 0)
    def update(self, dt, room):
        self.rect.x += int(self.vel.x * dt)
        # Simple AI: bounce on collision
        for tile in room.get_solid_tiles():
            if self.rect.colliderect(tile):
                self.vel.x *= -1