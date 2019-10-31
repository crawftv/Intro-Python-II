# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name: str, description: str,items:List[Item]=None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        self.items = items
    def __repr__(self):
        return self.name
