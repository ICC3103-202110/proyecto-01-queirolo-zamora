from abc import ABC
from abc import abstractmethod
from numpy import random


class Cards(ABC):

    def __init__(self, deck):
        self.deck = deck

    def generate_deck(self):
        # 1 = Duque
        # 2 = asesino
        # 3 = capitanes
        # 4 = embajador 
        # 5 = condesa
        self.deck = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]

        self.deckdeck = random.shuffle(self.deck)
        

        return self.deck

            

