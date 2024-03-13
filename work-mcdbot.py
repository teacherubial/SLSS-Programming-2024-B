# Coffee Bot

user_answer = input("Would you like fries with your meal? (Yes/No) ")

if user_answer.lower() == "yes":
    print("Here's your meal with fries!")
elif user_answer.lower() == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry. I don't understand {user_answer}.")
