from abc import ABC
from abc import abstractmethod

class Coup (ABC):

    def __init__ (self, attacker, players, n_players):
        self.attacker = attacker
        self.players = players
        self.n_players = n_players
    
    def coup (self):
        if self.attacker.coins <= 6:
            print("You don't have enough money, you lose your turn!")
        
        else:
            self.attacker.coins -= 7
            print()
            print('-7 coins.')
            print()
            for i in self.n_players:
                if self.players[i] != self.attacker:
                    print(i+1, '.-', self.players[i])
            COUPED = input("Choose a player to Coup: ") - 1
            print(self.players[COUPED].name, 'Choose a card to reveal!')
            for i in len(self.players[COUPED].cards):
                print(i, '.-', self.players[COUPED].cards[0])
            choosen_card = input()

            



            