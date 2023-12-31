######################################################################
# Program: HW1d: Stick Game START
# Author: Chayadon Lappabud
# Date: July 17, 2023
# Description: competition between Human and computer ~_~
######################################################################

# Rest of the code goes here...
import random as rd

check_sticks = lambda x: True if x in [1, 2] else False  # Determine condition as an annoymous function
left_sticks = lambda x: True if x > 0 else False  # Determine condition as an annoymous function


# Define a warning function returning a message
def warning_message(index: int):
    match index:
        case 1:
            print("No, you cannot take more than 2 sticks!")
        case 2:
            print("No, you cannot take less than 1 sticks!")
        case 3:
            print("There are no enough sticks to take.")


# Define a function that has two integer parameters and returns an integer
def sticks_in_pile(sticks: int, comp_play: bool):
    # Human Action
    taken_sticks = int(input(f"{name}, how many sticks you will take (1 or 2):"))
    if check_sticks(taken_sticks) and taken_sticks <= sticks:
        sticks -= taken_sticks
        comp_play = True  # Computer is allowed to play after the human plays first.
        if left_sticks(sticks):  # If there are sticks left do this condition else END the program.
            print(f"There are {sticks} sticks in the pile")
        else:
            print(f"{name}, takes the last stick.")
            return False
    elif taken_sticks > 2:
        warning_message(1)  # Take out more than 2 sticks.
    elif taken_sticks < 1:
        warning_message(2)  # Take out less than 1 stick.
    else:
        warning_message(3)  # Take more than we have.

    # Computer Action
    if left_sticks(sticks) and comp_play:
        tmp = rd.randint(1, 2)  # Random the number of sticks.
        comp_take_sticks = min(tmp, sticks)  # Do not take more than sticks have.
        print(f"\nI, smart computer, takes:{comp_take_sticks}")
        sticks -= comp_take_sticks
        comp_play = not comp_play  # After playing the game, computer has to wait untill human play again.
        if left_sticks(sticks):  # If there are sticks left do this condition else END the program.
            print(f"There are {sticks} sticks in the pile\n")
        else:
            print("I, smart computer,  takes the last stick.")
            return True

    return sticks_in_pile(sticks, comp_play)


pile = int(input("How many sticks (N) in the pile : "))
print(f"There are {pile} sticks in the pile.")
name = input("What is your name : ")

winner = sticks_in_pile(pile, False)  # Who's gonna win this game??

# Announce the winner
if winner:
    print(f"\n{name} win  ( I, smart computer,  am sad T_T)")
else:
    print("\nI, smart computer, win  !!!!")
