# name: Derek D'Arcy
# Description: This program takes user input and outputs a batting average calculation

# Takes user input for each field
name = input('Enter the name of the player: ')
jersey_number = int(input('Enter the players jersey number: '))
batted = int(input('Enter the number of times this player has batted: '))
hits = int(input('Enter the number of times this player has hit the ball: '))

# Prints user input
print(f'Player name: {name}')
print(f'Player Jersey Number: {jersey_number}')

# Performs calculation to get batting average as a percentage
batting_average = round((hits/batted)*100, 2)

# Prints out batting average
print(f'Batting average: {batting_average}%')
