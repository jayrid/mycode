#!/usr/bin/python3

#heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
heroes = ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]
favorite_character = "Black Panther"
print(f"My favorite character is {favorite_character}!")

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.
user_input = input("Pick a number between 1 and 100: ")
user_input = int(user_input)

# PART 3
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!

nums= [1, -5, 56, 987, 0]
largest_num = max(nums)  # Using the max() function to find the largest number in the list.
print(f"The largest number in the list is: {largest_num}")


