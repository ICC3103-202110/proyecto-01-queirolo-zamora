from cards import Cards
from players import Player


def main():

    deck = []
    shuffle_deck = Cards.generate_deck(Cards(deck))
    while True:
        while True:
            number_of_players = input('How many players are going to play?(3 or 4) : ')

            try:
                if int(number_of_players):
                    break
            except ValueError:
            
                print('Insert a valid number of players!')
                print()
        
        n_players = int(number_of_players)
        
        if n_players == 3 or n_players == 4:
            break
        else:
            print('Insert a valid number of players!')
            print()


    for i in range(n_players):

        print('enter the name of player', i+1 ,':')

        name = input()
        player_deck = []
        player_deck.insert(shuffle_deck[0])
        player_deck.insert(shuffle_deck[1])
        shuffle_deck = shuffle_deck.pop(0)
        shuffle_deck = shuffle_deck.pop(0)

        Player(name, 2, player_deck)


        
        


if __name__ == "__main__":
    main()
