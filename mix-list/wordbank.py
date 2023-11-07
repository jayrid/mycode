#!/usr/bin/env python3

# Part 1
wordbank = ["indentation", "spaces"]

# Part 2
tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# Part 3 - Append a word to the wordbank
wordbank.append('Deja')

# Part 4 - Include numbers 0-20
num = int(input("Pick a student number (0-20): "))

# Part 5 - Convert to a string and get the student's name
choice = tlgstudents[num]
student_name = str(choice)

# Part 6 - Print the result
print(f"{student_name} always uses 4 spaces to indent.")

