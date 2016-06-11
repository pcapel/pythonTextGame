
class Potion:
    def __init__(self):
        self.value = 50
        self.description = """
        Potions are used when you find yourself in dire straits.\n
        They return your vitality, and heal wounds that are superficial.\n
        Heals 5 health.
        """
        def effect(self, attribute):
            attribute = attribute + 5
