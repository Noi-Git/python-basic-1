'''
The program will run until user teminated by type "no"
1. Ask: roll dice?
  if yes -- generate random number -- print the result
  if no  -- terminate the program. -- print thank you for playing
  else -- print invalid choice
'''
import random

while True:
    user_ans = input('Do you want to play dice? ').lower()
    if user_ans == 'yes':
        dice = (f'({random.randint(1, 6)},{random.randint(1, 6)})')
        print(f'You got: {dice}')
    elif user_ans == 'no':
        print('Thank you for playing')
        break
    else:
        print("Please enter yes or no")
