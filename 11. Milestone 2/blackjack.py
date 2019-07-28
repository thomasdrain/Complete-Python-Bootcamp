class Card():
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"

mycard = Card("ace", "spade")
print(mycard)

class Deck():

    def __init__(self):
        self.cards = list(52)
        counter = 0
        for suit in ['club', 'diamond', 'heart', 'spade']:
            self.cards[counter + 1] = Card('ace', suit)
            self.cards[counter + 1] = Card('2', suit)
            self.cards[counter + 1] = Card('3', suit)
            self.cards[counter + 1] = Card('4', suit)
            self.cards[counter + 1] = Card('5', suit)
            self.cards[counter + 1] = Card('6', suit)
            self.cards[counter + 1] = Card('7', suit)
            self.cards[counter + 1] = Card('8', suit)
            self.cards[counter + 1] = Card('9', suit)
            self.cards[counter + 1] = Card('10', suit)
            self.cards[counter + 1] = Card('jack', suit)
            self.cards[counter + 1] = Card('queen', suit)
            self.cards[counter + 1] = Card('king', suit)