from abc import ABC
from abc import abstractmethod
from challenge import Challenge
from counterattack import Counterattack


class Assassinate (ABC):

    def __init__ (self, attacker, players, n_players):
        self.attacker = attacker
        self.players = players
        self.n_players = n_players
    
    def assassinate (self):

        if self.attacker.coins <= 3:
            print("You don't have enough money, you lose your turn!")
        else:
            challenged = Challenge.challenge(
                            Challenge(self.attacker, 2, self.n_players ,self.players))
            if challenged == False:
                if (input('Someone whats to counterattack this action? (yes/no)')) == "yes":
                    blocked = Counterattack.counterattack(
                        Counterattack(self.attacker, 5, self.n_players, self.players))
                else:
                    blocked = False

                if blocked == False:
                    self.attacker.coins -= 3
                    for i in range(self.n_players):
                        if self.players[i] != self.attacker:
                            print(i+1, '.-', self.players[i].name)
                    assassinated = int(input("Choose a player to Coup: ")) - 1
                    print(self.players[assassinated].name, 'Choose a card to reveal!')
                    for i in range(len(self.players[assassinated].cards)):
                        print(i, '.-', self.players[assassinated].cards[i])
                    choosen_card = int(input())-1
                    
                    