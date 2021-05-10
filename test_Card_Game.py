from unittest import TestCase
from Card_Game import CardGame
from player_class import Player
from Card_class import Card

class TestCardGame(TestCase):

    def setUp(self):
        Player1 = Player('roie')
        Player2 = Player('itamar')
        self.game1 = CardGame(Player1, Player2, 5)

    def test_build(self):
        """
        check that tha game is built properly
        """
        self.assertTrue(self.game1.player1.name == 'roie')
        self.assertTrue(self.game1.player2.name == 'itamar')
        self.assertTrue(len(self.game1.player1.hand) == 5)
        self.assertTrue(len(self.game1.player2.hand) == 5)
        self.assertTrue(len(self.game1.game_deck.cards_list) == 42)

        for card in self.game1.player1.hand:
            self.assertNotIn(card, self.game1.player2.hand)


    def test__new_game(self):
        """
        make shore __new_game doesnt change a thing when called a second time
        """
        self.game1._CardGame__new_game(Player('yoni'), Player('kobi'), 10)
        self.assertEqual(len(self.game1.player1.hand), 5)
        self.assertEqual(len(self.game1.player2.hand), 5)
        self.assertEqual(self.game1.player1.name, 'roie')
        self.assertEqual(self.game1.player2.name, 'itamar')

    def test_get_winner_win(self):
        """
        check that the correct player won the game
        """
        self.game1.player1.hand = [Card({"Harts": 3}, 3), Card({"Spades": 2}, 8), Card({"Clubs": 4}, 11)]
        self.game1.player2.hand = [Card({"Harts": 3}, 5)]
        self.assertEqual(self.game1.get_winner(), self.game1.player2)

    def test_get_winner_tie(self):
        """
        checks that when the players tied None will be returned
        """
        self.game1.player1.hand = [Card({"Harts": 3}, 3), Card({"Spades": 2}, 8)]
        self.game1.player2.hand = [Card({"Harts": 3}, 5), Card({"Clubs": 4}, 11)]
        self.assertEqual(self.game1.get_winner(), None)

    def test_get_winner_no_cards(self):
        """
        what happends when the players have no cards
        or just one player have no cards
        """
        self.game1.player1.hand = []
        self.game1.player2.hand = []
        self.assertEqual(self.game1.get_winner(), None)

        self.game1.player2.hand = [Card({"Harts": 3}, 5)]
        self.assertEqual(self.game1.get_winner(), self.game1.player1)