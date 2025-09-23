hero_stats= {
        "name" : "hero",
        "strength" : 7,
        "health" : 100.0,
}

def quit():
        print ("You Choose To Flee")
        print ("Game Over\n")
        return False

def player_stats():
          print("You are;")
          for key, value in hero_stats.items():
                print(f"{key} : {value}")

def player_move():
     pass

def player_attack():
     pass

isPlaying = True;

while (isPlaying):

    hero_stats["name"] = input ("what is your name?\n").lower
    
    player_stats()

    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit()
    
    elif (action == "attack"):
          player_attack()
    elif (action == "move"):
          player_move()
    else:
          print (f"{action} is an invalid action")

