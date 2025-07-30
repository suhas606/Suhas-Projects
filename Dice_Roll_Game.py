import random

while True:
    choice = input("roll the dice(y,n) : ") 
    if choice == "y"or choice == "Y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"you rolled {dice1} and {dice2}")
    elif choice == "n" or choice == "N":
        print("you chose not to roll the dice")
        break
        
    elif choice != "y" and choice != "n":
        print("invalid input, please enter 'y' or 'n'")
 
          