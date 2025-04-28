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

name_of_games = ['Rock', 'Paper' 'Scissors']
game = [rock, paper, scissors]
# event = [name_of_games, game]
my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
computer_game = random.choice(name_of_games[0])
computer_choice = random.choice(game[1])
user_choice = ''
if my_choice == 0:
    user_choice = name_of_games[0]
elif my_choice == 1:
    user_choice = name_of_games[1]
elif my_choice == 2:
    user_choice = name_of_games[2]


if my_choice == 0 and computer_choice == game[2]:
    print(f'\nYou chose: {game[0]}')
    print(f'\n Computer chose: {computer_choice}')
    print('You Win!')
elif my_choice == 2 and computer_choice == game[1]:
    print(f'\nYou chose: {game[2]}')
    print(f'\n Computer chose: {computer_choice}')
    print('You Win!')
elif my_choice == 1 and computer_choice == game[0]:
    print(f'\nYou chose: {game[1]}')
    print(f'\n Computer chose: {computer_choice}')
    print('You Win!')
else:
    print(f'\nYou chose: {user_choice}')
    print(f'\n Computer chose: {computer_choice}')
    print('You Lose!')

