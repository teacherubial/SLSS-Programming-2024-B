# Text/Emoji Replacer
# Author: Ubial
# 26 February 2024


# Create a function called translate
#    Accepts a string as parameter
#    From the parameter replace all 100 with 💯
#    Also replace all noodles with 🍜
#    Return the result
def translate(usr_input):
    # Your block of code goes in here
    # Delete the pass and put in your own code
    return usr_input.replace("100", "💯").replace("noodles", "🍜")


def main():
    # Get the user's input
    usr_input = input()
    # Use the translate function on the
    #    user's input
    print(translate(usr_input))


# Test cases
print(translate("Get to 100!"))
print(translate("I like noodles."))
print(translate("I love 100 noodles."))
main()
