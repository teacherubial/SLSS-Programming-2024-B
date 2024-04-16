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
        self.actual_cry = "Rooooooooooooooar"

    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
            - As a string the sound a pokemon makes
            - e.g. "{name} says, "{actual_cry}"""

        return f'{self.name} says, "{self.actual_cry}!"'

    def consume(self, item: str) -> str:
        """Pokemon consumes the item

        Params:
            - the item the pokemon consumes

        Returns:
            - the response of the pokemon
        """
        if item.lower() == "berry":
            return f'{self.name} eats the berry and says, "YUM!"'
        elif item.lower() == "potion":
            return f"{self.name} feels much better after the potion!"
        else:
            return f"{self.name} batted away the {item}!"


def main():
    # Create two Pokemon

    # Create something 'Pikachu'-like
    pokemon_one = Pokemon()

    # Access the properties inside pokemon_one
    # Print the name of pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)

    # Change the values of the propeties
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25

    # Print the values from pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)

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

    # Test Pokemon cry
    print(pokemon_one.cry())
    print(pokemon_two.cry())

    # Test Pokemon consume
    print(pokemon_one.consume("berry"))
    print(pokemon_one.consume("potion"))
    print(pokemon_one.consume("poison"))  # mr. ubial doesn't condone
    print(pokemon_two.consume("berry"))


if __name__ == "__main__":
    main()
