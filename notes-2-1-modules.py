# Lists and Modules
# Author: Ubial
# 8 March 2024 - Mrs. Ubial's Birthday

import collections
import random


def coin_flip():
    # Return heads or tails or other?
    # Heads is any number 0 to 0.499999999
    # Tails is any number from 0.5 to 0.999991
    # Other is any number greater than 0.999991
    roll = random.random()  # 0.0 -> 1.0

    if roll < 0.5:
        return "heads"
    elif roll < 0.999999:
        return "tails"
    else:
        return "other?"


def card_reveal():
    # Reveal a "card" from A, 2, ..., Q, K
    roll = random.randrange(1, 14)  # (1, 14]

    if roll == 1:
        return "A"
    elif roll == 11:
        return "J"
    elif roll == 12:
        return "Q"
    elif roll == 13:
        return "K"
    else:
        return str(roll)


def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0
    other = 0

    cards_drawn = {}

    for _ in range(1_000_000):
        # Flip coin and draw card
        result = coin_flip()
        card = card_reveal()

        if card in cards_drawn.keys():
            cards_drawn[card] += 1
        else:
            cards_drawn[card] = 1

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1  # increment
        else:
            other += 1

    ordered_cards = collections.OrderedDict(sorted(cards_drawn.items()))

    for k, v in ordered_cards.items():
        print(k, v)

    # Print results
    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(f"Number of Other: {other}")


main()
