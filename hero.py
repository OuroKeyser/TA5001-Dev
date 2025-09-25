
#character ____Hero
#         _____Enemy



class Hero():
    def __init__(self):
        self.max_health = 100.0

        self.stats = {
            "name" : "hero",
            "strength" : 7,
            "health" : 100,
        }
        self.inventory = ["sword", "health potion", "rope"]
    def print_stats(self):
        print("your stast are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")


    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()


    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self, damage):
        self.sytats["health"] = self.stats["health"] - damage
        print (f"your health is now {self.stats["health"]}")
        pass

    def heal(self, item_name):
        if (self.inventory.count("health potion") <=0):
            print(f"")

    def use_item(self):
        pass

#-------------------------------------------------
player = Hero()

#print (f"Here are your Hero Stats {player.stats}")

player.print_stats()