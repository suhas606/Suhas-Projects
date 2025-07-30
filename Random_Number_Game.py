import random
computer = random.randint(1, 6)
user  = int(input("Enter a number between 1 and 6: "))
if computer == user:
    print("You win!")
    print(f"Computer rolled: {computer}")
else:
    print("You lose!")
    print(f"Computer rolled: {computer}")