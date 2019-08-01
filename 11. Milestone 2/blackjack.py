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

    def deal(self, player, num):
        for i in range(num):
            new_card = self.cards.pop(-1)
            player.add_card(new_card)

'''
DEFINING A PLAYER
'''

class Player:

    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []

    def value_of_hand(self):
        value = 0
        ##### CANT USE c == 'x', MUST GET TO THE RANK OF THE CARD
        num_aces = len([c for c in self.cards_in_hand if c == 'ace'])
        num_non_aces = len(self.cards_in_hand) - num_aces
        print(num_aces)
        print(num_non_aces)

        # value calculations for all except any aces
        if num_non_aces > 0:
            for c in filter(lambda x: x != 'ace', self.cards_in_hand):
                if c in range(2, 10):
                    value += int(c)

                elif c in ['jack', 'queen', 'king']:
                    value += 10

        # if we've got one ace, it'll contribute 10 to the value, otherwise only one
        if num_aces == 1:
            if value <= 10:
                value += 11
            else:
                value += 1
        # if we've got two (or more!) aces, at most one ace will contribute 10 to the value,
        # otherwise 1 each.
        elif num_aces > 1:
            if value >= 10:
                value += num_aces
            else:
                value += 10 + (num_aces - 1)
        return value

    def add_card(self, new_card, reveal = False):
        self.cards_in_hand.append(new_card)
        if reveal:
            print(f"Dealt to {self.name}: {new_card}")
        else:
            print(f"Dealt to {self.name}: some card")

    def __str__(self):
        res = "\nCards held by " + self.name + ":\n" + '\n'.join(map(str, self.cards_in_hand)) +\
            "\n\nValue of hand = " + str(self.value_of_hand())
        return res

mydeck = Deck()
mydeck.shuffle()
human = Player("Player")
mydeck.deal(human, 3)
print(human)
#human.value_of_hand()

