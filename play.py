from abc import ABC
from abc import abstractmethod
import time
from showgame import Show_game
from players import Player
from deck import Deck
from counterattack import Counterattack
from challenge import Challenge
from coup import Coup
from steal import Steal
from assassinate import Assassinate


class Play (ABC):

    def __init__(self, players, n_players):
        self.players = players
        self.n_players = n_players

    def play (self):
        vbreak = False
        while True:
            if vbreak == True:
                break

            for i in range(self.n_players):

                print(100 * '\n')

                print("it's", self.players[i].name,"'s Turn!")
                


                Show_game.show_game(Show_game(
                    self.players[i], self.players, self.n_players))

                if self.players[i].coins >= 10:
                    action = 3

                else:
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
                    self.players[i].change_amount_coins(1)


                elif action == 2:
                    if (input(
                        'Someone whats to counterattack this action? (yes/no)')) == "yes":
                        blocked = Counterattack.counterattack(
                            Counterattack(
                                self.players[i], 1, self.n_players, self.players))
                    else:
                        blocked = False

                    if blocked == False:
                        self.players[i].change_amount_coins(2)
                   

                elif action == 3:
                    Coup.coup(Coup(self.players[i], self.players, self.n_players))
                
                #Character Actions

                elif action == 4:
                    challenged = Challenge.challenge(
                        Challenge(self.players[i], 4, self.n_players ,self.players))
                    if challenged == False:
                        self.players[i].coins += 3
                

                elif action == 5:
                    Assassinate.assassinate(
                        Assassinate(self.players[i], self.players, self.n_players))



                elif action == 6:
                    Steal.steal(Steal(self.players[i], self.players, self.n_players))

                
                elif action == 7:
                    NEW_CARDS= []
                    #for i in range(2): 
                        #NEW_CARDS.append(Deck.draw_card_from_deck())

                    self.players[i].cards.append(NEW_CARDS)

                    CARD1= input("Choose a card to return it to the deck: ")
                    CARD2= input("Choose another card to return it to the deck: ")

                    self.players[i].cards.remove(CARD1)
                    self.players[i].cards.remove(CARD2)

                    shuffle_deck.append(CARD1,CARD2)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                Show_game.show_game(Show_game(self.players[i], self.players, self.n_players))
                time.sleep(3)

            
