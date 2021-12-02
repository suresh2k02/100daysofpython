
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# using these to avoid writing the same "game over" message each time
game_over = False
victory = False

# area 1
print("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\".")
# lowercase the choice, just in case
choice1 = input("> ").lower()
if choice1 == "left":

    # area 2
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. "
          "Type \"swim\" to swim across.")
    choice2 = input("> ").lower()
    if choice2 == "wait":

        # area 3
        print("You arrive at the island unharmed. There is a house with 3 doors. "
              "One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?")
        choice3 = input("> ").lower()
        if choice3 == "red":
            print("It's a room full of fire.")
            game_over = True
        elif choice3 == "blue":
            print("You enter a room of beasts.")
            game_over = True
        elif choice3 == "yellow":
            print("You found the treasure!")
            victory = True
        else:
            print("You chose a door that doesn't exist.")
            game_over = True

    else:
        print("You get attacked by an angry trout.")
        game_over = True

else:
    print("You fell into a hole.")
    game_over = True

# print the final outcome
if game_over:
    print("Game over.")
elif victory:
    print("You win!")