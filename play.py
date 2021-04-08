from abc import ABC
from abc import abstractmethod
import time
from showgame import Show_game
from players import Player
from deck import Deck

class Play (ABC):

    def __init__(self, players, n_players):
        self.players = players
        self.n_players = n_players

    def play (self):

        while True:

            for i in range(self.n_players):

                print("it's", self.players[i].name,"'s Turn!")

                time.sleep(3)

                Show_game.show_game(Show_game(players[i], players, n_players))

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
                    Player[i].change_amount_coins(1)

                elif action == 2:

                elif action == 3:

                elif action == 4:

                elif action == 5:

                elif action == 6:

                elif action == 7:

                
