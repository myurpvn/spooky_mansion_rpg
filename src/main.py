from characters import Villager


villager = Villager()

print(villager.__dict__)

weapons = villager.weapons
for w in weapons:
    print(w.__dict__)
