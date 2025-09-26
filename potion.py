# potion.py
class Potion:
    def __init__(self, name, effect_amount, effect_type="heal"):
        self.name = name
        self.effect_amount = effect_amount
        self.effect_type = effect_type

    def use(self, hero):
        if self.effect_type == "heal":
            hero.stats["health"] += self.effect_amount
            if hero.stats["health"] > hero.max_health:
                hero.stats["health"] = hero.max_health
            print(f"{hero.stats['name']} healed {self.effect_amount} HP. Current health: {hero.stats['health']}")
        
        elif self.effect_type == "poison":
            hero.take_damage(self.effect_amount)
            print(f"{hero.stats['name']} was poisoned for {self.effect_amount} damage! Current health: {hero.stats['health']}")


test_inventory = []
first_item = test_inventory[0]
second_item = test_inventory[1]
third_item = test_inventory[2]
last_item = test_inventory[-1]

test_inventory.append("poison potion")

print (test_inventory)