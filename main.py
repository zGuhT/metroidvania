import pygame
from engine.settings import *
from engine.roommanager import *
from engine.camera import *
from engine.player import *
from engine.screens import *
from engine.hud import *

def run_game(screen, font):
    # --- Setup the game ---
    room_files = {
        "room1": "assets/rooms/room1.txt",
        "room2": "assets/rooms/room2.txt",
        "room3": "assets/rooms/room3.txt"
    }
    room_manager = RoomManager(room_files)
    camera = Camera(room_manager.current.width, room_manager.current.height)
    player = Player(room_manager.current.spawn_point)

    time_alive = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        dt = clock.tick(60) / 1000
        time_alive += dt

        # At the start of your update or loop:
        colliding_with_any_door = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", time_alive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit", time_alive

        keys = pygame.key.get_pressed()
        player.update(keys, room_manager.current, dt)
        camera.update(player)

        # Door transitions (optional)
        for door_id, door in room_manager.current.doors.items():
            if player.rect.colliderect(door["rect"]):
                colliding_with_any_door = True
                # Only allow transition if last_door_id is None (player wasn't just teleported)
                if player.last_door_id is None:
                    target_room = door["leads_to"]
                    target_door_id = door["leads_to_door"]
                    room_manager.change_room(target_room)
                    dest_door = room_manager.current.doors[target_door_id]
                    player.rect.topleft = dest_door["rect"].topleft
                    camera = Camera(room_manager.current.width, room_manager.current.height)
                    # Set last_door_id to this door, so no further transitions until they leave
                    player.last_door_id = target_door_id
                    break  # Prevents handling multiple doors in one frame

        # If not colliding with any door, reset last_door_id to None
        if not colliding_with_any_door:
            player.last_door_id = None

        # --- Game Over Example: restart if player falls off map ---
        if player.rect.top > room_manager.current.height:
            return "gameover"

        # Draw
        room_manager.current.draw(screen, camera)
        player.draw(screen, camera)
        draw_hud(screen, font, player)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Metroidvania!")
    font = pygame.font.Font(None, 56)

    while True:
        show_title_screen(screen, font)
        result, time_alive = run_game(screen, font)
        if result == "quit":
            break
        if result == "gameover":
            show_game_over(screen, font, time_alive)

    pygame.quit()

if __name__ == "__main__":
    main()