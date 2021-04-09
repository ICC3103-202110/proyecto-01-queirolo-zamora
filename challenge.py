from abc import ABC
from abc import abstractmethod

class Challenge (ABC):

    def __init__(self, victim, challenged_card, n_players):
        self.victim = victim
        self.challenged_card = challenged_card
        self.n_players = n_players
    
    def challenge(self):
        y_n = input('someone whats to challenge this action?(yes/no)')
        if  y_n == 'yes':
            for i in self.n_players
                if players[i] != self.victim:
                    print(i+1, '.-', players[i])
                
            attacker = (int(input()))-1

            if challenged_card == self.victim.cards[0] or challenged_card == self.victim.cards[1]:
                print(players[attacker], 'lose the challenge')
                print(players[attacker], 'chose a card to reval!')
                print('1.-', players[attacker].cards[0])
                print('2.-', players[attacker].cards[1])
                chosen_card = input()

            else:
                print(self.victim, 'lose the challenge')
                print(self.victim, 'chose a card to reval!')
                print('1.-', self.victim.cards[0])
                print('2.-', self.victim.cards[1])
                chosen_card = input()


        elif y_n == 'no':
            return False