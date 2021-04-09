from abc import ABC
from abc import abstractmethod


class Show_game(ABC):

    def __init__(self, player, players, n_players):
        self.player = player
        self.players = players
        self.n_players = n_players


    def show_game(self):
        print('-------------------------------------------------GAME-----------------------------------------------------------------')
        print()
        print('                                             Player:')
        print('                                                    ',self.players[1].name)
        print('                                             CARDS:')
        print('                                                    ',self.players[1].cards)
        print('                                             COINS:')
        print('                                                    ',self.players[1].coins)
        print()
        print('Player:                                                                                      Player:')
        print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
        print('CARDS:                                                                                       CARDS:')
        print('       ',self.players[0].cards,'                                                                                     ',self.players[2].cards)
        print('COINS:                                                                                       COINS:')
        print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
        if self.n_players == 4:
            print()
            print('                                             Player:')
            print('                                                    ',self.players[3].name)
            print('                                             CARDS:')
            print('                                                    ',self.players[3].cards)
            print('                                             COINS:')
            print('                                                    ',self.players[3].coins)
            print()






