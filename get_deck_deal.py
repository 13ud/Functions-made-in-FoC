from itertools import cycle
from itertools import product

def get_deck():
    """ Create a list of 52 cards . """
    suits = 'CDHS '
    values = '234567890 JQKA '
    deck = product(values, suits)
    return ([''.join(c) for c in deck])

def deal():
    """Put cards in 4 equal piles. """
    deck = get_deck()
    hands = [[],[],[],[]]
    players = cycle(hands)
    for card in deck:
        player = next(players)
        player.append(card)
    return hands

print(deal()[0])
print(deal()[1])
print(deal()[2])
print(deal()[3])

from itertools import groupby

def first ( x ):
    for rank , group in groupby ( hand , first ):
        print ( f"{ rank } { list ( group )}")
    return (x[0])

