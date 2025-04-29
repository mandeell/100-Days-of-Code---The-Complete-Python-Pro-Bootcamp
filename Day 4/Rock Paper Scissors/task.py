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

game = [rock, paper, scissors]
# event = [name_of_games, game]
my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
if my_choice >= 0 and my_choice <= 2:
    print(f'\nYou chose: \n{game[my_choice]}')

computer_choice = random.randint(0,2)
print('Computer chose: ')
print(game[computer_choice])

if my_choice >= 3 or my_choice < 0:
    print('You typed an invalid number. You Lose!')
elif my_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and my_choice == 2:
    print('You lose!')
elif computer_choice > my_choice:
    print('You lose!')
elif my_choice > computer_choice:
    print('You win!')
elif computer_choice == my_choice:
    print("It's a draw!")
