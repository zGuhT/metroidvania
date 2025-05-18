# engine/roommanager.py

from engine.room import Room

class RoomManager:
    def __init__(self, room_files):
        self.rooms = {name: Room(filename) for name, filename in room_files.items()}
        self.current = self.rooms["room1"]

    def change_room(self, room_name, entry_point=None):
        self.current = self.rooms[room_name]
        # Return the appropriate spawn point
        if entry_point:
            return entry_point
        else:
            return self.current.spawn_point