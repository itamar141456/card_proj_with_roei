from random import choice
from deck_class import CardDeck
from Card_class import Card


class Player:
    """
    class that represent a player that have a name and a hand of cards drawn from a deck of cards
    """

    def __init__(self, name):
        """
        initialize a player
        :param name: str
        """
        self.name = name
        self.hand = []

    def __set_hand(self, deck, cards_to_deal):
        """
        assigning a hand of cards to the player from the deck for the player
        :param deck: CardDeck type, cant be empty
        :param cards_to_deal: type - int, determine how many cards to deal
        :return:
        """
        assert type(deck) == CardDeck
        if cards_to_deal > 26:
            cards_to_deal = 26
        if cards_to_deal < 1:
            cards_to_deal = 1
        self.hand = [deck.deal_one() for i in range(cards_to_deal)]

    def __str__(self):
        """
        print the player
        :return: name & hand
        """
        return f"Player {self.name} hand: \n{self.hand}"

    def __repr__(self):
        """
        print the player
        :return: name & hand
        """
        return f"Player {self.name} hand: \n{self.hand}"

    def get_card(self):
        """
        draw a random card from the players hand.
        and remove the card from the hand
        :return: a card type
        """
        card = choice(self.hand)
        self.hand.remove(card)
        return card

    def add_cards(self, *new_cards):
        """
        add cards to the players hand
        :param new_cards: cards, can be more that one.
        will not add non card type objects
        :return:
        """
        for card in new_cards:

            if type(card) == Card:
                self.hand.append(card)
            else:
                continue

    def show(self):
        """
        shows the player to the user
        :return:
        """
        print(self)


