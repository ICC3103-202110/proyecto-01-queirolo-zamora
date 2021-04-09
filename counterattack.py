from abc import ABC
from abc import abstractmethod
from challenge import Challenge


class Counterattack(ABC):

    def __init__(self, victim, counterattack_card, n_players, players):
        self.victim = victim
        self.counterattack_card = counterattack_card
        self.n_players = n_players
        self.players = players

    def counterattack(self):
        y_n = input('someone whats to challenge this counterattack?(yes/no)')
        if  y_n == 'yes':
            for i in self.n_players:
                if self.players[i] != self.victim:
                    print(i+1, '.-', self.players[i])
            attacker = input()
            winner = Challenge.challenge(Challenge(attacker, self.counterattack_card, self.players))

            if winner == 'victim':
                return True
            if winner == 'attacker':
                return False

        elif y_n == 'no':
            return True
