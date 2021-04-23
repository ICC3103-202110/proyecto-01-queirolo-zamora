from abc import ABC
from abc import abstractmethod
from challenge import Challenge
from counterattack import Counterattack
from gamestatus import Gamestatus
import random



class Steal (ABC):

    def __init__ (self, attacker, players, n_players, deck):
        self.attacker = attacker
        self.players = players
        self.n_players = n_players
        self.deck = deck
    
    def steal (self):
        print(100 * '\n')
        
        challenged = Challenge.challenge(
                        Challenge(self.attacker, 3, self.n_players ,self.players, self.deck))
        if challenged == False:
            y_n = input('someone else whats to counterattack this action?(yes/no)')
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
                print(attacker.name, 'is counterattacking')
                while True:
                    print('1.- Capitan')
                    print('2.- Ambassador')
                    ccoor = int(input(attacker.name, 'with which card are you counterattacking? (1 or 2): '))

                    if ccoor == 1 :
                        ccard = 3
                        break
                    elif ccoor == 2:
                        ccard = 4
                        break
                    else:
                        print('choose a valid card!')

                blocked = Counterattack.counterattack(
                    Counterattack(self.attacker, ccard, self.n_players, self.players, attacker, self.deck))
            else:
                blocked = False

            if blocked == False:
                Gamestatus.Show_gamestatus(Gamestatus(
                        self.attacker, self.players, self.n_players))
                print('Who do you want to steal from?')
                for i in range(self.n_players):
                    if self.players[i] != self.attacker:
                        print(i+1, '.-', self.players[i].name)
                stoled = int(input("Choose a player to steal: ")) - 1
                if self.players[stoled].coins == 0:
                    print(self.players[stoled], 'has no money to steal')
                elif self.players[stoled].coins == 1:
                    self.players[stoled].coins -= 1
                    self.attacker.coins += 1
                else:
                    self.players[stoled].coins-= 2
                    self.attacker.coins += 2
            else:
                print('the action failed')