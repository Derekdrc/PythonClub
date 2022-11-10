"""
name: Derek D'Arcy
Description: This program plays a game of war between two players
"""

import random


first_player = input('Please enter the name of player 1: ')
second_player = input('Please enter the name of player 2: ')

player1_count = 0
player2_count = 0

while player1_count < 10 and player2_count < 10:
    num1 = random.randrange(1, 13)
    num2 = random.randrange(1, 13)

    print(f'{first_player} drew a {num1}')
    print(f'{second_player} drew a {num2}')
    if num1 > num2:
        player1_count += 1
        print('')
    elif num2 > num1:
        player2_count += 1
        print('')
    else:
        print('The hand is a draw\n')

print('\n\nFinal Score: ')
print(f'{first_player} ended with {player1_count} points')
print(f'{second_player} ended with {player2_count} points\n')

if player1_count > player2_count:
    print(f'{first_player} is the winner!')
else:
    print(f'{second_player} is the winner!')
