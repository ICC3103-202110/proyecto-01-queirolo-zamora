from abc import ABC
from abc import abstractmethod
from challenge import Challenge


class Counterattack(ABC):

    def __init__(self, victim, attack):
        self.victim = victim
        self.attack = attack

    def counterattack(self):
        y_n = input('someone whats to challenge this counterattack?(yes/no)')
        if  y_n == 'yes':
            print('who is challenging?')
            print('1.' )
            print('2.' )
            if n_players == 4:
                print('3.' )
            Challenge.challenge()
        elif y_n == 'no':
            

