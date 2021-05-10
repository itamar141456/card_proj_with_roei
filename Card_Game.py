from deck_class import CardDeck


class CardGame:
    """
    class that represent a game: has 2 players, a deck of cards, and "get winner" function.
    """
    def __init__(self, player1, player2, num_of_card_to_deal=10):
        """
        Initialize a game
        :Param num_of_card_to_deal: int (default 10), if deviates from the range allowed (1-26), it is changed to the closest allowed number
        :Param player1: type - Player class
        :param player1: type - Player class
        Shuffle the deck and assigning the players a hand
        """
        self.game_started = False
        self.game_deck = CardDeck()
        self.player1 = player1
        self.player2 = player2
        self.__new_game(player1, player2, num_of_card_to_deal)

    def __str__(self):
        """
        For printing the game
        :return: The game deck and the 2 players names
        """
        return f"the game deck is: {self.game_deck} and the players are {self.player1.name} and {self.player2.name}"

    def __new_game(self, player1, player2, num_of_card_to_deal):
        """
        Shuffles the deck, assigning cards to the players, can be used only through the __init__ method (one time only)
        :return:
        """
        if not self.game_started:
            self.game_started = True
            self.game_deck.Shuffle()
            player1._Player__set_hand(self.game_deck, num_of_card_to_deal)
            player2._Player__set_hand(self.game_deck, num_of_card_to_deal)
        else:
            print("Error: __new_game, unable to execute")

    def get_winner(self):
        """
        determines who is the winner by checking for the shorter hand
        :return: the player who won, type - Player
        """
        if len(self.player1.hand) < len(self.player2.hand):
            return self.player1
        elif len(self.player2.hand) < len(self.player1.hand):
            return self.player2
        else:
            return None







