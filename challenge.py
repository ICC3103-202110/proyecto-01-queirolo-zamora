from abc import ABC
from abc import abstractmethod
from gamestatus import Gamestatus
import random

class Challenge (ABC):

    def __init__(self, victim, challenged_card, n_players, players):
        self.victim = victim
        self.challenged_card = challenged_card
        self.n_players = n_players
        self.players = players
    
    def challenge(self):
        attackers = []
        y_n = input('someone whats to challenge this action?(yes/no)')
        if  y_n == 'yes':
            for i in range(self.n_players):
                if self.players[i] != self.victim:
                    print(i+1, '.-', self.players[i].name)
                
            attacker1 = (int(input()))-1
            attackers.append(attacker1)
            y_n = input('someone else whats to challenge this action?(yes/no)')
            if  y_n == 'yes':
                for i in range(self.n_players):
                    if self.players[i] != self.victim:
                        print(i+1, '.-', self.players[i].name)
                attacker2 = (int(input()))-1
                attackers.append(attacker2)
            if self.n_players == 4 and y_n == 'yes':
                y_n = input('someone else whats to challenge this action?(yes/no)')
                if  y_n == 'yes':
                    for i in range(self.n_players):
                        if self.players[i] != self.victim:
                            print(i+1, '.-', self.players[i].name)
                    attacker3 = (int(input()))-1
                    attackers.append(attacker3)
            attacker = random.choice(attackers)
            print(attacker.name, 'is chalenging')
        


            if self.challenged_card == self.victim.cards[0] or self.challenged_card == self.victim.cards[1]:
                print(self.players[attacker].name, 'lose the challenge')
                print(self.players[attacker].name, 'chose a card to reval!')
                print('1.-', self.players[attacker].playing_cards[0])
                print('2.-', self.players[attacker].playing_cards[1])
                choosen_card = int(input())-1
                Gamestatus.Change_gamestatus(Gamestatus(self.players[attacker], self.players, self.n_players), self.players[attacker], choosen_card)
                
                
                return False

            else:
                print(self.victim.name, 'lose the challenge')
                print(self.victim.name, 'chose a card to reval!')
                print('1.-', self.victim.playing_cards[0])
                print('2.-', self.victim.playing_cards[1])
                choosen_card = int(input())-1
                Gamestatus.Change_gamestatus(Gamestatus(self.players[attacker], self.players, self.n_players), self.victim, choosen_card)
                

                return 'attacker'




        elif y_n == 'no':
            return False