from unittest import TestCase
from unittest.mock import patch
from player_class import Player
from deck_class import CardDeck
from Card_class import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player('roie')
        self.player2 = Player('itamar')
        self.card_deck = CardDeck()
        self.card_deck2 = CardDeck()

    def test__set_hand1(self):
        """
        checks that the maximum of cards to set_hand for each player is 26
        """
        with patch("final_python_project.player_class.CardDeck.deal_one") as mock_deal_one:
            mock_deal_one.return_value = Card({"Diamond": 1}, 8)
            self.player1._Player__set_hand(self.card_deck, 27)
            self.player2._Player__set_hand(self.card_deck, 26)
            self.assertTrue(len(self.player1.hand) == len(self.player2.hand))
            self.assertTrue(len(self.player1.hand) == 26)

    def test__set_hand3(self):
        """
        checks that the minimum of cards to set_hand of the player is 1
        """
        with patch("final_python_project.player_class.CardDeck.deal_one") as mock_deal_one:
            mock_deal_one.return_value = Card({"Diamond": 1}, 8)
            self.player1._Player__set_hand(self.card_deck, 0)
            self.player2._Player__set_hand(self.card_deck, 1)
            self.assertTrue(len(self.player1.hand) == len(self.player2.hand))
            self.assertTrue(len(self.player1.hand) == 1)

    def test_get_card(self):
        """
        check that get_card get a card from the given player not somewhere else
        """
        self.player1.hand = [Card({"Clubs": 4}, 8)]
        p1_card = self.player1.hand[0]
        # checks a card from the players hand is dealt and not a random card from somewhere else
        self.assertEqual(p1_card, self.player1.get_card())
        # checks the card is removed
        self.assertEqual(self.player1.hand, [])

    def test_get_card2(self):
        """
        checks the cards got from the player are random and not the first in the deck.
        the test will be on three cards, because 1 if tried with 1 card
        """
        self.player2.hand = [Card({"Clubs": 4}, 8), Card({"Harts": 3}, 7), Card({"Diamonds": 1}, 5),
                             Card({"Spades": 2}, 4), Card({"Clubs": 4}, 9), Card({"Harts": 3}, 4),
                             Card({"Diamonds": 1}, 8), Card({"Spades": 2}, 6)]
        p2_hand = self.player2.hand.copy()  # saves a copy of the first hand to compare later
        cards_dealt = []
        for i in range(3):
            cards_dealt.append(self.player2.get_card())  # get three cards from the player.
        self.assertNotEqual(cards_dealt, p2_hand[0:3])
        self.assertNotEqual(cards_dealt[::-1], p2_hand[-3:-1])

    def test_get_card3(self):
        """
        test that get_card returning an Error when player hand is empty
        """
        self.player1.hand = []
        try:
            self.player1.get_card()
            self.fail()
        except IndexError:
            pass
        except:
            self.fail()

    def test_add_cards(self):
        """
        checks the add_cards func can get as many cards as given.
        checks 0, 1, 3
        and check that no card type input is not added to the list
        """
        self.player1.add_cards(Card({"Diamonds": 1}, 1))
        self.assertEqual(len(self.player1.hand), 1)
        self.player1.add_cards(Card({"Harts": 3}, 3), Card({"Spades": 2}, 8), Card({"Clubs": 4}, 11), 4, "abba", 5.2345)
        self.assertEqual(len(self.player1.hand), 4)
        self.assertNotIn('abba', str(self.player1.hand))
        self.player1.add_cards()
        self.assertEqual(len(self.player1.hand), 4)
