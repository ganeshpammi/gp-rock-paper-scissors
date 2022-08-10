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

#Write your code below this line 👇
import random

user_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

collection = [rock, paper, scissors]

print(collection[user_input])

print("Computer chose:")

comp_choice = random.randint(0, 2)

print(collection[comp_choice])

if user_input == comp_choice:
    print("It's a draw")
elif user_input == 0:
    if comp_choice == 1:
        print("You lose!")
    else:
        print("You win!")
elif user_input == 1:
    if comp_choice == 2:
        print("You lose!")
    else:
        print("You win!")
elif user_input == 2:
    if comp_choice == 1:
        print("You lose!")
    else:
        print("You win!")
