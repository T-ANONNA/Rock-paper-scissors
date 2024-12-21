import random

scissors='''  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

game_images=[rock,paper,scissors]
user_Choice=int(input("What do you choose?Type 0 for rock, 1 for paper or 2 for scissors\n"))
print(game_images[user_Choice])
comp_choice=random.randint(0,2)
print("computer chose: ")
print(game_images[comp_choice])
if user_Choice>=3 or user_Choice<0:
    print("You typed an invalid number. You lose!")
elif user_Choice==0 and comp_choice==2:
    print("you win")
elif comp_choice>user_Choice:
    print("You lose")
elif user_Choice>comp_choice:
    print("You win.")
elif comp_choice==user_Choice:
    print("It's a draw!")    
  