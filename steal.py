from abc import ABC
from abc import abstractmethod
from challenge import Challenge
from counterattack import Counterattack


class Steal (ABC):

    def __init__ (self, attacker, players, n_players):
        self.attacker = attacker
        self.players = players
        self.n_players = n_players
    
    def steal (self):
        challenged = Challenge.challenge(
                        Challenge(self.attacker, 4, self.n_players ,self.players))
        if challenged == False:
            if (input('Someone whats to counterattack this action? (yes/no)')) == "yes":
                blocked = Counterattack.counterattack(
                    Counterattack(self.attacker, 1, self.n_players, self.players))
            else:
                blocked = False

            if blocked == False:
                print('Who do you want to steal from?')
                for i in range(self.n_players):
                    if self.players[i] != self.attacker:
                        print(i+1, '.-', self.players[i].name)
            stoled = int(input("Choose a player to Coup: ")) - 1
            if self.players[stoled].coins == 1:
                self.players[stoled].coins -= 1
                self.attacker.coins += 1
            else:
                self.players[stoled].coins-= 2
                self.attacker.coins += 2