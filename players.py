
class Player():

    def __init__(self, name, coins, cards, playing_cards, hiden_deck):
        self.name = name
        self.coins = coins
        self.cards = cards
        self.playing_cards = playing_cards
        self.hiden_deck = hiden_deck

        

    def change_amount_coins(self, value):
        self.coins = self.coins + value
    
    def add_card (self, card):
        self.cards.append(card)
    
    def remove_card (self, card):
        self.cards.remove(card)

    def coins_setter(self, value):
        if value < 0:
            self.coins = 0
        else:
            self.coins = value
                
        