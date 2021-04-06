import random
from players import Player


def main():

    shuffle_deck = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
    random.shuffle(shuffle_deck)
    print(shuffle_deck)
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
        player_deck.append(shuffle_deck[0])
        player_deck.append(shuffle_deck[1])
        shuffle_deck.pop(0)
        print(shuffle_deck)
        shuffle_deck.pop(0)
        print(shuffle_deck)

        Player(name, 2, player_deck)


    for i in range(n_players):
        print("Nombre: ", Player[i].name)
        
        


if __name__ == "__main__":
    main()
