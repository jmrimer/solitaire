from enum import Enum

import numpy as np
import numpy as numpy


class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in range(1, 13 + 1):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        np.random.shuffle(self.cards)
