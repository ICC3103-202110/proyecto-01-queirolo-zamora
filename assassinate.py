from abc import ABC
from abc import abstractmethod
from challenge import Challenge
from counterattack import Counterattack
from gamestatus import Gamestatus
import time
import random



class Assassinate (ABC):

    def __init__ (self, attacker, players, n_players,deck):
        self.attacker = attacker
        self.players = players
        self.n_players = n_players
        self.deck = deck
    
    def assassinate (self):

        if self.attacker.coins < 3:
            print("You don't have enough money, you lose your turn!")
        else:
            
            
            time.sleep(3)
            print(100 * '\n')
            challenged = Challenge.challenge(
                            Challenge(self.attacker, 2, self.n_players ,self.players,self.deck))
            if challenged == False:
                print()
                self.attacker.coins -= 3
                print('-3 coins.')
                print()
                y_n = input(
                        'someone whats to counterattack this action?(yes/no)')
                if  y_n == 'yes':
                    attackers = []
                    for i in range(self.n_players):
                        if self.players[i] != self.attacker:
                            print(i+1, '.-', self.players[i].name)
                                
                    attacker1 = (int(input()))-1
                    attackers.append(attacker1)
                    y_n = input(
                        'someone else whats to counterattack this action?(yes/no)')
                    if  y_n == 'yes':
                        for i in range(self.n_players):
                            if self.players[i] != self.attacker:
                                print(i+1, '.-', self.players[i].name)
                        attacker2 = (int(input()))-1
                        attackers.append(attacker2)
                    if self.n_players == 4 and y_n == 'yes':
                        y_n = input(
                            'someone else whats to challenge this action?(yes/no)')
                        if  y_n == 'yes':
                            for i in range(self.n_players):
                                if self.players[i] != self.attacker:
                                    print(i+1, '.-', self.players[i].name)
                            attacker3 = (int(input()))-1
                            attackers.append(attacker3)
                    attacker = random.choice(attackers)
                    blocked = Counterattack.counterattack(
                        Counterattack(self.attacker, 5, self.n_players, self.players, attacker, self.deck))
                else:
                    blocked = False

                if blocked == False:
                    Gamestatus.Show_gamestatus(Gamestatus(
                        self.attacker, self.players, self.n_players))
                    print("-----------------------------------------------------------------------------------")
                    for i in range(self.n_players):
                        if self.players[i] != self.attacker:
                            print(i+1, '.-', self.players[i].name)
                    assassinated = int(input("Choose the number of the player you want to Assassinate: ")) - 1
                    print(self.players[assassinated].name, 'Choose a card to reveal!')
                    time.sleep(3)
                    for i in range(len(self.players[assassinated].playing_cards)):
                        print(i+1, '.-', self.players[assassinated].playing_cards[i])
                    
                    choosen_card = int(input())-1
                    
                    Gamestatus.Change_gamestatus(Gamestatus(self.attacker, self.players, self.n_players), self.players[assassinated], choosen_card)
                else:
                    print('the action failed')