import random


choices =["ROCK", "PAPER", "SCISSORS"]


while True:
    while True:
        player_choice = input("Please choose rock, paper or scissors\n")
        if player_choice.upper() not in choices:
            print("That's not a legal move")
            continue
        else:
            player_choice = player_choice.upper()
            break

    #randomly generate a choice for the computer
    comp_choice = random.choice(choices)

    #compare the two and determine a winner
    if player_choice == "ROCK":
        if comp_choice == "PAPER":
            print("Paper beats Rock, the computer wins")
        elif comp_choice == "SCISSORS":
            print("Rock beats Scissors, you win")
        else:
            print("You both chose Rock, it's a draw")
    elif player_choice == "PAPER":
        if comp_choice == "SCISSORS":
            print("Scissors beats paper, the computer wins")
        elif comp_choice == "ROCK":
            print("Paper beats Rock, you win")
        else:
            print("You both chose Paper, it's a draw")
    else:
        if comp_choice == "ROCK":
                print("Rock beats Scissors, the computer wins")
        elif comp_choice == "PAPER":
            print("Scissors beats Paper, you win")
        else:
            print("You both chose Scissors, it's a draw")
            
    while True:
        choice = input("Would you like to play again? Y/N\n")
        if choice.upper() == "Y":
            break
        elif choice.upper() == "N":
            print("Goodbye")
            exit()
        else:
            continue


