import random
computer_choice = random.choice (['rock', 'paper', 'scissors'])

while True:
    user_choice = input("Enter rock, paper, or scissors : ")
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.") 
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(f"You win! {user_choice} beats {computer_choice}.")
    elif (user_choice == "rock" and computer_choice == "paper") or \
         (user_choice == "scissors" and computer_choice == "rock") or \
            (user_choice == "paper" and computer_choice == "scissors"):
        print(f"You lose! {computer_choice} beats {user_choice}.")
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

          