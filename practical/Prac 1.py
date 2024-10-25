import random

#Task 1:
class Card:
    def __init__(self, suit, value_str):
        self.suit = suit
        self.value_str = value_str

    def getSuit(self):
        return self.suit

    def getValueStr(self):
        return self.value_str

    def getValue(self):
        if self.value_str == 'ace':
            return 1
        elif self.value_str in ['jack', 'queen', 'king']:
            return 10
        else:
            return int(self.value_str)

    def __str__(self):
        return f"{self.value_str} of {self.suit}"
    
    #Task 2:
class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        suits = ['hearts', 'pades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop(0)

#Task 3:
class Hand:
    def __init__(self):
        self.cards = []

    def addToHand(self, card):
        if len(self.cards) < 5:
            self.cards.append(card)
        else:
            print("Error: Hand already has 5 cards.")

    def getHandValue(self):
        return sum(card.getValue() for card in self.cards)

    def emptyHand(self):
        self.cards = []

    def showCards(self):
        print(', '.join(str(card) for card in self.cards))


c1 = Card('hearts', 'ace')
print(c1, 'is worth', c1.getValue())
c2 = Card('spades', 'jack')
print(c2, 'is worth', c2.getValue())

deck = Deck()
print(deck.drawCard(), 'is worth', deck.drawCard().getValue())
deck.shuffle()
c3 = deck.drawCard()
print(c3, 'is worth', c3.getValue())
deck.reset()

myCards = Hand()
myCards.addToHand(deck.drawCard())
myCards.addToHand(deck.drawCard())
myCards.showCards()
print(myCards.getHandValue())
myCards.emptyHand()
print(myCards.getHandValue())

