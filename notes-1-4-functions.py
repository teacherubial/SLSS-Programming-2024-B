# Functions
# Author: Ubial
# 26 February 2024

# Create a function called say_hello
# When you call it, it prints Hello!


def say_hello():
    print("Hello!")


# Create a function called say_hello_params
#   The parameter we pass in is the name of
#   the person that we're greeting


def say_hello_params(name):
    print(f"Hello {name.capitalize()}!")


# Create a function that takes a number
#    It will tell you how big that number is
def how_big(num):
    if num < 0:
        return "Very small"
    if num < 10:
        return "Pretty small"
    if num < 100:
        return "Big"
    if num < 1000:
        return "Pretty big"
    return "Very big"


# Create a function called adder
#    Accept two inputs
#    Return the sum of the inputs
def adder(x: int, y: int) -> int:
    return x + y


# say_hello()
# say_hello_params("Jeffrey")
# say_hello_params("Thomas")
# say_hello_params("thomas")  # string methods
# print(how_big(-1))  # "Very small"
result = adder(100, 132)  # 232
print(result)

# result = how_big(10000)
