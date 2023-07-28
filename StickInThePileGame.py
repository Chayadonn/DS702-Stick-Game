######################################################################
# Program: HW1d: Stick Game START
# Author: Chayadon Lappabud
# Date: July 17, 2023
# Description: competition between Human and computer ~_~
######################################################################

# Rest of the code goes here...
from random import choice, randint

<<<<<<< Updated upstream
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
=======
# Declear global variables
max_sticks = 0
pile = 0

check_sticks = lambda x: True if x in range(max_sticks+1) else False     # Determine condition as an annoymous function
left_sticks = lambda x: True if x > 0 else False                         # Determine condition as an annoymous function

# Define the function check inputed sticks.
def check_input(st:int) -> int:
    if st > 0:
        return st
    else:
        st = int(float(input("How many sticks (N) in the pile : ")))
        if st <= 0:
            print("Please, Input sticks more than 1")
        return check_input(st)


# Define the function computer_action.
def AI(pile_size:int)->int:
    tmp = pile_size % (max_sticks + 2)
    remainder = min(tmp, max_sticks)
    if pile_size <= max_sticks:
        remove_pile = max(pile_size - 1, 1)
    else:
        if remainder == 0:
            remove_pile = randint(1, max_sticks)
        else:
            remove_pile = remainder
    return remove_pile


# Define a warning function returning a message.
def warning_message(index: int, *arg):
    match index:                                                    # Matching index then print output
        case 1: print("No, you cannot take more than 2 sticks!")
        case 2: print("No, you cannot take less than 1 sticks!")
        case 3: print("There are no enough sticks to take.")
        case 4: print(f"{arg[0]}, takes the last stick.")
        case 5: print("I, smart computer, takes the last stick.")
        case 6: print(f"There are {arg[0]} sticks in the pile [{arg[0] * '|'}]\n")

>>>>>>> Stashed changes

# Define this function to check error in input from human.
def check_human_input(num:int)->int:
    while num < 0 or not check_sticks(num):
        print("Invaild input.!!")
        num = int(float(input(f"{name}, how many sticks you will take (max {max_sticks}):")))
    return num

<<<<<<< Updated upstream
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
=======

# Define a action function of human
def human_action(h_sticks:int)->int:
    # Human Action
    if left_sticks(h_sticks):                   # If there are sticks left do the rest commands.
        taken_sticks = int(float(input(f"{name}, how many sticks you will take (max {max_sticks}):")))
        taken_sticks = check_human_input(taken_sticks)      # Check input from user.
        h_sticks -= taken_sticks                # Take out the sticks.
        if left_sticks(h_sticks):               # If there are sticks left do this condition else END the program.
            warning_message(6, h_sticks)
            return h_sticks
        else:
            warning_message(4,name)
            global win
            win = False                         # If haman takes last stick then computer wins.
            return 0                            # Return 0 stick to end program.
>>>>>>> Stashed changes
    else:
        return 0
    

# Define action of the computer function 
def computer_action(c_sticks:int)->int:
    # Computer Action
<<<<<<< Updated upstream
    if left_sticks(sticks) and comp_play:
        tmp = rd.randint(1, 2)  # Random the number of sticks.
        comp_take_sticks = min(tmp, sticks)  # Do not take more than sticks have.
        print(f"\nI, smart computer, takes:{comp_take_sticks}")
        sticks -= comp_take_sticks
        comp_play = not comp_play  # After playing the game, computer has to wait untill human play again.
        if left_sticks(sticks):  # If there are sticks left do this condition else END the program.
            print(f"There are {sticks} sticks in the pile\n")
=======
    if left_sticks(c_sticks):                   # If there are sticks left do the rest commands. 
        comp_take_sticks = AI(c_sticks)         # Calls function AI to make itself more intelligent
        print(f"\nI, smart computer, takes : {comp_take_sticks}")
        c_sticks -= comp_take_sticks            # Take out the sticks.
        if left_sticks(c_sticks):               # If there are sticks left do this condition else END the program.
            warning_message(6, c_sticks)
            return c_sticks
>>>>>>> Stashed changes
        else:
            warning_message(5)
            global win
            win = True                          # If computer takes last stick then human wins.
            return 0                            # Return 0 stick to end program.
    else:
        return 0

<<<<<<< Updated upstream
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
=======

# Define a function that has an integer parameters and returns nothing. Computer play first.
def SiP_game_com_first(sticks: int):    # This is recursive function and calls other functions.
    if sticks == 0 :        
        return
    sticks = computer_action(sticks)
    sticks = human_action(sticks)
    SiP_game_com_first(sticks)


# Define a function that has an integer parameters and returns nothing. Human play first.
def SiP_game_human_first(sticks: int):  # This is recursive function and calls other functions.
    if sticks == 0 :        
        return
    sticks = human_action(sticks)
    sticks = computer_action(sticks)
    SiP_game_human_first(sticks)


if __name__ == "__main__":
    pile = check_input(0)                           # At first, there is 0 stick in pile.
    print(f"There are {pile} sticks in the pile.")  # Show sticks.
    name = input("What is your name : ")            # Input your name.
    max_sticks = int(input("How many maximum sticks you want to take : ")) # Input maximum sticks both players can take

    start = choice([1,2])                # Random who gonna play first?   
    if start == 1:
        SiP_game_human_first(pile)       # Human play first.
    else:
        SiP_game_com_first(pile)         # Com play first.

    if win:                              # Show the winner.
        print(f"\n{name} win (I, smart computer, am sad T_T)")
    else:
        print("\nI, smart computer, win  !!!!")
>>>>>>> Stashed changes
