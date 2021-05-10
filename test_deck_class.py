from unittest import TestCase
from Card_class import Card
from deck_class import CardDeck
from unittest.mock import patch

class TestCardDeck(TestCase):

    def setUp(self):
        """
        create 2 deck, deck1 = full deck, deck2
        """
        self.deck1 = CardDeck()
        self.deck2 = CardDeck()
        self.deck2.cards_list = [Card({"Clubs": 4}, 8), Card({"Harts": 3}, 7), Card({"Diamonds": 1}, 5),
                                 Card({"Spades": 2}, 4)]

    def test_initialization(self):
        """
        check that all the objects in deck1 are from type - Card, 52 cards with no duplications
        check that all the objects in deck2 (manual deck) are from type - Card (for reliability)
        """
        # checking type and length
        for i in self.deck1.cards_list:
            assert type(i) == Card
        for i in self.deck2.cards_list:
            assert type(i) == Card
        self.assertEqual(len(self.deck1.cards_list), 52)

        # checking for duplicated cards
        duplicated_list = self.deck1.cards_list.copy()
        for i in duplicated_list:
            self.deck1.cards_list.remove(i)
            if i in self.deck1.cards_list:
                self.fail()

    def test_shuffle(self):
        """
        checking that CardDeck.shuffle built well
        """
        # """
        # check that the shuffle method is working, as well as making sure it does a good job by
        # checking the statistic of identical deck after a shuffle, when deck has 4 cards
        # """
        # # count times that deck being properly shuffled
        # count_statistic = 0
        # for i in range(5):
        #     try:
        #         deck_test = self.deck2.cards_list.copy()
        #         self.deck2.Shuffle()
        #         self.assertFalse(deck_test == self.deck2.cards_list)
        #         self.assertEqual(len(self.deck2.cards_list), 4)
        #         count_statistic += 1
        #     except AssertionError:
        #         # checking that the deck has a minimum of: 4 of 5 effective shuffles
        #         if count_statistic >= 4:
        #             pass
        #         else:
        #             self.fail("the shuffle doesn't work properly")
        for i in range(3):
            deck_test = self.deck2.cards_list.copy()
            self.deck2.Shuffle()
            self.assertFalse(deck_test == self.deck2.cards_list)
            self.assertEqual(len(self.deck2.cards_list), 4)

    def test_deal_one(self):
        """
        checking that deal_one is removing the chosen card from the list
        checking that deal_one is returning the chosen cards from the list
        """
        with patch('final_python_project.deck_class.random.choice') as choice_mock:
            choice_mock.return_value = Card({"Clubs": 4}, 8)
            self.assertNotIn(self.deck2.deal_one(), self.deck2.cards_list)
            self.assertEqual(len(self.deck2.cards_list), 3)
            self.assertEqual(self.deck1.deal_one(), Card({"Clubs": 4}, 8))

            choice_mock.return_value = Card({"Spades": 2}, 4)
            self.assertNotIn(self.deck2.deal_one(), self.deck2.cards_list)
            self.assertEqual(len(self.deck2.cards_list), 2)

            choice_mock.return_value = Card({"Diamonds": 1}, 5)
            self.assertNotIn(self.deck2.deal_one(), self.deck2.cards_list)
            self.assertEqual(len(self.deck2.cards_list), 1)

            choice_mock.return_value = Card({"Harts": 3}, 7)
            self.assertNotIn(self.deck2.deal_one(), self.deck2.cards_list)
            self.assertEqual(len(self.deck2.cards_list), 0)
            self.assertEqual(self.deck2.cards_list, [])

    def test_deal_one_empty(self):
        """
        checking that deal_one on empty list is returning an error and not dealing, error = IndexError / other
        """
        self.deck2.cards_list = []
        try:
            self.deck2.deal_one()
            self.fail()
        except IndexError:
            pass
        except:
            self.fail()

