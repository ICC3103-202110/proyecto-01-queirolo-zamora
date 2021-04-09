from abc import ABC
from abc import abstractmethod

class Deck(ABC):

    def __init__(self, deck, hand_deck):
        self.deck = deck
        self.hand_deck = hand_deck
    
    def draw_card_from_deck(self):

        rcard = self.deck[0]
        self.deck.remove[rcard]
        return rcard

    def return_card(self,card,hand_deck):
        self.hand_deck.remove(self.card)
        self.deck.append(self.card)
        return self.hand_deck, self.deck


