# More Functions
# Author: Ubial
# 3 April 2024

# Implement stars function


def stars(num):
    """Returns specified number of *s"""
    value = ""  # placeholder for return value

    if num == 0 or num == 1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else:
        value = "Sorry, can't take negative numbers."

    return value


def biggest_of_three(num_one: int, num_two: int, num_three: int):
    """Returns the largest of three numbers"""

    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three


def pyramid(base_width: int):
    """Prints a pyramid of stars with given base

    Params:
        base_width: width of base of pyramid
    """

    for i in range(base_width):
        print(stars(i + 1))


# Multiply strings
greeting = "hello"
print(greeting * 100)

print("the quick brown fox jumps over the lazy dog" * 2)

# Tests for function
print(stars(0))
print(stars(1))
print(stars(1000))
print(stars(-1))

# Test biggest_of_three()
print(biggest_of_three(10, 1000, 10000))
print(biggest_of_three(1000, 10, 10000))
print(biggest_of_three(10000, 1000, 10))

# Test pyramid function
pyramid(1)

pyramid(5)

pyramid(20)
