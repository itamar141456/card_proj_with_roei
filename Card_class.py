class Card:
    """
    a class representing a standard game card
    """
    def __init__(self, suit, value):
        """
        initialize a card
        :param suit: dict, key = str(suit name), value = int(number represent the suit), only one pair
        :param value: int, between 1-13
        """

        self.__suit = suit  # dict
        self.__value = value  # int
        self.special_cards = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}

    def __str__(self):
        """
        return a string representing the card.
        if the self__suit number is 11, 12, 13, 1
        it will represent it as the allocated word.
        'Jack' for 11, 'Queen' for 12, 'King' for 13, 'Ace' for 1
        :return: str, representation of a card
        """
        if self.__value in self.special_cards.keys():
            return f"{self.special_cards[self.__value]} of {list(self.__suit.keys())[0]}"
        return f"{self.__value} of {list(self.__suit.keys())[0]}"

    def __repr__(self):
        """
        return a string representing the card.
        if the self__suit number is 11, 12, 13, 1
        it will represent it as the allocated word.
        'Jack' for 11, 'Queen' for 12, 'King' for 13, 'Ace' for 1
        :return: str, representation of a card
        """
        if self.__value in self.special_cards.keys():
            return f"{self.special_cards[self.__value]} of {list(self.__suit.keys())[0]}"
        return f"{self.__value} of {list(self.__suit.keys())[0]}"

    def __eq__(self, other):
        """
        compare two cards, to see if they are equal.
        compare both the suit and value,
        :param other: Card class
        :return: bool, if the card are equal or not
        """
        if self.__value == other.__value:
            if self.__suit.keys() == other.__suit.keys():
                return True
        return False

    def __gt__(self, other):
        """
        compare two cards to see if the first given card is of higher value then the second
        note that although Ace numbered as '1' it is the highest card.
        :param other: card
        :return: bool, if self is higher them other or not
        """
        if self.__value == 1 and 2 <= other.__value <= 13:
            return True
        elif 2 <= self.__value <= 13 and other.__value == 1:
            return False

        elif self.__value > other.__value:
            return True
        elif self.__value < other.__value:
            return False

        elif self.__value == other.__value:
            if list(self.__suit.values())[0] > list(other.__suit.values())[0]:
                return True
            elif list(self.__suit.values())[0] < list(other.__suit.values())[0]:
                return False
