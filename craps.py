"""Craps

This script displays rules to play craps, then gives user three options
to Play, See Rules again, or Exit program.
"""

from random import randint

def display_rules():
    """Displays rules and wait for user to contine"""
    rules = ("\nA player rolls two dice, and the first roll is calculated. If the sum is\n"
            "7, or 11 on the first roll, then the player wins. If the sum is\n"
            "2, 3, or 12 on the first roll, then the player loses. Any other sum is\n"
            "counted as the point roll, and to win, the player must roll the point again\n"
            "before rolling a 7. If the point is rolled again before rolling a 7, then\n"
            "the player wins. If a 7 is rolled before rolling the point again, then\n"
            "the player loses.\n")
    print(rules)
    print("\nPress enter key to continue...")
    input("")


def is_float(string_value):
    """Determines if string can be converted to float value"""
    if string_value is None:
        return False
    try:
        float(string_value)
        return True
    except:
        return False
    

def is_int(string_value):
    """Determines if string represents rounded integer"""
    if is_float(string_value) and float(string_value) // 1 == float(string_value):
        return True
    else:
        return False
    

def play_game():
    """Enter Craps game and continue until user desides to exit to menu"""
    die_one = 0
    die_two = 0
    play_cash = 0
    initial_cash = 0
    wager_amount = 0
    point_number = 0
    stop_playing = ""
    
    print("\nPlease decide how many dollars you would like to play with:")
    play_cash = input()

    # Invalid cash input correction loop
    while not is_int(play_cash) or float(play_cash) < 1:
        if not is_float(play_cash):
            print("\nPlease input a valid amount:")
        elif float(play_cash) < 1:
            print("\nSorry, we do not provide credit, please input a positive amount:")
        else:
            print("\nWe only play with whole dollars, please keep your change.")
            break
        play_cash = input()
    play_cash = int(float(play_cash))
    initial_cash = play_cash
    
    # Game loops until player decides to stop or runs out of money
    while stop_playing.lower() not in ["stop", "done", "exit", "quit", "leave", "end"] and play_cash != 0:
        print("Current cash: ", play_cash)
        wager_amount = input("Please place a wager: ")

        # Invalid wager correction loop
        while not is_int(wager_amount) or float(wager_amount) < 1 or float(wager_amount) > play_cash:
            print("\nCurrent cash: ", play_cash)
            if not is_float(wager_amount):
                print("Please input a valid wager amount: ", end = "")
            elif float(wager_amount) < 1:
                print("That's not how we do wagers here, you must wager at least a dollar: ", end = "")
            elif float(wager_amount) > play_cash:
                print("You may not wager more than you have, please make a new wager: ", end = "")
            else:
                print("Your wager has been rounded down to the nearest dollar.\n")
                break
            wager_amount = input()
        wager_amount = int(float(wager_amount))

        play_cash -= wager_amount
        print()
        print("Current cash: ", play_cash)
        print("Current wager: ", wager_amount)
        print("Please make the first roll (Press Enter)")
        input()
        die_one = randint(1, 6)
        die_two = randint(1, 6)

        # win on the first roll 
        if die_one + die_two in [7, 11]:
            print("\nYou rolled {} (Die 1: {}, Die 2: {})! You win!".format(die_one + die_two, die_one, die_two))
            play_cash += (2 * wager_amount)

        # lose on the first roll
        elif die_one + die_two in [2, 3, 12]:
            print("\nYou rolled {} (Die 1: {}, Die 2:  {}). You lose.".format(die_one + die_two, die_one, die_two))

        # point on the first roll
        else:
            print("\nYou rolled {} (Die 1: {}, Die 2: {}).".format(die_one + die_two, die_one, die_two), end = " ")
            print("That number is now the point.")
            print("You must roll that number again to win!\nPress Enter to make next roll.\n")
            point_number = die_one + die_two
            input()
            die_one = randint(1, 6)
            die_two = randint(1, 6)
            while die_one + die_two not in [7, point_number]:
                print("Point: ", point_number)
                print("You rolled {} (Die 1: {}, Die 2: {}). Press Enter to make next roll.\n".format(die_one + die_two, die_one, die_two))
                input()
                die_one = randint(1, 6)
                die_two = randint(1, 6)
            if die_one + die_two == point_number:
                print("You rolled {} (Die 1: {}, Die 2: {})! You win!\n".format(die_one + die_two, die_one, die_two))
                play_cash += (2 * wager_amount)
            else:
                print("You rolled 7. You crapped out.\n")

        wager_amount =0
        print("Starting cash: ", initial_cash)
        print(" Current cash: ", play_cash)
        if initial_cash > play_cash:
            print("         down: ", initial_cash - play_cash)
        else:
            print("           up: ", play_cash - initial_cash)

        print()
        print("Press Enter to continue.")
        print('Or enter "quit" if you would like to stop playing.')
        stop_playing = input()
    
    # Game ends
    print()
    if play_cash == 0:
        print("You ran out of money. Better Luck next time")
        stop_playing = "quit"
    print("Starting cash: ", initial_cash)
    print("Current cash:  ", play_cash)
    if initial_cash > play_cash:
        print("Lost:          ", initial_cash - play_cash)
    elif initial_cash < play_cash:
        print("Gained:        ", play_cash - initial_cash)
    else:
        print("You broke even.")
    print("Thanks for playing!")   


def main():  
    print("Welcome to Craps!")

    while True:  
        print()
        print("1. Play")
        print("2. Rules")
        print("3. Exit\n")
        
        selection_choice = ""
        selection_choice = input()
        while selection_choice.lower() not in ['1', '2', '3', 'p', 'play', 'r', 'rule', 'rules', 'e', 'exit']:
            print("Please make a valid selection...")
            selection_choice = input()
        
        if selection_choice.lower() in ['1', 'p', 'play']:
            play_game()
            selection_choice = ""
        
        if selection_choice.lower() in ['2', 'r', 'rule', 'rules']:
            display_rules()
            selection_choice = ""

        if selection_choice.lower() in ['3', 'e', 'exit']:
            print("Thank you for playing\n")
            exit()

   
if __name__ == '__main__':
    main()
