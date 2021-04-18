
class Player():

    def __init__(self, name, coins, cards):
        self.name = name
        self.coins = coins
        self.cards = cards

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
                
        