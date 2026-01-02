# Assigning numeric values to each choice for easier comparison logic
# Snake = 1, Water = -1, Gun = 0
snake = 1
water = -1
gun = 0

'''
The above assignments define a scoring system:
Snake beats Water  -> 1 beats -1
Water beats Gun    -> -1 beats 0
Gun beats Snake    -> 0 beats 1
'''

import random

# This function randomly selects the computer's move
# It returns one of the predefined numeric values: -1, 0, or 1
def generate_randon():
    Value = random.choice([-1,0,1])
    return Value

# Computer's choice is generated once when the program starts
computer = generate_randon()

# This function validates user input by checking if the key exists in dictionary d1
# If valid, it returns the mapped numeric value
def varify(d1, key):
    if key in d1:
        return d1[key]
    else:
        print("Invalid input")

# This function converts numeric values back into readable words
# Used only for displaying results to the user
def varify_reverse(d2, key):
    if key in d2:
        return d2[key]
    else:
        return "wrong input"
    

# Mapping user input characters to their corresponding numeric values
d1 = { "s":1, "w":-1, "g":0 }

# Reverse mapping to convert numeric values into readable form
reverse_dict = { 1:"Snake", -1:"Water", 0:"Gun"}

# Taking user input and converting it to lowercase for consistency
youstr = input("Your choice (s/w/g)?\n")
youstr = youstr.lower()

# Convert user's choice from character to numeric value
you = varify(d1, youstr)

# Display both user's and computer's selected choices in readable format
print(f"You chose {varify_reverse(reverse_dict, you)}, Computer chose {reverse_dict[computer]}")

# Game decision logic begins here
if(computer == you):
    # If both values are same, the match is a draw
    print("It's draw !\nHit again")
else:
    # All possible winning and losing conditions
    if(computer == -1 and you == 1):      # (computer - you) = -2 
        print("You win")
    elif(computer == -1 and you == 0):    # (computer - you) = -1
        print("You loose")
    elif(computer == 1 and you == 0):     # (computer - you) = 1
        print("You win")
    elif(computer == 1 and you == -1):    # (computer - you) = 2
        print("You loose")
    elif(computer == 0 and you == 1):     # (computer - you) = -1
        print("You loose")
    elif(computer == 0 and you == -1):    # (computer - you) = 1
        print("You win")
    else:
        # This should never happen, but is kept as a safety fallback
        print("Something wrong happen")
