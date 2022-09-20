# File: FindTwoLargest.py
# Name: Sergio Ley Languren

"""In a list of integers, this module will find the two largest numbers."""

# variable definition

input_msg = "? "

# ------------
def find_two_largest():
    """Finds the two largest number in the provided list."""
    # Introduction
    print("This program finds the two largest integers")

    # prompt and user input loop
    space_input = False

    int_list = []

    print("Enter a blank line to stop")

    while not space_input:
        inp = input(input_msg)
        if inp == "":
            space_input = True
        else:
            int_list.append(int(inp))
    # calculations
    int1 = max(int_list)
    int_list.remove(int1)
    int2 = max(int_list)
    
    # result 
    print(f"The largest value is: {int1}")
    print(f"The second largest value is: {int2}")

# Startup code

if __name__ == "__main__":
    find_two_largest()
