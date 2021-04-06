



def main():
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

        


if __name__ == "__main__":
    main()
