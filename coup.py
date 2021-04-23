from abc import ABC
from abc import abstractmethod
from gamestatus import Gamestatus

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
            for i in range(self.n_players):
                if self.players[i] != self.attacker:
                    print(i+1, '.-', self.players[i].name)
    
            while True:
                COUPED = int(input("Choose a player to Coup: ")) - 1
                try:
                    if COUPED<= self.n_players-1 and COUPED>=0:
                        break
                except:
                    print('Insert a valid answer!')
                    ValueError
            print(self.players[COUPED].name, 'Choose a card to reveal!')
            for i in range(len(self.players[COUPED].playing_cards)):
                print(i, '.-', self.players[COUPED].playing_cards[i])

            while True:
                choosen_card = int(input())-1
                try:
                    if choosen_card>= 0 and choosen_card>=1:
                        break
                except:
                    print('Insert a valid answer!')
                    ValueError
            Gamestatus.Change_gamestatus(Gamestatus(self.attacker, self.players, self.n_players), self.players[COUPED], choosen_card)
            
            



            