import random

  # add ask user how many dice they want to play?
  # add keeps track of how many times the user rolled the dice

# count = 0
# dices = {}

# number = int(input('How many dice you want to roll? '))
# for dice in range(number):
#   dices[dice+1] = random.randint(1, 6),random.randint(1, 6)
  # print(4dices)

# for key, value in dices.items():
#   print(value, end='')

# use the number the user provide to multiply the dice -- to create dices
# for dice in range(number):
#   number_dice = dices.update('random.randint(1, 6)' * number)

count = 0
number = int(input('How many dice you want to roll? '))
while True:
  dices = {}
  for dice in range(number):
    # dices[dice+1] = random.randint(1, 6),random.randint(1, 6)
    dices[dice+1] = random.randint(1, 6)
    print(f'=== {dices[dice+1]} ===')
  print(f'---- {dices}')
  print()

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
print(f'Your roll dice {count} times.')

