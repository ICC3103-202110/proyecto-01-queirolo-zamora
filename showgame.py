from abc import ABC
from abc import abstractmethod


class Show_game(ABC):

    def __init__(self, player, players, n_players):
        self.player = player
        self.players = players
        self.n_players = n_players


    def show_game(self):
        a = [[],[]]
        hide_deck1 = a
        hide_deck2 = a
        hide_deck3 = a
        hide_deck4 = a
    






        if self.players[0] == self.player:
            print('-------------------------------------------------GAME-----------------------------------------------------------------')
            print()
            print('                                             Player:')
            print('                                                    ',self.players[1].name)
            print('                                             CARDS:')
            print('                                                    ',hide_deck2)
            print('                                             COINS:')
            print('                                                    ',self.players[1].coins)
            print()
            print('Player:                                                                                      Player:')
            print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
            print('CARDS:                                                                                       CARDS:')
            print('       ',self.players[0].playing_cards,'                                                                                     ',hide_deck3)
            print('COINS:                                                                                       COINS:')
            print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
            if self.n_players == 4:
                print()
                print('                                             Player:')
                print('                                                    ',self.players[3].name)
                print('                                             CARDS:')
                print('                                                    ',hide_deck4)
                print('                                             COINS:')
                print('                                                    ',self.players[3].coins)
                print()

        elif self.players[1] == self.player:
            print('-------------------------------------------------GAME-----------------------------------------------------------------')
            print()
            print('                                             Player:')
            print('                                                    ',self.players[1].name)
            print('                                             CARDS:')
            print('                                                    ',self.players[1].playing_cards)
            print('                                             COINS:')
            print('                                                    ',self.players[1].coins)
            print()
            print('Player:                                                                                      Player:')
            print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
            print('CARDS:                                                                                       CARDS:')
            print('       ',hide_deck1,'                                                                                     ',hide_deck3)
            print('COINS:                                                                                       COINS:')
            print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
            if self.n_players == 4:
                print()
                print('                                             Player:')
                print('                                                    ',self.players[3].name)
                print('                                             CARDS:')
                print('                                                    ',hide_deck4)
                print('                                             COINS:')
                print('                                                    ',self.players[3].coins)
                print()

        elif self.players[2] == self.player:
            print('-------------------------------------------------GAME-----------------------------------------------------------------')
            print()
            print('                                             Player:')
            print('                                                    ',self.players[1].name)
            print('                                             CARDS:')
            print('                                                    ',hide_deck2)
            print('                                             COINS:')
            print('                                                    ',self.players[1].coins)
            print()
            print('Player:                                                                                      Player:')
            print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
            print('CARDS:                                                                                       CARDS:')
            print('       ',hide_deck1,'                                                                                     ',self.players[2].playing_cards)
            print('COINS:                                                                                       COINS:')
            print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
            if self.n_players == 4:
                print()
                print('                                             Player:')
                print('                                                    ',self.players[3].name)
                print('                                             CARDS:')
                print('                                                    ',hide_deck4)
                print('                                             COINS:')
                print('                                                    ',self.players[3].coins)
                print()


        elif self.players[3] == self.player:
            print('-------------------------------------------------GAME-----------------------------------------------------------------')
            print()
            print('                                             Player:')
            print('                                                    ',self.players[1].name)
            print('                                             CARDS:')
            print('                                                    ',hide_deck2)
            print('                                             COINS:')
            print('                                                    ',self.players[1].coins)
            print()
            print('Player:                                                                                      Player:')
            print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
            print('CARDS:                                                                                       CARDS:')
            print('       ',hide_deck1,'                                                                                     ',hide_deck3)
            print('COINS:                                                                                       COINS:')
            print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
            if self.n_players == 4:
                print()
                print('                                             Player:')
                print('                                                    ',self.players[3].name)
                print('                                             CARDS:')
                print('                                                    ',self.players[3].playing_cards)
                print('                                             COINS:')
                print('                                                    ',self.players[3].coins)
                print()










