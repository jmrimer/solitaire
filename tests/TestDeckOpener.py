import unittest

from gameplay.Deck import Deck, Suit


def count_suit(deck, suit):
    suits = sum(card.suit == suit for card in deck.cards)
    return suits


class MyTestCase(unittest.TestCase):
    def test_create_deck_of_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.test_all_suits_in_deck(deck)
        self.test_all_ranks_in_deck(deck)

    def test_shuffle(self):
        shuffled_deck = Deck()
        original_deck = shuffled_deck.cards.copy()
        self.assertEqual(shuffled_deck.cards, original_deck)
        shuffled_deck.shuffle()
        self.assertNotEqual(shuffled_deck.cards, original_deck)

    def test_all_ranks_in_deck(self, deck):
        for rank in range(1, 13 + 1):
            rank_cards = set(card for card in deck.cards if card.rank == rank)
            self.assertEqual(len(rank_cards), 4)

    def test_all_suits_in_deck(self, deck):
        self.assertEqual(count_suit(deck, Suit.CLUB), 13)
        self.assertEqual(count_suit(deck, Suit.DIAMOND), 13)
        self.assertEqual(count_suit(deck, Suit.HEART), 13)
        self.assertEqual(count_suit(deck, Suit.SPADE), 13)


# count aces, etc.

if __name__ == '__main__':
    unittest.main()
