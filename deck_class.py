from Card_class import Card
import random


class CardDeck:
    """
    a class representing a deck of 52 cards. each card will be different.
    their are 4 suits and 13 cards of each suit
    """
    def __init__(self):
        """
        initialize a shuffled deck of 52 cards of 4 suits (D, S, H, C - from strongest to weakest)
        at the end of the init the params will be:
            self.__suit_dict will be a shuffles list of 52 different cards
            self.__suit_dict will always be a list of dicts representing the suits exist

        """
        self.__suit_dict = [{"Diamonds": 1}, {"Spades": 2}, {"Harts": 3}, {"Clubs": 4}]
        self.cards_list = []
        for suit in self.__suit_dict:
            for value in range(1, 14):
                self.cards_list.append(Card(suit, value))
        self.Shuffle()

    # def __str__(self):
    #     """
    #     simple str method using the Card class __repr__ method
    #     :return:
    #     """
    #     return f"the Deck: {self.cards_list}"

    def Shuffle(self):
        """
        Shuffle the cards in the deck (self._card_deck) used in the __init__ method
        :return:
        """
        random.shuffle(self.cards_list)

    def deal_one(self):
        """
        return a random card from the cards_list and delete him from the cards_list
        :return: card from cards_list
        """
        rand_card = random.choice(self.cards_list)
        self.cards_list.remove(rand_card)
        return rand_card

    def show(self):
        """
        shows all the cards in the cards_list
        """
        for card in self.cards_list:
            print(card)


