from abc import ABC
from abc import abstractmethod
from challenge import Challenge


class Counterattack(ABC):

    def __init__(self, victim, counterattack_card, n_players):
        self.victim = victim
        self.counterattack_card = counterattack_card
        self.n_players = n_players

    def counterattack(self):
        y_n = input('someone whats to challenge this counterattack?(yes/no)')
        if  y_n == 'yes':
            print('who is counterattacking?')
            print('1.' )
            print('2.' )
            if self.n_players == 4:
                print('3.' )
            attacker = input()
            Challenge.challenge(Challenge(attacker, self.counterattack_card))
        elif y_n == 'no':
            return True
