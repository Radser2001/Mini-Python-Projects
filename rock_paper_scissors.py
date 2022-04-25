import random

print('''
            #################################
                ROCK, PAPER, SCISSORS!!!
            #################################
''')

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("It's a draw!")
        user_wins += 0

    elif user_input == "paper" and computer_pick == "paper":
        print("It's a draw!")
        user_wins += 0

    elif user_input == "scissors" and computer_pick == "scissors":
        print("It's a draw!")
        user_wins += 0
        
    
    else: 
        print("You lost!")
        computer_wins += 1

print("\n-------You won", user_wins, "times.-------")
print("-------Computer won", computer_wins, "times.-------")
print("\nGoodbye!")