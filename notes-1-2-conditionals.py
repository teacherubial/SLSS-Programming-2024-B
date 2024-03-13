# Conditionals
# Author: Ubial
# 14 February 2024

# Implement the flowchart from the notes

# Create two variables, x and y
x = 1_000_000
y = -5.2

# If x is less than y, print that
# If x is greater than y, print that
# If x is equal, print that
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# Ask the user what their favourite fruit is
fave_fruit = input("What's your favourite fruit? ")
# Ask the user how old they are
user_age = input("How old are you? ")

# If they answer apple or orange
if fave_fruit == "apple" or fave_fruit == "orange":
    print("Delicious choice!")

# If they answer banana and they're 2 years old
if fave_fruit == "banana" and user_age == "2":
    print("Bananas are delicious 🍌")

