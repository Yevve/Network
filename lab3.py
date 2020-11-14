from enum import Enum
import random
class Values(Enum):
    King=13
    Queen=12
    Jack=11
    Ten=10
    Nine=9
    Eight=8
    Seven=7
    Six=6
    Five=5
    Four=4
    Three=3
    Two=2
    Ace=1
class Suits(Enum):
    Hearts=1
    Diamonds=2
    Clubs=3
    Spades=4


class Card():
    def __init__(self,suit,value):
        assert 1 <= suit <=4 and 1 <= value <= 13
        self._suit=suit
        self._value=value
    def getValue(self):
        return self._value
    def getSuit(self):
        return self._suit
    def __str__(self): 
        clor=Card.getSuit(self)
        val=Card.getValue(self)
        return str(Values(val).name)+ " of " + str(Suits(clor).name)
        


class CardDeck:
    def __init__(self):
        self.reset()
    def shuffle(self):
        random.shuffle(self.cards)
    def getCard(self):
        return self.cards.pop()
    def size(self):
        return len(self.cards)
    def reset(self):
        self.cards=[]
        for suit in range(1,5):
            for value in range(1,14):
                self.cards.append(Card(suit,value))


deck=CardDeck()
deck.shuffle()
while deck.size()>0:
    card=deck.getCard()
    print("Card {} has value {}".format(card,card.getValue()))