import potion
# Character ___ Hero
#        |___ Enemy

# TODO
# Player Heal
# USe Items
# Connect the two files.

class Hero:
    def __init__(self, x, y):
        self.max_health = 100.0
        self.x = x
        self.y = y
        self.stats = {
            "name" : "hero",
            "strength": 7,
            "health": 100.0,
        }
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")

    def use_item(self, item_name):
        item_name = input(f"What item do you want to use? {self.inventory}\n").lower()
        print (f"The item you want to use is {item_name}")
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                print(f"{item_name} has been removed from inventory\n")
                return
        print(f"You don’t have a {item_name}.")

    def print_stats(self):
        print("Your stats are: ")
        for key,value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move(self):
        direction = input ("What direction do you want to move? (north/south/west/east)\n").lower()

        if direction == "north":
            self.y += 1

        elif direction == "south":
            self.y -+ 1

        elif direction == "east":
            self.x += 1

        elif direction == "west":
            self.x -= 1

        else:
            print("Invalid direction. Please choose north, south, east, or west.")

        print (f"You moved {direction}. Your new position is ({self.x}, {self.y}.)")

    def attack(self):
        pass


    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your Health is now {self.stats['health']}")
        
    def heal(self,item_name):

        #TODO -> Move this to the Use Item Function
        if (self.inventory.count("health potion") <= 0):
            print (f"You don't have any {item_name}")
            return

        print (f"You've used a {item_name} you've restored {self.health_potion_strength} Health")
        self.stats["health"] = self.stats["health"] + self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print ("You've Reached Max Health")
            self.stats["health"] = self.max_health

        print (f"Your Health is now {self.stats['health']}")
        self.inventory.remove("health potion")
        print(f"Your inventory is now {self.inventory}")

    #def use_item(self):
        pass


#-------------------------------------------------
hero = Hero(0,0) # <--- __init__(self)
print("\n--------------------------------\n")
hero.set_name("Ouro")
print("\n--------------------------------\n")
health_potion = potion.Potion("Health Potion", 10, "heal")
poison_potion = potion.Potion("Poison Potion", 15, "poison")
hero.add_item(health_potion)
hero.add_item(poison_potion)
hero.stats["health"] = 70
hero.move()
hero.use_item("Health Potion")
hero.use_item("Poison Potion")
print("\n--------------------------------\n")

#print(f"Here are your Hero Stats {player.stats}")


