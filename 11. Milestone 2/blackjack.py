from random import shuffle


'''
CLASS DEFINITION OF A SINGLE CARD
'''


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"


mycard = Card("ace", "spade")

'''
DEFINING A DECK OF CARDS
'''


class Deck:
    def __init__(self):
        self.cards = [None] * 52
        counter = 0
        for suit in ['clubs', 'diamonds', 'hearts', 'spades']:
            self.cards[(counter * 13)] = Card('ace', suit)
            self.cards[(counter * 13) + 1] = Card('2', suit)
            self.cards[(counter * 13) + 2] = Card('3', suit)
            self.cards[(counter * 13) + 3] = Card('4', suit)
            self.cards[(counter * 13) + 4] = Card('5', suit)
            self.cards[(counter * 13) + 5] = Card('6', suit)
            self.cards[(counter * 13) + 6] = Card('7', suit)
            self.cards[(counter * 13) + 7] = Card('8', suit)
            self.cards[(counter * 13) + 8] = Card('9', suit)
            self.cards[(counter * 13) + 9] = Card('10', suit)
            self.cards[(counter * 13) + 10] = Card('jack', suit)
            self.cards[(counter * 13) + 11] = Card('queen', suit)
            self.cards[(counter * 13) + 12] = Card('king', suit)
            counter += 1

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(len(self)) + ' cards in the deck:\n' + '\n'.join(map(str, self.cards))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num):
        dealt_cards = [None] * num
        for i in range(num):
            dealt_cards[i] = self.cards.pop(-1)
        return dealt_cards

class Hand:

    def __init__(self):
        self.cards = [Card]

    def value(self):
        pass

    def add(self, new_cards):
        pass




mydeck = Deck()
#print(mydeck)
mydeck.shuffle()
x = mydeck.deal(2)
print(mydeck)
print(x)
#print("New hand\n" + x)

