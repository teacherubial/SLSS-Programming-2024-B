# Dictionaries
# 12 April 2024

# Big Ideas:
#   - dictionaries are a data structure
#   - dictionaries map keys to values

# Flashback to lists
person = ["John", "23 years old", "4500 1023 2222 1111"]

person_dict = {
    "name": "John",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111",
    "height": 190,
    "SIN number": "727 000 111",
}


# Get and print the person's name
print(person[0])
print(person[1])  # age?
print(person[2])  # some numbers?
print(person_dict["name"])
print(person_dict["age"])
print(person_dict["cc num"])

# Print the last thing in the list
print(person[-1])
print(person[-2])  # second to last
# print(person[10])  # break

# Iterate over the person list
#     - print each value
# for value in person:
#     print(value)

# Iterate over a dictionary
for key in person_dict:
    # Print the key and value for each key
    print(key, person_dict[key], sep=": ")

for key, value in person_dict.items():
    print(key, value, sep=": ")
