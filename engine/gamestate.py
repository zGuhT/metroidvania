# engine/gamestate.py

import json

class GameState:
    """
    Holds persistent player state: health, upgrades, cleared rooms, and more.
    Add methods to save/load progress to disk as needed.
    """
    def __init__(self):
        self.health = 3
        self.upgrades = {
            "double_jump": False,
            "dash": False,
            "morph_ball": False,
            # add more abilities here as needed
        }
        self.rooms_cleared = set()
        self.inventory = set()  # For keys, collectibles, etc.

    def to_dict(self):
        """Return a serializable dictionary of game state."""
        return {
            "health": self.health,
            "upgrades": self.upgrades,
            "rooms_cleared": list(self.rooms_cleared),
            "inventory": list(self.inventory),
        }

    def from_dict(self, data):
        """Restore state from a dictionary."""
        self.health = data.get("health", 3)
        self.upgrades = data.get("upgrades", self.upgrades)
        self.rooms_cleared = set(data.get("rooms_cleared", []))
        self.inventory = set(data.get("inventory", []))

    def save(self, filename="savegame.json"):
        """Save the game state to disk as JSON."""
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    def load(self, filename="savegame.json"):
        """Load the game state from disk (if present)."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.from_dict(data)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Start new game if no save

# Usage Example (at the top of your main loop or when loading a save):
# game_state = GameState()
# game_state.load()