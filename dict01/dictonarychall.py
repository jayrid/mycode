#!/usr/bin/env python3
marvelchars = {
    "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
    "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
}

# Get user input for the character name
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")

# Get user input for the statistic
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")

# Check if the character exists in the dictionary
if char_name in marvelchars and char_stat in marvelchars[char_name]:
    value = marvelchars[char_name][char_stat]
    # Print the information
    print(f"{char_name}'s {char_stat} is: {value}")
else:
    print("Character or statistic not found in the dictionary.")

