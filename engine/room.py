# engine/room.py

import pygame
import json
import os
from engine.settings import *

class Room:
    def __init__(self, filename):
        self.tiles = []
        self.spawn_point = (0, 0)
        self.doors = {}  # id: {"rect", "leads_to", "leads_to_door"}
        width = height = 0

        # Load room layout
        with open(filename) as f:
            for y, line in enumerate(f):
                line = line.rstrip('\n')
                height = y + 1
                for x, char in enumerate(line):
                    width = max(width, x + 1)
                    if char == "#":
                        self.tiles.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    if char == "P":
                        self.spawn_point = (x*TILE_SIZE, y*TILE_SIZE)
        self.width = width * TILE_SIZE
        self.height = height * TILE_SIZE

        # --- Load doors from JSON metadata ---
        doors_json = filename.replace(".txt", "_doors.json")
        if os.path.exists(doors_json):
            with open(doors_json) as f:
                doors_data = json.load(f)
            for door in doors_data["doors"]:
                x, y = door["pos"]
                self.doors[door["id"]] = {
                    "rect": pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    "leads_to": door["leads_to"],
                    "leads_to_door": door["leads_to_door"]
                }

    def get_solid_tiles(self):
        return self.tiles

    def draw(self, screen, camera):
        screen.fill(COLOR_BG)
        for tile in self.tiles:
            screen_x = tile.x - camera.camera_rect.x
            screen_y = tile.y - camera.camera_rect.y + HUD_HEIGHT
            pygame.draw.rect(screen, COLOR_WALL, (screen_x, screen_y, TILE_SIZE, TILE_SIZE))
        for door in self.doors.values():
            door_rect = door["rect"]
            screen_x = door_rect.x - camera.camera_rect.x
            screen_y = door_rect.y - camera.camera_rect.y + HUD_HEIGHT
            pygame.draw.rect(screen, COLOR_DOOR, (screen_x, screen_y, TILE_SIZE, TILE_SIZE))