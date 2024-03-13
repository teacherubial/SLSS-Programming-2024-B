# Chatbot
# Author: Ubial
# Mrs. Ubial's Birthday

# A basic chatbot

import random
import time

# 1. Greets the user
print("Hello there!")
time.sleep(1.5)

# 2. Asks them, "how are you?" or something like it
print("How are you doing?")
user_feeling = input().strip(",.?! ").lower()
time.sleep(1.5)

# 3. Responds with a general statement
#       that is randomly chosen
#         - create a list of possible responses
#         - randomly choose a response
#         - print that response

good_possible_resp = [
    "I'm really happy for you.",
    "That's really good news!!",
    "That's awesome.",
]
bad_possible_resp = ["I'm sorry you're feeling that way.", "There, there.", "🥺"]
neutral_possible_resp = ["Thanks for sharing that with me.", "Cool!", "🤜🤛"]

if user_feeling == "good" or user_feeling == "great":
    print(random.choice(good_possible_resp))
elif user_feeling == "bad" or user_feeling == "not too good":
    print(random.choice(bad_possible_resp))
else:
    print(random.choice(neutral_possible_resp))
time.sleep(1.5)

# 4. Says goodbye
print("Well thank you for your time! 😊")
