import random

class Card:
    pass


class CardDeck:  # inherits from 'object'
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = CLUB, DIAMOND, HEART, SPADE

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def get_dealer(self):
        return self._dealer

    @property  # getter property
    def dealer(self):
        return self._dealer

    @dealer.setter  # setter property
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


    @classmethod
    def get_suits(cls):
        return cls.CLUB, cls.DIAMOND, cls.HEART, cls.SPADE

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{self.dealer},{len(self)}"

    @property
    def spam(self):
        return self._spam

    @property
    def ham(self):
        return return self._ham

    @ham.setter
    def ham(self, value):
        self._ham = value

#  prop   props
