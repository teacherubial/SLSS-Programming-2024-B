# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and functions together


# Create a class that represents a Pokemon
class Pokemon:  # always name classes with capital
    def __init__(self):
        """Constructor: contains all properties
        of a Pokemon. It also contains the default
        state of the properties.
        """
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "Normal"


def main():
    # Create two Pokemon

    # Create something 'Pikachu'-like
    pokemon_one = Pokemon()

    # Access the properties inside pokemon_one
    # Print the name of pokemon_one
    # print(pokemon_one.name)
    # print(pokemon_one.type)

    # Change the values of the propeties
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25

    # Print the values from pokemon_one
    # print(pokemon_one.name)
    # print(pokemon_one.type)

    # TODO: Create something 'Squirtle'-like
    #  - Create a new Pokemon object
    #      - Store this in variable pokemon_two
    #  - Squirtle's Pokedex id is 4
    #  - Squirtle's type is Water

    pokemon_two = Pokemon()
    pokemon_two.name = "Squirtle"
    pokemon_two.type = "Water"
    pokemon_two.id = 4

    # To test, print out all of squirtle's properties
    print(pokemon_two.name)
    print(pokemon_two.id)
    print(pokemon_two.type)


if __name__ == "__main__":
    main()
