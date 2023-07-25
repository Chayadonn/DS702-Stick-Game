######################################################################
# Program: HW1d: Stick Game START
# Author: Chayadon Lappabud
# Date: July 24, 2023
# Description: competition between Human and computer ~_~
######################################################################

# Rest of the code goes here...
import random as rd

max_sticks = 5

check_sticks = lambda x: True if x in range(max_sticks+1) else False     # Determine condition as an annoymous function
left_sticks = lambda x: True if x > 0 else False                       # Determine condition as an annoymous function


# Define the function check sticks inputed
def check_input(st:int) -> int:
    if st > 0:
        return st
    else:
        st = int(float(input("How many sticks (N) in the pile : ")))
        if st <= 0:
            print("Please, Input sticks more than 1")
        return check_input(st)  


# Define the function computer_action 
def AI(pile_size:int)->int:
    remainder = min(pile_size % (max_sticks + 2), max_sticks)
    if pile_size <= max_sticks:
        remove_pile = max(pile_size - 1, 1)
    else:
        if remainder == 0:
            # Remove any number of stones to keep the pile size a multiple of 4
            remove_pile = rd.randint(1, max_sticks)
        else:
            # Remove stones to make the pile size a multiple of 4
            remove_pile = remainder

    return remove_pile


# Define a warning function returning a message
def warning_message(index: int):
    match index:
        case 1: print("No, you cannot take more than 2 sticks!")
        case 2: print("No, you cannot take less than 1 sticks!")
        case 3: print("There are no enough sticks to take.")


# Define a function that has two integer parameters and returns an integer
def sticks_in_pile(sticks: int, comp_play: bool):
    # Human Action
    taken_sticks = int(input(f"{name}, how many sticks you will take (1 or 2):"))

    if check_sticks(taken_sticks) and taken_sticks <= sticks:
        sticks -= taken_sticks
        comp_play = True         # Computer is allowed to play after the human plays first.
        if left_sticks(sticks):  # If there are sticks left do this condition else END the program.
            print(f"There are {sticks} sticks in the pile [{sticks * '|'}]")
        else:
            print(f"{name}, takes the last stick.")
            return False
    # elif taken_sticks > max_sticks:
    #     warning_message(1)  # Take out more than 2 sticks.
    # elif taken_sticks < 1:
    #     warning_message(2)  # Take out less than 1 stick.
    # else:
    #     warning_message(3)  # Take more than we have.

    # Computer Action
    if left_sticks(sticks) and comp_play:
        tmp = AI(sticks)        # Random the number of sticks.
        comp_take_sticks = tmp  # Do not take more than sticks have.
        print(f"\nI, smart computer, takes:{comp_take_sticks}")
        sticks -= comp_take_sticks     
        comp_play = not comp_play   # After playing the game, computer has to wait untill human play again.
        if left_sticks(sticks):     # If there are sticks left do this condition else END the program.
            print(f"There are {sticks} sticks in the pile [{sticks * '|'}]\n")
        else:
            print("I, smart computer,  takes the last stick.")
            return True

    return sticks_in_pile(sticks, comp_play)


if __name__ == "__main__":
    pile = check_input(20)  # At first, there is 0 stick in pile
    print(f"There are {pile} sticks in the pile.")
    # name = input("What is your name : ")
    name = "Xia O"
    winner = sticks_in_pile(pile, False)  # Who's gonna win this game??

    # Announce the winner
    if winner:
        print(f"\n{name} win  ( I, smart computer,  am sad T_T)")
    else:
        print("\nI, smart computer, win  !!!!")
