import random

# count = 0
dices = {}

number = int(input('How many dice you want to roll? '))
def chosen_number(number):
    for dice in range(number):
      # dices = {}
      dices[dice+1] = random.randint(1, 6)
      print(dices)
    return dices
# chosen_number(number)

def roll(dices):
  count = 0
  while True:
    roll_dice = input('\nRoll the dice? y/n: ').lower()
    if roll_dice == 'y':
      count = count + 1
      for key, value in dices.items():
        print(value,' ',end='')
    elif roll_dice == 'n':
      print("Thank you for playing.")
      break
    else:
      print('Please enter "y" or "n"')


def rolling():
  chosen_number(number)
  roll(dices)
  print()

rolling()

# print(f'Your roll dice {count} times.')
