import random
#------------------------------ROLL DICE------------------------------\n
def roll_dice():
    return random.randint(1,6)

#------------------------------Start Game------------------------------\n
def start_game():
    print("\n------------------------------GAME STARTED------------------------------\n")

    name=input("Enter your name: ")
    computer_score=0
    user_score=0

    rounds=3

    for i in range(1,rounds+1):
        print(f"\n------------------------------Round {i}------------------------------\n")

        input("Press Enter to roll the dice")

        user_roll=roll_dice()
        computer_roll=roll_dice()

        if user_roll > computer_roll:
            print(f"{name} rolled:", user_roll,"Computer rolled:",computer_roll)
            print(f"{name} wins")
            user_score+=1
        elif computer_roll > user_roll:
            print(f"{name} rolled:", user_roll,"Computer rolled:",computer_roll)
            print("Computer wins")
            computer_score+=1
        else:
            print(f"{name} rolled:", user_roll,"Computer rolled:",computer_roll)
            print("Draw")
            user_score+=1
            computer_score+=1

    print("\nFINAL RESULT\n")

    if user_score > computer_score:
        print(f"{name} wins")
        print(f"{name}-",user_score,"Computer-",computer_score)
    elif computer_score > user_score:
        print(f"Computer wins")
        print(f"{name}-",user_score,"Computer-",computer_score)
    else:
        print("Draw")
        print(f"{name}-",user_score,"Computer-",computer_score)

    input("Press Enter to return to main menu")
    main_menu()

#------------------------------INSTRUCTIOONS------------------------------\n
def read_instruction():
    print("\n------------------------------INSTRUCTIONS------------------------------\n")
    print("1)User and Computer both rolls the dice.")
    print("2)Highest number wins the round.")
    print("3)Game is playedd for a selected number of rounds.")
    print("4)Final winner is based on total score.")
#------------------------------MAIN MENU------------------------------
def main_menu():
    while True:
        print("\n------------------------------MAIN MENU------------------------------\n")
        print("1) Start Game ")
        print("2) Read Instruction ")
        print("3) EXIT ")

        choice=int(input("Enter your choice: "))

        if choice == 1:
            start_game()
        elif choice == 2:
            read_instruction()
        elif choice == 3:
            return
        else:
            print("Invalid Option !")
main_menu()