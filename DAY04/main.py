import random
# Rock, Paper, Scissors ASCII Art (optional but fun)
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
# Store choices in a list
choices = [rock, paper, scissors]
# User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
# Validate input
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You lose!")
else:
    print("You chose:")
    print(choices[user_choice])
    # Computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])
        # Game logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    else:
        print("You lose!")
