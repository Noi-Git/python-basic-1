import random

number = int(input('How many dice you want to roll? '))

def rolling(number):
  count = 0
  while True:
    dices = {}
    for dice in range(number):
      dices[dice+1] = random.randint(1, 6)
    print()

    roll_dice = input('\nRoll the dice? y/n: ').lower()
    if roll_dice == 'y':
      count = count + 1
      for key, value in dices.items():
        print(f'{value} ',end='')
    elif roll_dice == 'n':
      print("Thank you for playing.")
      break
    else:
      print('Please enter "y" or "n"')
  print(f'Your roll dice {count} times.')

rolling(number)


