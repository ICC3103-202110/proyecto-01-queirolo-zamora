
class jugador():

    #CONSTANTES
    MIN_COINS = 0

    #CONSTRICTOR
    def __init__(self, name, coins, cards):
        self.__name = name
        self.__coins = coins
        self.__cards = cards

    @property
    def name(self):
        return self.__name

    @property
    def coins(self):
        return self.__coins

    @property
    def cards(self):
        return self.__cards

    #GETTER Y SETTER
    @coins.setter
    def coins_setter(self, value):
        if vulue < MIN_COINS:
            self.__coins = self.MIN_COINS
        else:
            self.__coins  =value
    #MÉTODOS

   

    