import random
import os
import sys
import time
from words import word_list
from stages import logo, stages


def choose_letter():
    while True:
        letter = input("Guess a letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            os.system('cls')
            return letter
        else:
            continue


def hash_word_display(chosen_word):
    hashed_word = []
    for _ in range(len(chosen_word)):
        hashed_word.append("_")
    return hashed_word


def start_new_game():
    user_choice = input("Do you want to play again? (Y/N) ").lower()
    if user_choice == "y":
        os.system('cls')
        main()
    elif user_choice == "n":
        sys.exit()


def main():

    ### dev assist
    # print(f'The solution is {chosen_word}.')

    lives = 7

    # welcome screen
    print(logo)
    print("Loading new word. . . ")
    time.sleep(2)
    os.system('cls')

    # generate word
    chosen_word = random.choice(word_list)
    print(stages[lives])
    display = hash_word_display(chosen_word)
    print(display)
    
    # main game
    while "_" in display:
        guess = choose_letter()
        
        if guess in display:
            print(stages[lives])
            print(f"You already guessed '{guess}'.")

        elif guess in chosen_word:
            print(stages[lives])
            print(f"Correct guess! Letter '{guess}' is part of the word!")
            for n in range(len(chosen_word)):
                if guess in chosen_word[n]:
                    display[n] = guess
                    
        elif guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            if lives > 0:
                print(f"Letter '{guess}' is not in the word. Lives left: " + str(lives))
            if lives == 0:
                print(f"Gave over. The word was '{chosen_word}'.")
                start_new_game()
        print(display)

    else:
        print("You win!")
        start_new_game()
        
        
if __name__ == "__main__":
    main()