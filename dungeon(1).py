from hero_redo import Hero

# TODO 
#    1. Assign hero variables for: 
    #  attack moves
    #  & their damage values,
    #  inventory.​
#    2. Track monsters & their health: goblin:30, dragon: 200 etc.​
#    3. Display hero & monster stats at the start.​
#    
#    4. Allow for inputs & functions for:​
        #    Attacking​
        #    Using an item​
#    5. Create a graphical grid representation of the world, with the player's position indicated, add a MOVE input to move the player's position on the grid.​


def quit ():
    print ("You Chose To Flee")
    print ("GAME OVER")
    return False

    # TODO
    # Make sure that if the player has 100 health and they try to use a potion, 
    # The potion does not get consumed.

    # Health = 100.0
    # use Health Potion
    # print -> you're already at max health. 
    # DO NOT remove the health potion.

    if (hero_stats["health"] >= hero_max_health):
        print ("You've reached Max health")
        hero_stats["health"] = hero_max_health

    print (f"Your Health is now {hero_stats['health']}")
    hero_inventory.remove("health potion")
    print(f"Your inventory is now {hero_inventory}")

    # make sure it doesn't go above max health

# Temporary Function
def main():
    isPlaying = True

    hero = Hero(0,0)

    while (isPlaying):    

        action = input("\nSelect Action: Attack, Move, Use or Flee\n").lower()
        print (f"Player Action: {action}")

        print(f"You have: {hero.inventory}")

        if (action == "flee"):
            isPlaying = quit() #<-- isPlaying = False
        elif (action == "attack"):
            #player_attack()
            hero.damage_player() # temporary
        elif (action == "use"):
            item_name = input(f"What item do you want to use? {hero.inventory}\n").lower()
            hero.use_item(item_name)
        elif (action == "move"):
            hero.move()
        else:
            print (f"{action} is an invalid action")








if __name__ == "__main__":
    main()