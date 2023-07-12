# Define a function that has two integer parameters and returns an integer
def sticks_in_pile(sticks: int, count: int) -> int:
    if sticks == 0:  # If there is no sticks left end the program (Base case)
        return count  # Return (count) how many times does a user take the sticks out.
    else:
        taken_sticks = int(input(f"{name}, how many sticks you will take (1 or 2):"))
        if (
            taken_sticks in [1, 2] and taken_sticks <= sticks
        ):  # Take out one or two sticks and not more than we have.
            count += 1
            sticks -= taken_sticks
            if sticks != 0:
                print(f"There are {sticks} sticks in the pile")
        elif taken_sticks > 2:  # Take out more than 2 sticks
            print("No, you cannot take more than 2 sticks!")
        elif taken_sticks < 1:  # Take out less than 1 stick
            print("No, you cannot take less than 1 sticks!")
        else:
            print("There are no enough sticks to take.")
        return sticks_in_pile(sticks, count)


pile = int(input("How many sticks (N) in the pile : "))
print(f"There are {pile} sticks in the pile.")
name = input("What is your name : ")

times = sticks_in_pile(pile, 0)
print(f"OK. There is no stick left in the pile. You spent {times} times.")
