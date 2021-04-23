import random
from players import Player
from showgame import Show_game
from play import Play




def main():

    players = []
    

    shuffle_deck = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
    random.shuffle(shuffle_deck)
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
        playing_cards = []
        hiden_deck = [[], []]


        player_deck.append(shuffle_deck[0])
        if shuffle_deck[0] == 1:
            playing_cards.append('Duke')
        elif shuffle_deck[0] == 2:
            playing_cards.append('Assassin')
        elif shuffle_deck[0] == 3:
            playing_cards.append('Capitan')
        elif shuffle_deck[0] == 4:
            playing_cards.append('Ambassador')
        elif shuffle_deck[0] == 5:
            playing_cards.append('Contessa')
        player_deck.append(shuffle_deck[1])
        if shuffle_deck[1] == 1:
            playing_cards.append('Duke')
        elif shuffle_deck[1] == 2:
            playing_cards.append('Assassin')
        elif shuffle_deck[1] == 3:
            playing_cards.append('Capitan')
        elif shuffle_deck[1] == 4:
            playing_cards.append('Ambassador')
        elif shuffle_deck[1] == 5:
            playing_cards.append('Contessa')

        shuffle_deck.pop(0)
        shuffle_deck.pop(0)
    
        players.append(Player(name, 2, player_deck, playing_cards, hiden_deck))
    
    Play.play(Play(players, n_players, shuffle_deck))

    


    
    
 



        
        


if __name__ == "__main__":
    main()
