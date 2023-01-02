import random

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

my_choice = input('Please make your choice: rock,paper or scissors?:')
if (my_choice != 'rock' and my_choice !='paper' and my_choice != 'scissors'):
    


    if my_choice == computer_choice:
        winner = 'Tie'
elif computer_choice == 'paper' and my_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and my_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and my_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Computer' or winner == 'User':
    print('The', winner, 'wins!')
else:
    print('There is no winner, it is a Tie')
    