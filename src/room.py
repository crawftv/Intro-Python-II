# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from typing import Dict


class Room:
    def __init__(self, name: str, description: str, items: Dict[str,Item] = None):
        self.name = name
        self.description = description
        self.items = items if items is not None else {}

    def __repr__(self):
        return self.name
