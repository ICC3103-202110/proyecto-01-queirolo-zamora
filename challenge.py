from abc import ABC
from abc import abstractmethod
from gamestatus import Gamestatus
import random
import time



class Challenge (ABC):

    def __init__(self, victim, challenged_card, n_players, players, deck):
        self.victim = victim
        self.challenged_card = challenged_card
        self.n_players = n_players
        self.players = players
        self.deck = deck
    
    def challenge(self):
        attackers = []
        while True:
            y_n = input('someone whats to challenge this action?(yes/no)')
            try:
                if y_n == "yes" or y_n == "no":
                    break
            except:
                print('Insert a valid answer!')
                ValueError
        if  y_n == 'yes':
            for i in range(self.n_players):
                if self.players[i] != self.victim:
                    print(i+1, '.-', self.players[i].name)

            while True:
                    attacker1 = (int(input()))-1
                    try:
                        if attacker1<= self.n_players-1 and attacker1>=0:
                            break
                    except:
                        print('Insert a valid answer!')
                        ValueError
            attackers.append(attacker1)
            while True:
                y_n = input('someone else whats to challenge this action?(yes/no)')
                try:
                    if y_n == "yes" or y_n == "no":
                        break
                except:
                    print('Insert a valid answer!')
                    ValueError
    
            if  y_n == 'yes':
                for i in range(self.n_players):
                    if self.players[i] != self.victim:
                        print(i+1, '.-', self.players[i].name)
                while True:
                    attacker2 = (int(input()))-1
                    try:
                        if attacker2<= self.n_players-1 and attacker2>=0:
                            break
                    except:
                        print('Insert a valid answer!')
                        ValueError
                attackers.append(attacker2)
            if self.n_players == 4 and y_n == 'yes':
                while True:
                    y_n = input('someone else whats to challenge this action?(yes/no)')
                    try:
                        if y_n == "yes" or y_n == "no":
                            break
                    except:
                        print('Insert a valid answer!')
                        ValueError
                        
                if  y_n == 'yes':
                    for i in range(self.n_players):
                        if self.players[i] != self.victim:
                            print(i+1, '.-', self.players[i].name)
                    while True:
                        attacker3 = int(input())-1
                        try:
                            if attacker3<= self.n_players-1 and attacker3>=0:
                                break
                        except:
                            print('Insert a valid answer!')
                            ValueError
                attackers.append(attacker3)
            attacker = random.choice(attackers)
            print(self.players[attacker].name, 'is challenging')
            time.sleep(3)
            print()
        


            if self.challenged_card == self.victim.cards[0] or self.challenged_card == self.victim.cards[1]:
                print(self.players[attacker].name, 'lost the challenge')
                time.sleep(2)
                print()
                print(self.players[attacker].name, 'choose a card to reval!')
                time.sleep(3)
                print()
                print('1.-', self.players[attacker].playing_cards[0])
                print('2.-', self.players[attacker].playing_cards[1])
                
                while True:
                    choosen_card = int(input())-1
                    try:
                        if choosen_card>=0 and choosen_card<=1:
                            break
                    except:
                        print('Insert a valid answer!')
                        ValueError
                Gamestatus.Change_gamestatus(Gamestatus(self.players[attacker], self.players, self.n_players), self.players[attacker], choosen_card)
                
                return False

            else:
                print(self.victim.name, 'lost the challenge')
                time.sleep(2)
                print()
                print(self.victim.name, 'choose a card to reval!')
                time.sleep(3)
                print()
                print('1.-', self.victim.playing_cards[0])
                print('2.-', self.victim.playing_cards[1])
                while True:
                    choosen_card = int(input())-1
                    try:
                        if choosen_card>=0 and choosen_card<=1:
                            break
                    except:
                        print('Insert a valid answer!')
                        ValueError
                Gamestatus.Change_gamestatus(Gamestatus(self.players[attacker], self.players, self.n_players), self.victim, choosen_card)
                

                return 'attacker'




        elif y_n == 'no':
            return False