from abc import ABC
from abc import abstractmethod
import time
from showgame import Show_game
from players import Player
from deck import Deck
from counterattack import Counterattack
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

                print('Action you want to perform?')
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
                        blocked = Counterattack.counterattack(Player[i], 1)
                    else:
                        blocked = False

                    if bloked == False:
                        self.players[i].change_amount_coins(2)
                   



                elif action == 3:
                    self.players[i].coins-=7
                    print()
                    print('-7 coins.')
                    print()
                    COUPED=input("Choose a player: ")

                    if self.n_players == 2:
                        if COUPED == self.players[0].name:
                            pass
                        elif COUPED == self.players[1].name:
                            pass

                    if self.n_players == 3:
                        if COUPED == self.players[0].name:
                            pass
                        elif COUPED == self.players[1].name:
                            pass
                        elif COUPED == self.players[2].name:
                            pass
                     if self.n_players == 4:
                        if COUPED == self.players[0].name:
                            pass
                        elif COUPED == self.players[1].name:
                            pass
                        elif COUPED == self.players[2].name:
                            pass
                        elif COUPED == self.players[3].name:
                            pass

                elif action == 4:
                    self.players[i].coins+=3
                    print()
                    print("You've earned 3 coins")
                    print()

                elif action == 5:
                    if (input('Someone whats to counterattack this action? (yes/no)') == "yes"):
                        blocked = Counterattack.counterattack(Player[i], 5)    #ver si 5 es condesa
                    else:
                        blocked = False

                    if bloked == False:
                        self.players[i].coins-=3
                        MUERDERED=input("Choose a player: ")
                        
                        if self.n_players == 2:
                            if COUPED == self.players[0].name:
                                pass
                            elif COUPED == self.players[1].name:
                                pass

                        if self.n_players == 3:
                            if MUERDERED == self.players[0].name:
                                pass
                            elif MUERDERED == self.players[1].name:
                                pass
                            elif MUERDERED == self.players[2].name:
                                pass
                            
                        if self.n_players == 4:
                            if MUERDERED == self.players[0].name:
                                pass
                            elif MUERDERED == self.players[1].name:
                                pass
                            elif MUERDERED == self.players[2].name:
                                pass
                            elif MUERDERED == self.players[3].name:
                                pass

                elif action == 6:
                    if (input('Someone whats to counterattack this action? (yes/no)') == "yes"):
                        blocked = Counterattack.counterattack(Player[i], 4)
                    else:
                        blocked = False

                    if bloked == False:
                        EXTORTED=input("Choose a player: ")

                        if self.n_players == 2:
                            if COUPED == self.players[0].name:
                                pass
                            elif COUPED == self.players[1].name:
                                pass

                        if self.n_players == 3:
                            if EXTORTED == self.players[0].name:
                                if self.players[0].coins>=2:
                                    self.players[0].coins-=2
                                else:
                                    self.players[0].coins-=1
                            elif EXTORTED == self.players[1].name:
                                if self.players[1].coins>=2:
                                    self.players[1].coins-=2
                                else:
                                    self.players[1].coins-=1
                            elif EXTORTED == self.players[2].name:
                                if self.players[2].coins>=2:
                                    self.players[2].coins-=2
                                else:
                                    self.players[2].coins-=1

                        if self.n_players == 4:
                            if EXTORTED == self.players[0].name:
                                if self.players[0].coins>=2:
                                    self.players[0].coins-=2
                                else:
                                    self.players[0].coins-=1
                            elif EXTORTED == self.players[1].name:
                                if self.players[1].coins>=2:
                                    self.players[1].coins-=2
                                else:
                                    self.players[1].coins-=1
                            elif EXTORTED == self.players[2].name:
                                if self.players[2].coins>=2:
                                    self.players[2].coins-=2
                                else:
                                    self.players[2].coins-=1
                            elif EXTORTED == self.players[3].name:
                                if self.players[3].coins>=2:
                                    self.players[3].coins-=2
                                else:
                                    self.players[3].coins-=1
                
                elif action == 7:
                     pass