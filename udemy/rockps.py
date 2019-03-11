#!/usr/bin/env python3

import random

player_1_input = input('Enter choice: ').lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    player_2_input = 'rock'
elif rand_num == 1:
    player_2_input = 'paper'
else:
    player_2_input = 'scissors'
print('computer plays ' + player_2_input)
p1 = 'player one wins'
p2 = 'player two wins'

if player_1_input == 'rock' and player_2_input == 'scissors':
    print(p1)

elif player_1_input == 'rock' and player_2_input == 'paper':
    print(p2)

elif player_1_input == 'paper' and player_2_input == 'rock':
    print(p1)

elif player_1_input == 'paper' and player_2_input == 'scissors':
    print(p2)

elif player_1_input == 'scissors' and player_2_input == 'paper':
    print(p1)

elif player_1_input == 'scissors' and player_2_input == 'rock':
    print(p2)

elif player_1_input == player_2_input:
    print('draw, try again')

else:
    print('something went wrong')
