import random
from HangManWords import word_list
from HangManArt import stages
from HangManArt import logo
print(logo)

end_game = False
lives = 7
chosen_word = random.choice(word_list)
length_of_word = len(chosen_word)
guesses = []

display = []
for blank in chosen_word:
    display += "_"
print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()

    # Correct guesses - Replace the '_' with letter
    for position in range(length_of_word): # Iterates through each letter of chosen word
        letter = chosen_word[position] # Where position will increment starting from 0
        if letter == guess:
            display[position] = letter
    print(display)

    # Wrong guesses
    if guess not in chosen_word and guess not in guesses:
        lives -= 1
        print(f"Your guess '{guess}' is not in the word, you lose a life")
        print(stages[lives]) # Prints each image according to their index in ASCII list
        if lives == 0:
            end_game = True
            print("You lose")

    if "_" not in display:
        end_game = True
        print("You win")

    # If guess has already been made
    if guess in guesses:
        print("You've guessed this letter already")
    guesses.append(guess)

