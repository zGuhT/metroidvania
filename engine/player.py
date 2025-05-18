# engine/player.py

import pygame
from engine.settings import *

class Player:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], TILE_SIZE, TILE_SIZE)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.jump_count = 0
        self.max_jumps = 1  # Set to 2 for double jump
        # Add HUD-related state:
        self.health = 3
        self.max_health = 5
        self.shield = 2    # Shield level (or True/False)
        self.max_shield = 3
        self.ammo = {"missiles": 5, "bombs": 2}
        self.max_ammo = {"missiles": 10, "bombs": 5}
        self.last_door_id = None

    def update(self, keys, room, dt):
        # --- Horizontal movement ---
        self.vel.x = 0
        if keys[pygame.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel.x = PLAYER_SPEED

        # --- Jumping ---
        if self.on_ground:
            self.jump_count = 0  # Reset on ground
        if keys[pygame.K_SPACE]:
            if self.on_ground:
                self.vel.y = -PLAYER_JUMP
                self.jump_count = 1
                self.on_ground = False
            elif self.jump_count < self.max_jumps and not getattr(self, "jump_held", False):
                self.vel.y = -PLAYER_JUMP
                self.jump_count += 1
            self.jump_held = True
        else:
            self.jump_held = False

        # Gravity
        self.vel.y += GRAVITY * dt
        if self.vel.y > MAX_FALL_SPEED:
            self.vel.y = MAX_FALL_SPEED

        # Move and collide (horizontal first)
        self.rect.x += int(self.vel.x * dt)
        self.collide(room, 1)
        self.rect.y += int(self.vel.y * dt)
        self.on_ground = False
        self.collide(room, 0)

    def collide(self, room, horizontal):
        for tile in room.get_solid_tiles():
            if self.rect.colliderect(tile):
                if horizontal:
                    if self.vel.x > 0:
                        self.rect.right = tile.left
                    if self.vel.x < 0:
                        self.rect.left = tile.right
                else:
                    if self.vel.y > 0:
                        self.rect.bottom = tile.top
                        self.vel.y = 0
                        self.on_ground = True
                    if self.vel.y < 0:
                        self.rect.top = tile.bottom
                        self.vel.y = 0

    def draw(self, screen, camera):
        screen_x = self.rect.x - camera.camera_rect.x
        screen_y = self.rect.y - camera.camera_rect.y + HUD_HEIGHT
        pygame.draw.rect(screen, COLOR_PLAYER, (screen_x, screen_y, TILE_SIZE, TILE_SIZE))