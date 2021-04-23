from abc import ABC
from abc import abstractmethod
import time
from showgame import Show_game
from gamestatus import Gamestatus
from players import Player
from counterattack import Counterattack
from challenge import Challenge
from coup import Coup
from steal import Steal
from assassinate import Assassinate
import random

class Play (ABC):

    def __init__(self, players, n_players, deck):
        self.players = players
        self.n_players = n_players
        self.deck = deck

    def play (self):
        vbreak = False

        while True:
            if self.n_players == 1:
                break
            
            if vbreak == True:
                break

            for i in range(self.n_players):
                if i <= self.n_players-1:

                    print(100 * '\n')

                    print("it's", self.players[i].name,"'s Turn!")
                    


                    Gamestatus.Show_gamestatus(Gamestatus(
                        self.players[i], self.players, self.n_players))
                    #Show_game.show_game

                    if self.players[i].coins >= 10:
                        action = 3

                    else:
                        print(2*'\n')
                        print('Action you want to perform?')
                        print('1. income ')
                        print('2. Foreign aid')
                        print('3. Coup')
                        print('4. Tax')
                        print('5. Assassinate')
                        print('6. Steal')
                        print('7. Exchange')
                        print('8. Force STOP')
                        action = int(input())
                    

                    if action == 8:
                        vbreak = True 
                        
                        break 


                    elif action == 1:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Income')
                        self.players[i].change_amount_coins(1)
                        


                    elif action == 2:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Foreign aid')
                        y_n = input('Someone whats to counterattack this action? (yes/no)')
                        if y_n == "yes" :
                            if  y_n == 'yes':
                                attackers = []
                                for j in range(self.n_players):
                                    if self.players[j] !=self.players[i]:
                                        print(j+1, '.-', self.players[j].name)
                                
                                attacker1 = (int(input()))-1
                                attackers.append(attacker1)
                                y_n = input(
                                    'someone else whats to counterattack this action?(yes/no)')
                                if  y_n == 'yes':
                                    for j in range(self.n_players):
                                        if self.players[j] != self.players[i]:
                                            print(j+1, '.-', self.players[j].name)
                                    attacker2 = (int(input()))-1
                                    attackers.append(attacker2)
                                if self.n_players == 4 and y_n == 'yes':
                                    y_n = input(
                                        'someone else whats to challenge this action?(yes/no)')
                                    if  y_n == 'yes':
                                        for j in range(self.n_players):
                                            if self.players[j] != self.players[i]:
                                                print(j+1, '.-', self.players[i].name)
                                        attacker3 = (int(input()))-1
                                        attackers.append(attacker3)
                                attacker = random.choice(attackers)
                            blocked = Counterattack.counterattack(
                                Counterattack(
                                    self.players[i], 1, self.n_players, self.players, attacker, self.deck))
                        else:
                            blocked = False

                        if blocked == False:
                            self.players[i].change_amount_coins(2)
                        
                    

                    elif action == 3:
                        Coup.coup(Coup(self.players[i], self.players, self.n_players))
                        print(100 * '\n')
                        print(self.players[i].name, 'use Coup')
                    
                    #Character Actions

                    elif action == 4:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Tax')
                        challenged = Challenge.challenge(
                            Challenge(self.players[i], 1, self.n_players ,self.players, self.deck))
                        if challenged == False:
                            self.players[i].coins += 3
                        
                    

                    elif action == 5:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Assassinate')
                        Assassinate.assassinate(
                            Assassinate(self.players[i], self.players, self.n_players, self.deck))
                        



                    elif action == 6:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Steal')
                        Steal.steal(Steal(self.players[i], self.players, self.n_players, self.deck))
                        

                    
                    elif action == 7:
                        print(100 * '\n')
                        print(self.players[i].name, 'use Exchange')
                        new_cards = []
                        new_cards_name = []
                        new_cards.append(self.deck[0])
                        new_cards.append(self.deck[1])
                        if self.players[i].cards[0] != 0:
                            new_cards.append(self.players[i].cards[0])
                        if self.players[i].cards[1] != 0:    
                            new_cards.append(self.players[i].cards[1])
                        self.players[i].cards.pop(0)
                        self.players[i].cards.pop(0)
                        self.players[i].playing_cards.pop(0)
                        self.players[i].playing_cards.pop(0)
                        self.deck.pop(0)
                        self.deck.pop(0)
                        for j in range(len(new_cards)):
                            if new_cards[j] == 1:
                                new_cards_name.append('Duke')
                            elif new_cards[j] == 2:
                                new_cards_name.append('Assassin')
                            elif new_cards[j] == 3:
                                new_cards_name.append('Capitan')
                            elif new_cards[j] == 4:
                                new_cards_name.append('Ambassador')
                            elif new_cards[j] == 5:
                                new_cards_name.append('Contessa')

                        for j in range(len(new_cards)):
                            print(j+1,'.-', new_cards_name[j])

                        card1 = int(input('Select the first card to keep!'))
                        self.players[i].cards.append(new_cards[card1-1])
                        self.players[i].playing_cards.append(new_cards_name[card1-1])
                        new_cards.pop(card1-1)
                        new_cards_name.pop(card1-1)

                        
                        if self.players[i].cards[0] != 0:
                            for j in range(len(new_cards)):
                                print(j+1,'.-', new_cards_name[j])
                            card2 = int(input('Select the second card to keep!'))
                            self.players[i].cards.append(new_cards[card2-1])
                            self.players[i].playing_cards.append(new_cards_name[card2-1])
                            new_cards.pop(card2-1)
                            new_cards_name.pop(card1-1)
                            self.deck.append(new_cards[1])
                        self.deck.append(new_cards[0])
                            

                    
                    self.n_players = len(self.players)
                    
                    if i+1 <= self.n_players:

                        Gamestatus.Show_gamestatus(Gamestatus(
                            self.players[i], self.players, self.n_players))
                        #Show_game.show_game

                        time.sleep(3)
        if vbreak == False:
            print(100 * '\n')
            print('--------------------------------------------------------------------')
            print()
            print('                 ',self.players[0].name, 'Wins!!!!')
            print()
            print('--------------------------------------------------------------------')
            print()
            print()
            print()
            print()
        else:
            print('Force Quit')
    
