import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def get_player_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def display_score(wins, losses, ties):
    print(f"\nScore:\nWins: {wins}\nLosses: {losses}\nTies: {ties}\n")

def main():
    wins = 0
    losses = 0
    ties = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == 'win':
            print("You win!")
            wins += 1
        elif result == 'lose':
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        display_score(wins, losses, ties)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()