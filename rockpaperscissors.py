import random

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Rock, Paper, Scissors.\n")

choices = ["rock", "paper", "scissors"]

playing = True

while playing:
    player_choice = input("Type rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose: " + computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win! Rock beats scissors.")
        else:
            print("Computer wins! Paper beats rock.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win! Paper beats rock.")
        else:
            print("Computer wins! Scissors beats paper.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win! Scissors beats paper.")
        else:
            print("Computer wins! Rock beats scissors.")

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        playing = False

print("\nThanks for playing, " + name + "!")