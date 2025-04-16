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
if choice == 0:
    print("You have chosen")
    print(rock)
if choice == 1:
    print("You have chosen")
    print(paper)
if choice == 2:
    print("You have chosen")
    print(scissors)
if computer == 0:
    print("Computer has chosen")
    print(rock)
if computer == 1:
    print("Computer has chosen")
    print(paper)
if computer == 2:
    print("Computer has chosen")
    print(scissors)
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
else:
    print("You typed an invalid number! You lose!")
    exit()
print("Thanks for Playing!")



