import random

exit = False
user_points = 0
computer_input = 0
while exit == False:
    options= ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit:")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("game ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computer input is rock")
            print("It is a tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("computer input is paper")
            print("Computer Wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("computer input is scissors")
            print("you Win")
            user_points += 1    

    elif user_input == "paper":
        if computer_input == "paper":
            print("Your input is rock")
            print("computer input is rock")
            print("you win")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("computer input is paper")
            print("it is a tie")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("computer input is scissors")
            print("Computer Wins")
            user_points += 1   

    elif user_input == "scissors":
        if computer_input == "rockr":
            print("Your input is rock")
            print("computer input is rock")
            print("you win")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("computer input is paper")
            print("you win")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("computer input is scissors")
            print("its a tie")
             

    else: user_input != "rock" or user_input != "paper" or user_input != "scissors"
    print("Invalid input")

