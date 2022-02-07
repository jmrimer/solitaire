import unittest

from gameplay.Deck import Deck, Suit


def count_suit(deck, suit):
    suits = sum(card.suit == suit for card in deck.cards)
    return suits


class MyTestCase(unittest.TestCase):
    def test_create_deck_of_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.test_suits(deck)
        self.test_ranks(deck)

    def test_ranks(self, deck):
        for rank in range(1, 13 + 1):
            rank_count = sum(card.rank == rank for card in deck.cards)
            self.assertEqual(rank_count, 4)

    def test_suits(self, deck):
        self.assertEqual(count_suit(deck, Suit.CLUB), 13)
        self.assertEqual(count_suit(deck, Suit.DIAMOND), 13)
        self.assertEqual(count_suit(deck, Suit.HEART), 13)
        self.assertEqual(count_suit(deck, Suit.SPADE), 13)


# count aces, etc.

if __name__ == '__main__':
    unittest.main()
