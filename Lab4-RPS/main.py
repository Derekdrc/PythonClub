"""
name: Derek D'Arcy
Description: This program plays a game of rock, paper, scissors between a player and a computer
"""

import random


def get_user_choice():
    """This is the function used to recieve input from the user, and returns the value that the user chose."""
    user_input = int(input("Please choose '1' for Rock, '2' for Paper, or '3' for Scissors: "))
    while user_input not in {1, 2, 3}:
        print("You did not choose an available option")
        user_input = int(input("Please choose '1' for Rock, '2' for Paper, or '3' for Scissors: "))
    return user_input


def play_game():
    """This is the main fucntion that chooses for the computer and determines a winner."""
    is_game_over = False
    while not is_game_over:
        computer_number = random.randrange(1, 4, 1)
        if computer_number == 1:
            computer_choice = "Rock"
        elif computer_number == 2:
            computer_choice = "Paper"
        elif computer_number == 3:
            computer_choice = "Scissors"
        else:
            break

        player_number = int(get_user_choice())
        if player_number == 1:
            player_choice = "Rock"
        elif player_number == 2:
            player_choice = "Paper"
        elif player_number == 3:
            player_choice = "Scissors"
        else:
            break

        print(f"Player chose {player_choice} and computer chose {computer_choice}")
        # waterfall if statement, check if tie, check if scissors beats rock, then higher number beats lower number
        if computer_number == player_number:
            print("Player and computer chose the same, try again")
        elif player_number == 1 and computer_number == 3:
            print("Player Wins!")
            is_game_over = True
        elif computer_number == 1 and player_number == 3:
            print("Computer wins!")
            is_game_over = True
        elif player_number > computer_number:
            print("Player wins!")
            is_game_over = True
        elif computer_number > player_number:
            print("Computer wins!")
            is_game_over = True
        else:
            break


play_game()
