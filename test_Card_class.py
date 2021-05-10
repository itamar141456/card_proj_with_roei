from unittest import TestCase
from Card_class import Card

class TestCard(TestCase):

    def setUp(self):
        self.card1 = Card({"Diamonds": 1}, 1)
        self.card2 = Card({"Diamonds": 1}, 10)
        self.card3 = Card({"Spades": 2}, 8)
        self.card4 = Card({"Spades": 2}, 1)
        self.card5 = Card({"Harts": 3}, 1)
        self.card6 = Card({"Harts": 3}, 13)
        self.card7 = Card({"Clubs": 4}, 2)
        self.card8 = Card({"Clubs": 4}, 13)



    def test_calc(self):
        """
        check that tha calculations are correct
        """
        # same suit, different value
        self.assertTrue(self.card1 > self.card2)
        self.assertTrue(self.card4 > self.card3)
        self.assertTrue(self.card5 > self.card6)
        self.assertTrue(self.card8 > self.card7)

        # different suit, same value
        self.assertTrue(self.card4 > self.card1)
        self.assertTrue(self.card5 > self.card4)
        self.assertTrue(self.card8 > self.card6)

        # different suit, different values
        self.assertTrue(self.card1 > self.card3)
        self.assertTrue(self.card6 > self.card3)
        self.assertTrue(self.card6 > self.card7)

        # same suit, same value
        card_eq = Card({"Clubs": 4}, 13)
        self.assertTrue(card_eq == self.card8)
        card_eq = Card({"Harts": 3}, 13)
        self.assertTrue(card_eq == self.card6)
        card_eq = Card({"Spades": 2}, 1)
        self.assertTrue(card_eq == self.card4)
        card_eq = Card({"Diamonds": 1}, 10)
        self.assertTrue(card_eq == self.card2)