class Weapons:
    def __init__(self) -> None:
        self.name = ""
        self.damage = 0
        self.use_count = 0


class Hand(Weapons):
    def __init__(self) -> None:
        super().__init__()
        self.name = "hand"
        self.damage = 5
        self.use_count = 9999


class Sword(Weapons):
    def __init__(self) -> None:
        super().__init__()
        self.name = "sword"
        self.damage = 15
        self.use_count = 5
