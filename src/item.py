class Item:
    def __init__(self,name:str,description:str):
        self.name = name.replace(" ","_")
        self.description = description
    def __repr__(self):
        return self.name
