



def main():

    while True:
        number_of_players = input('How many players are going to play?(3 or 4) : ')

        try:
            if int(number_of_players):
                break
        except ValueError:
            print('Insert a valid number of players!')
    
    n_players = int(number_of_players)
    print(n_players)

    


if __name__ == "__main__":
    main()
