#TODO
#     
#
#
#
#
#
#
#
hero_stats= {
        "name" : "hero",
        "strength" : 7,
        "health" : 100.0,
}

hero_max_health = 100

health_potion_strength = 5
hero_inventory = ["sword", "health potion", "rope"]

def quit():
        print ("You Choose To Flee")
        print ("Game Over\n")
        return False

def player_stats():
          print("You are:")
          for key, value in hero_stats.items():
                print(f"{key} : {value}")

def player_move():
     pass

def player_attack():
     pass

def player_heal(item_name):

    
      if (hero_inventory.count("health potion") <=0):
          print(f"you dont have any {item_name}")
          return

      print(f"You've used a {item_name} and restored {health_potion_strength} Health")
      hero_stats ["health"] = hero_stats ["health"] + health_potion_strength
    
      if (hero_stats["health"] >= hero_max_health):
          print("You've reached max health")
          hero_stats["health"] = hero_max_health

           print (f"Your health is now {hero_stats['health']}")
           hero_inventory.remove("health potion")
           print(f"your inventory is now{hero_inventory}")


def use_item():
     item_name = input(f"what item would you like to use?{hero_inventory}\n")
     print(f"The item you want to use is {item_name}")
     match item_name:
           case "sword":
                 pass
           case "health potion":
                   player_heal(item_name)


           case "rope":
                 pass
           case _:
                 print(f"{item_name} is not in your inventory")

#temporary function
def damage_player():
      hero_stats["health"] = hero_stats["health"] - 10
      print (f"your health is now {hero_stats['health']}")

isPlaying = True;

hero_stats["name"] = input ("what is your name?\n")
player_stats()


while (isPlaying):
    
    action = input ("\nSelect Action: Attack, Move, Use or Flee\n").lower()

    print(f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit()
    
    elif (action == "attack"):
          #player_attack()
          damage_player()
          
    elif (action == "use"):
          use_item()


    elif (action == "move"):
          player_move()

    else:
          print (f"{action} is an invalid action")

