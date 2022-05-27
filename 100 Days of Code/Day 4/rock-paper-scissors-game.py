import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_is_on = True
game_images = [rock, paper, scissors]
player_wins = 0
computer_wins = 0

while game_is_on:
    player_choice = int(input("Please choose 0 for Rock, 1 for Paper, and 2 For Scissors: \n "))
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number, you lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
        player_wins = player_wins + 1
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
        computer_wins = computer_wins + 1
    elif computer_choice > player_choice:
        print("You lose")
        computer_wins = computer_wins + 1
    elif player_choice > computer_choice:
        print("You win!")
        player_wins = player_wins + 1
    elif computer_choice == player_choice:
        print("It's a draw")
    print(f"Computer Wins:{computer_wins}, Player Wins: {player_wins}")

    end_game = input(" Do you Wish to Continue Playing y or n: \n")

    if end_game == "n":
        game_is_on = False
