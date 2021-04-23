from abc import ABC
from abc import abstractmethod


class Show_game(ABC):

    def __init__(self, player, players, n_players):
        self.player = player
        self.players = players
        self.n_players = n_players
        self.hide_deck1 = self.players[0].hiden_deck
        self.hide_deck2 = self.players[1].hiden_deck
        if n_players == 3:
            self.hide_deck3 = self.players[2].hiden_deck
        if n_players == 4 :
            self.hide_deck4 = self.players[3].hiden_deck



    def show_game(self):

        if self.players[0] == self.player:
            if self.n_players == 2:
                print('Player:                                                                                      Player:')
                print('       ',self.players[0].name,'                                                                                          ',self.players[1].name)
                print('CARDS:                                                                                       CARDS:')
                print('       ',self.players[0].playing_cards,'                                                                                     ',self.hide_deck1)
                print('COINS:                                                                                       COINS:')
                print('       ',self.players[0].coins,'                                                                                          ',self.players[1].coins)
            elif self.n_players >= 3:
                print('-------------------------------------------------GAME-----------------------------------------------------------------')
                print()
                print('                                             Player:')
                print('                                                    ',self.players[1].name)
                print('                                             CARDS:')
                print('                                                    ',self.hide_deck2)
                print('                                             COINS:')
                print('                                                    ',self.players[1].coins)
                print()
                print('Player:                                                                                      Player:')
                print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
                print('CARDS:                                                                                       CARDS:')
                print('       ',self.players[0].playing_cards,'                                                                                     ',self.hide_deck3)
                print('COINS:                                                                                       COINS:')
                print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
                if self.n_players == 4:
                    print()
                    print('                                             Player:')
                    print('                                                    ',self.players[3].name)
                    print('                                             CARDS:')
                    print('                                                    ',self.hide_deck4)
                    print('                                             COINS:')
                    print('                                                    ',self.players[3].coins)
                    print()

        elif self.players[1] == self.player:
            if self.n_players == 2:
                print('Player:                                                                                      Player:')
                print('       ',self.players[0].name,'                                                                                          ',self.players[1].name)
                print('CARDS:                                                                                       CARDS:')
                print('       ',self.hide_deck1,'                                                                                     ',self.players[1].playing_cards)
                print('COINS:                                                                                       COINS:')
                print('       ',self.players[0].coins,'                                                                                          ',self.players[1].coins)
            
            if self.n_players >= 3:
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
                print('       ',self.hide_deck1,'                                                                                     ',self.hide_deck3)
                print('COINS:                                                                                       COINS:')
                print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
                if self.n_players == 4:
                    print()
                    print('                                             Player:')
                    print('                                                    ',self.players[3].name)
                    print('                                             CARDS:')
                    print('                                                    ',self.hide_deck4)
                    print('                                             COINS:')
                    print('                                                    ',self.players[3].coins)
                    print()

        elif self.players[2] == self.player:

            if self.n_players >= 3:
                print('-------------------------------------------------GAME-----------------------------------------------------------------')
                print()
                print('                                             Player:')
                print('                                                    ',self.players[1].name)
                print('                                             CARDS:')
                print('                                                    ',self.hide_deck2)
                print('                                             COINS:')
                print('                                                    ',self.players[1].coins)
                print()
                print('Player:                                                                                      Player:')
                print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
                print('CARDS:                                                                                       CARDS:')
                print('       ',self.hide_deck1,'                                                                                     ',self.players[2].playing_cards)
                print('COINS:                                                                                       COINS:')
                print('       ',self.players[0].coins,'                                                                                          ',self.players[2].coins)
            
                if self.n_players >= 4:
                    print()
                    print('                                             Player:')
                    print('                                                    ',self.players[3].name)
                    print('                                             CARDS:')
                    print('                                                    ',self.hide_deck4)
                    print('                                             COINS:')
                    print('                                                    ',self.players[3].coins)
                    print()


        elif self.players[3] == self.player:
            print('-------------------------------------------------GAME-----------------------------------------------------------------')
            print()
            print('                                             Player:')
            print('                                                    ',self.players[1].name)
            print('                                             CARDS:')
            print('                                                    ',self.hide_deck2)
            print('                                             COINS:')
            print('                                                    ',self.players[1].coins)
            print()
            print('Player:                                                                                      Player:')
            print('       ',self.players[0].name,'                                                                                          ',self.players[2].name)
            print('CARDS:                                                                                       CARDS:')
            print('       ',self.hide_deck1,'                                                                                     ',self.hide_deck3)
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

        









