import random

computer_choice = random.randint(1, 100)
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess < computer_choice:
        print("Your guess is too low. Try again!")
    elif user_guess > computer_choice:
        print("Your guess is too high. Try again!")
    elif user_guess == computer_choice:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    

