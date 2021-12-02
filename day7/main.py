import hangman_art as art
import hangman_words as words
import random


letter_list = list("abcdefghijklmnopqrstuvwxyz")

guessed_letter_list = []

chosen_word = list(random.choice(words.word_list))
print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display.append("_")

print(display)

game_over = False
is_winner = False

lives = len(art.stages) - 1
print('lives: ' + str(lives))
print(art.logo)
print("Pssst, the solution is "+''.join(chosen_word)+".")

def get_guess():
    while True:
        g = input("Guess a letter: ").lower()
        if g in guessed_letter_list:
            print("You have already guessed the letter "+g+".")
        elif g not in letter_list:
            print("The guess has to be a single letter. Please try again.")
        else:
            return g

while not game_over:
   
    guess = get_guess()

    guessed_letter_list.append(guess)

    # evaluate the guess, and update the display list if needed
    good_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            # set to True if there was at least one match
            good_guess = True

    if good_guess:
        # check for win condition
        # count the "_" in the display list, none means all characters have been guessed already
        if display.count("_") == 0:
            is_winner = True
            game_over = True
    else:
        print("The letter "+guess+" is not in the word. You lose a life.")
        lives -= 1
        # check for game over condition
        if lives == 0:
            game_over = True

    # print the display list as a string and the corresponding "art"
    print(" ".join(display))
    print(art.stages[lives])

# after game over, print the final result
if is_winner:
    print("You win!")
else:
    print("Game over.")