from abc import ABC
from abc import abstractmethod

class Challenge (ABC):

    def __init__(self, attacker, victim, challenged_card):
        self.attacker = attacker
        self.victim = victim
        self.challenged_card = challenged_card
    
    def challenge(self):
        pass