import random
# Rock
rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
your_choice = input("Choose Between rock, paper & Scissors ").upper()
if your_choice == "ROCK":
    expression = 1
    print(rock)
elif your_choice == "PAPER":
    expression = 2
    print(paper)
else:
    expression = 3
    print(scissors)

random_integer =  random.randint(1,3)
if random_integer == 1:
    print(rock)
elif random_integer == 2:
    print(paper)
else:
    print(scissors)
    
if expression == 1 & random_integer == 3:
    print("You Win")
elif expression == 2 & random_integer == 1:
    print("You Win")
elif expression == 3 & random_integer == 2:
    print("You Win")
else:
    print("You lost")
