from weapons import Hand, Sword


class Charactor:
    def __init__(self, health=100, race="human") -> None:
        self.health = health
        self.race = race
        self.weapons = [Hand(), Sword()]


class Villager(Charactor):
    def __init__(self) -> None:
        super().__init__()
