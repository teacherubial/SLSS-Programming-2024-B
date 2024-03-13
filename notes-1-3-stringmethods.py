# Methods - String Methods
# Author: Ubial
# 21 February 2024

# Ask the user what the weather is
user_reply = input("What is the weather like? ")

# If they answer rainy, say
# bring an umbrella
if user_reply.strip(" !.?,").lower() == "rainy":
    print("Bring an umbrella ☂️!")
else:
    print("Sorry I didn't understand what you said.")
