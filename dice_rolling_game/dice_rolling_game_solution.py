# -- use Loop for continue playing until user enter n ---
  # Ask: roll the dice?
  # If user enters y
    # Generate 2 random numbers
    # Print them
  # If user enters n
    # Print thank you message
    # Termiante
  # Else
    # Print invalid choice
import random

while True:
  choice = input('Roll the dice? (y/n): ').lower() #if this is outside the loop -- will get infinite loop

  if choice == 'y':
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'Your dice ({dice1}, {dice2})')
  elif choice == 'n':
    print('Thank you for playing!')
    break
  else:
    print('Invaid choice')