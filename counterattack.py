from abc import ABC
from abc import abstractmethod
from challenge import Challenge


class Counterattack(ABC):

    def __init__(self, victim, counterattack_card, n_players, players, attacker):
        self.victim = victim
        self.counterattack_card = counterattack_card
        self.n_players = n_players
        self.players = players
        self.attacker = attacker

    def counterattack(self):
        print(self.attacker.name, 'is counterattacking')
        winner = Challenge.challenge(Challenge(
            self.attacker, self.counterattack_card, self.n_players ,self.players))

        if winner == False:
                return True
                print('successful counterattack')
        if winner == 'attacker':
                return False
