import random

while True:
  # ask for user input
    # check if user input y -- continue, n -- break
    # -- generate first random number
    # -- generate second random number
  roll_dice = input('Roll the dice? y/n: ').lower()


  if roll_dice == 'y':
    first_number = random.randint(1, 6)
    second_number = random.randint(1,6)
    print(f'You dice ({first_number}, {second_number})')
  elif roll_dice == 'n':
    print("Thank you for playing.")
    break
  else:
    print('Please enter "y" or "n"')

  # print(f'Your dice outside is ({first_number}, {second_number})') #this will always print the last result