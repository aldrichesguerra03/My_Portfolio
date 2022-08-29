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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_answer = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_answer])

if user_choice >= 3 and user_choice < 0:
  print("You typed an invalid number.")
elif user_choice == 0 and computer_answer == 2:
  print("You win!")
elif user_choice == 0 and computer_answer == 1:
  print("you lose!")
elif user_choice == 1 and computer_answer == 0:
  print("You win!")
elif user_choice == 1 and computer_answer == 2:
  print("You lose!")
elif user_choice == 2 and computer_answer == 1:
  print("You win!")
elif user_choice == 2 and computer_answer == 0:
  print("You lose!")
elif user_choice == computer_answer:
  print("It's a draw!")

  






