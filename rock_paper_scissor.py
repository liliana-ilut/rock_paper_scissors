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

# store the game images into a list
game_images = [rock, paper, scissors]

# input the user choice and store it as an integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# possible if statments for all the combinations
if user_choice >= 3 or user_choice <0:
    print("You lose, you typed an invalid number! Please try again")  
else:    
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice ==0 and user_choice == 2:
        print("You lose")    
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw, try again")    
  