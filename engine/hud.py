import pygame
from engine.settings import *

def draw_hud(screen, font, player):
    # Opaque background for HUD (cover up the game world)
    pygame.draw.rect(screen, (20, 18, 36), (0, 0, SCREEN_WIDTH, HUD_HEIGHT))
    pygame.draw.line(screen, (120,120,160), (0, HUD_HEIGHT), (SCREEN_WIDTH, HUD_HEIGHT), 2)
    
    # Health (draw as hearts or bars)
    for i in range(player.max_health):
        color = (255, 0, 0) if i < player.health else (100, 50, 50)
        pygame.draw.rect(screen, color, (20 + i * 36, 20, 28, 28), border_radius=6)
        # If you want icons, load and blit a heart image instead!

    # Shield (draw as blue blocks or an icon)
    for i in range(player.max_shield):
        color = (80, 180, 255) if i < player.shield else (50, 80, 120)
        pygame.draw.rect(screen, color, (20 + i * 36, 60, 28, 28), border_radius=6)
        # Again, can use a shield image/icon

    # Ammo counts
    missiles = player.ammo.get("missiles", 0)
    bombs = player.ammo.get("bombs", 0)
    missile_text = font.render(f"Missiles: {missiles}/{player.max_ammo.get('missiles', missiles)}", True, (255,255,180))
    bomb_text = font.render(f"Bombs: {bombs}/{player.max_ammo.get('bombs', bombs)}", True, (255,220,80))
    screen.blit(missile_text, (SCREEN_WIDTH//2 - 80, 25))
    screen.blit(bomb_text, (SCREEN_WIDTH//2 - 80, 65))

    # (Optional) Display other info, e.g., powerups, score, etc.