from abc import ABC
from abc import abstractmethod

class Deck(ABC):

    def __init__(self, deck):
        self.deck = deck
    
    def draw_card_from_deck(self):

        rcard = self.deck[0]
        self.deck.remove[rcard]
        return rcard

