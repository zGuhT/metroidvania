# Metroidvania Game (Python, Pygame)

A retro-style Metroidvania platformer template written in Python using Pygame.  
Explore interconnected rooms, transition through doors, manage player upgrades, and display a HUD!

---

## Features

- **Room-based world:** Each room is loaded from an ASCII `.txt` file and paired with a `.json` file describing all doors and their connections.
- **Non-linear exploration:** Doors can lead anywhere, using an unlimited, ID-based linking system for full Metroidvania design flexibility.
- **HUD display:** Health, shield, and ammo are tracked and drawn above the game world.
- **Player state:** Upgrades, health, and persistent game state managed via `GameState`.
- **Basic enemies, upgrades, and transitions** (expandable).
- **Fully keyboard-navigable menu and game over screens.**

---

## Requirements

- Python 3.10+
- Pygame 2.0+

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Running the Game

```bash
python3 main.py
```

---

## Controls

* Arrow keys or WASD: Move
* Space: Jump
* Esc: Quit
* Enter: Select menu option

---

## Directory Structure

```go
assets/
├── rooms/
│   ├── room1.txt
│   ├── room1_doors.json
│   ├── room2.txt
│   ├── room2_doors.json
│   ├── room3.txt
│   └── room3_doors.json
engine/
├── camera.py
├── enemy.py
├── gamestate.py
├── hud.py
├── player.py
├── room.py
├── roommanager.py
├── screens.py
├── settings.py
├── tilemap.py
├── upgrade.py
└── main.py
README.md
requirements.txt
test_pygame.py
update_changelog.py
```

---

## Example Room File (room1.txt)

```text
#########################
#.......................#
###########....##########
#.......................#
#.....#############.....#
#......................D#
###########....##########
#.......................#
#.....#############.....#
#.......................#
###########....##########
#.......................#
#.....#############.....#
#.......................#
###########....##########
#.......................#
#.....#############.....#
#P..........##.........D#
#########################
```

---

## Example Door File (room1_doors.json)

```json
{
  "doors": [
    {
      "id": "right_exit",
      "pos": [23, 17],
      "leads_to": "room2",
      "leads_to_door": "left_entrance"
    },
    {
      "id": "upper_right_exit",
      "pos": [23, 5],
      "leads_to": "room3",
      "leads_to_door": "left_entrance"
    }
  ]
}
```

---

## Version History

v0.01 (2025-05-18)
* Initial project setup
* ASCII room loading and door system (via JSON for unlimited doors)
* Room-to-room transitions (with anti-ping-pong logic)
* HUD for health, shield, ammo
* Title menu, instructions, game over screens
* Player movement, jump, basic enemy framework
* Game state persistence structure
* Simple example rooms and door configs

---

## To Do (at least)

* Implement upgrades and collectibles
* Add more enemy types and AI
* Add music and sound effects
* Polish menus and transitions
* Save/load support
* Expand level design

---

## Credits

* Pygame for the framework
* Myself - J.V.