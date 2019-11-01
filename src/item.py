class Item:
    def __init__(self, name: str, description: str):
        self.name = name.replace(" ", "_")
        self.description = description
    def on_take(self):
        print(f"You have picked up {self.name}")
    def on_drop(self):
        print(f"You have dropped {self.name}")

    def __repr__(self):
        return self.name
