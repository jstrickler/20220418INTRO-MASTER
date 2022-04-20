from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck() # call parent method
        for i in range(1, 3):
            joker = '** JOKER **', i
            self._cards.append(joker)
