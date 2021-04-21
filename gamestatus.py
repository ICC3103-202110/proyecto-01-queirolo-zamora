from abc import ABC
from abc import abstractmethod
from showgame import Show_game


class Gamestatus(ABC):



    def __init__ (self, player, players, n_players):
        self.player = player
        self.players = players
        self.n_players = n_players
        


    def Change_gamestatus(self,choosen_player,value):

        if choosen_player == self.players[0]:
            self.players[0].hiden_deck.pop(value-1)
            self.players[0].hiden_deck.append(self.players[0].playing_cards[value-1])
            self.players[0].cards.pop(value-1)
            self.players[0].cards.append(0)

            self.players[0].playing_cards.pop(value-1)
            self.players[0].playing_cards.append('-------')


        elif choosen_player == self.players[1]:
            self.players[1].hiden_deck.pop(value-1)
            self.players[1].hiden_deck.append(self.players[1].playing_cards[value-1])
            self.players[1].cards.pop(value-1)
            self.players[1].cards.append(0)

            self.players[1].playing_cards.pop(value-1)
            self.players[1].playing_cards.append('-------')

        elif choosen_player == self.players[2]:
            self.players[2].hiden_deck.pop(value-1)
            self.players[2].hiden_deck.append(self.players[2].playing_cards[value-1])
            self.players[2].cards.pop(value-1)
            self.players[2].cards.append(0)

            self.players[2].playing_cards.pop(value-1)
            self.players[2].playing_cards.append('-------')

        elif choosen_player == self.players[3]:
            self.players[3].hiden_deck.pop(value-1)
            self.players[3].hiden_deck.append(self.players[3].playing_cards[value-1])
            self.players[3].cards.pop(value-1)
            self.players[3].cards.append(0)

            self.players[3].playing_cards.pop(value-1)
            self.players[3].playing_cards.append('-------')
        
        if choosen_player.cards[0] == 0 and choosen_player.cards[1] == 0 :
            print (choosen_player, 'Lose!')
            self.players.remove(choosen_player)
            

        
    def Show_gamestatus(self):
        Show_game.show_game(Show_game(
            self.player, self.players, self.n_players))