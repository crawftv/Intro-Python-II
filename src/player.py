# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

from item import Item
from typing import Dict


class Player:
    def __init__(self, current_room: Room, items: Dict = None):
        self.current_room = current_room
        self.items = items if items is not None else {} 
