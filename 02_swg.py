import random

# Generates a random move for the computer
# Returns one of: -1 (Water), 0 (Gun), 1 (Snake)
def generate_randon():
    Value = random.choice([-1,0,1])
    return Value

# Store computer's randomly selected move
computer = generate_randon()

# Validates the user's input against allowed options dictionary
# Returns the corresponding numeric value if valid
def varify(d1, key):
    if key in d1:
        return d1[key]
    else:
        print("Invalid input")

# Converts numeric game values back into readable form for display
def varify_reverse(d2, key):
    if key in d2:
        return d2[key]
    else:
        return "wrong input"
    

# Mapping of user input characters to internal numeric values
d1 = { "s":1, "w":-1, "g":0 }

# Reverse mapping used for displaying results
reverse_dict = { 1:"Snake", -1:"Water", 0:"Gun"}

# Taking user input and preparing it for processing
youstr = input("Your choice (s/w/g)?\n")
print("\n")
youstr = youstr.lower()

# Convert validated input into its numeric representation
you = varify(d1, youstr)

# Display the choices made by the user and the computer
print(f"You chose {varify_reverse(reverse_dict, you)}, Computer chose {reverse_dict[computer]}")


# List of all valid internal move values
li = [0,-1,1]

# Only proceed with the game if the user's input was valid
if you in li:
    if(computer == you):
        # Same value indicates a draw
        print("It's draw !\nHit again")
    else:
        # Core decision logic based on mathematical difference
        if((computer - you) == -1 or (computer-you) == 2):
            print("You loose")
        else:
            print("You win")
