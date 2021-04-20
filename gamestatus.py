from abc import ABC
from abc import abstractmethod



class Gamestatus(ABC):

    a = [[],[]]
    hide_deck1 = a
    hide_deck2 = a
    hide_deck3 = a
    hide_deck4 = a

    def __init__ (self, player, players, n_players):
        self.player = player
        self.players = players
        self.n_players = n_players

    def Change_gamestatus(self,choosen_player,value):

        if choosen_player == self.players[0]:
            hiden_deck1.remove(value)
            hiden_deck1.append(self.players[0].playing_cards[value])
            self.players[0].cards.remove[value]
            self.players[0].cards.append(0)
        elif choosen_player == self.players[1]:
            hiden_deck1.remove(value)
            hiden_deck1.append(self.players[1].playing_cards[value])
            self.players[1].cards.remove[value]
            self.players[1].cards.append(0)
        elif choosen_player == self.players[2]:
            hiden_deck1.remove(value)
            hiden_deck1.append(self.players[2].playing_cards[value])
            self.players[2].cards.remove[value]
            self.players[2].cards.append(0)
        elif choosen_player == self.players[3]:
            hiden_deck1.remove(value)
            hiden_deck1.append(self.players[3].playing_cards[value])
            self.players[3].cards.remove[value]
            self.players[3].cards.append(0)
        
    def Show_gamestatus(self):
        Show_game.show_game(Show_game(self.player, self.players, self.n_players,
         self.hide_deck1, self.hide_deck2, self.hide_deck3, self.hide_deck4))