from abc import ABC
from abc import abstractmethod
import time
from showgame import Show_game
from players import Player
from deck import Deck
#from counterattack import Counterattack
from challenge import Challenge

class Play (ABC):

    def __init__(self, players, n_players):
        self.players = players
        self.n_players = n_players

    def play (self):

        while True:

            for i in range(self.n_players):

                print("it's", self.players[i].name,"'s Turn!")

                time.sleep(3)

                Show_game.show_game(Show_game(self.players[i], self.players, self.n_players))

                print('action you want to perform!')
                print('1. income ')
                print('2. Foreign aid')
                print('3. Strike')
                print('4. Duke-Tax')
                print('5. Murderer-Murder')
                print('6. Captain-Extortion')
                print('7. Ambassador-Change')
                action = int(input())
                
                if action == 1:
                    self.players[i].change_amount_coins(1)


                elif action == 2:
                    if (input('Someone whats to counterattack this action? (yes/no)') == "yes"):
                        pass
                        #blocked = Counterattack.counterattack(Player[i], 1)
                    else:
                        pass
                        #blocked = False

                    #if bloked == False:
                        #self.players[i].change_amount_coins(2)
                   



                elif action == 3:
                    self.players[i].coins-=7
                    print()
                    print('-7 coins. ')
                    COUPED=input("Choose a player: ")
                    if COUPED == self.players[0].name:
                        pass

                elif action == 4:
                    pass

                elif action == 5:
                    pass

                elif action == 6:
                    pass

                elif action == 7:
                    pass
