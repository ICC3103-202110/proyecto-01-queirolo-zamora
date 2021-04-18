from abc import ABC
from abc import abstractmethod

class Challenge (ABC):

    def __init__(self, victim, challenged_card, n_players, players):
        self.victim = victim
        self.challenged_card = challenged_card
        self.n_players = n_players
        self.players = players
    
    def challenge(self):
        y_n = input('someone whats to challenge this action?(yes/no)')
        if  y_n == 'yes':
            for i in range(self.n_players):
                if self.players[i] != self.victim:
                    print(i+1, '.-', self.players[i].name)
                
            attacker = (int(input()))-1

            if self.challenged_card == self.victim.cards[0] or self.challenged_card == self.victim.cards[1]:
                print(self.players[attacker], 'lose the challenge')
                print(self.players[attacker], 'chose a card to reval!')
                print('1.-', self.players[attacker].cards[0])
                print('2.-', self.players[attacker].cards[1])
                choosen_card = int(input())-1
                
                
                return 'victim'

            else:
                print(self.victim, 'lose the challenge')
                print(self.victim, 'chose a card to reval!')
                print('1.-', self.victim.cards[0])
                print('2.-', self.victim.cards[1])
                choosen_card = int(input())-1
                

                return 'attacker'




        elif y_n == 'no':
            return False