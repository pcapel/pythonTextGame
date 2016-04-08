from character_classes import Character
class Goblin(Character):
    def __init__(self, player, name):
        Character.__init__(self, 1, 10, 10, 6, 5, 1)
        self.name = name
        self.gives_exp = 150

class Bear(Character):
    def __init__(self, player, name):
        Character.__init__(self, 3, 15, 15, 12, 2, 1)
        self.name = "Bear"
        self.gives_exp = 170

class Demon(Character):
    def __init__(self, player, name):
        Character.__init__(self, 10, 30, 30, 20, 15, 1)
        self.name = name
        self.gives_exp = 1500
