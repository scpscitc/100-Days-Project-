import random
rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choice = int(input("O for rock, 1 for paper, 2 for scissors"))
computer = random.randint(0,2)
photos =[rock, paper, scissors]
if 0<=choice<=2:
    print(f"You've chosen {photos[choice]}")
else:
    print("You typed an invalid number! You lose!")
    exit()
print(f"Computer has chosen {photos[computer]}")
if choice == computer:
    print("It's a draw!")
elif choice == 0 and computer == 1:
    print("You've lost!")
elif choice == 0 and computer == 2:
    print("You've won!")
elif choice == 1 and computer == 0:
    print("You've won!")
elif choice == 1 and computer == 2:
    print("You've lost!")
elif choice == 2 and computer == 0:
    print("You've lost!")
elif choice == 2 and computer == 1:
    print("You've won!")
print("Thanks for Playing!")



