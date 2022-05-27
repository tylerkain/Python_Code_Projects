import random
import word_list
import hangman_art
chosen_word = random.choice(word_list.word_list)
display_list = []
game_lives = 6
letter = ""
user_guess = 0
game = True

print(hangman_art.logo)

for _ in range(len(chosen_word)):
    display_list += "_"

while game is True:
    player_guess = input("Guess A letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == player_guess:
            display_list[position] = letter
    if "_" not in display_list:
        game = False
    if player_guess not in chosen_word:
        game_lives -= 1
    if game_lives == 0:
        game = False
        print(chosen_word)
    print(hangman_art.stages[game_lives])
    print(display_list)
