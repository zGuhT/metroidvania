from engine.settings import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

def show_title_screen(screen, font):
    menu_options = ["Start Game", "Instructions", "Quit"]
    selected = 0

    title_text = font.render("Metroidvania!", True, (200, 220, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(menu_options)
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(menu_options)
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if menu_options[selected] == "Start Game":
                        return "start"
                    if menu_options[selected] == "Instructions":
                        show_instructions(screen, font)
                    if menu_options[selected] == "Quit":
                        pygame.quit()
                        exit()

        screen.fill((20, 18, 36))
        screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH//2, 180)))

        for i, option in enumerate(menu_options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            option_text = font.render(option, True, color)
            screen.blit(option_text, option_text.get_rect(center=(SCREEN_WIDTH//2, 300 + i*60)))

        pygame.display.flip()

def show_instructions(screen, font):
    instructions = [
        "Arrow keys/WASD to move",
        "Space to jump",
        "Goal: Explore and survive!",
        "",
        "Press [ESC] to return"
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.fill((20, 18, 36))
        for i, line in enumerate(instructions):
            text = font.render(line, True, (220, 220, 220))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH//2, 180 + i*50)))
        pygame.display.flip()

def show_game_over(screen, font, time_alive):
    over_text = font.render("Game Over", True, (255, 80, 80))
    time_text = font.render(f"You survived: {time_alive:.2f} seconds", True, (255, 255, 255))
    prompt_text = font.render("Press [SPACE] for Menu or [ESC] to Quit", True, (180, 180, 180))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "menu"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        screen.fill((20, 18, 36))
        screen.blit(over_text, over_text.get_rect(center=(SCREEN_WIDTH//2, 180)))
        screen.blit(time_text, time_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60)))
        pygame.display.flip()
