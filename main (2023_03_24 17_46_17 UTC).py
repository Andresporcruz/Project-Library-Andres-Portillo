#Defines the values
# Import library for random integer numbers
#Andres Portillo
#COP3502C
#02/09/2023
#BlackJack game

#Defines the values
# Import library for random integer numbers
import p1_random as p1

#Defines the values
def win(dealer_bust, player_bust, dealer_win, tie, player_win, player_blackjack):
    if dealer_bust:
        print('You win!')
        return 1
    elif player_bust:
        print('You exceeded 21! You lose.')
        return 0
    elif dealer_win:
        print('Dealer wins!')
        return 0
    elif tie:
        print("It's a tie! No one wins!")
        return 0
    elif player_win:
        print('You win!')
        return 1
    elif player_blackjack:
        print('BLACKJACK! You win!')
        return 1

def main():

    # defining variables inside main
    game_continue = True
    player_hand = 0
    menu = '1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n'
    dealer_wins = 0
    player_wins = 0
    game_num = 1
    tie_games = 0

    # creating an array that includes the names of the cards and their corresponding values
    cards = [
        ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING'],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ]

    rng = p1.P1Random()
    new_card = rng.next_int(13) + 1
    player_hand += cards[1][new_card - 1]

    print(f'START GAME #{game_num}\n')
    print('Your card is a ' + cards[0][new_card - 1] + '!')
    print(f'Your hand is: {player_hand}\n')
    print(menu)

    # while loop so that the game will continue for as long as the player wants to play
    while game_continue:

        # takes an input from the player of the menu options
        menu_select = int(input('Choose an option: '))
        print()

        # using a match case statement to more easily format how the program will
        # progress when a menu selection is picked
        if menu_select == 2:

            dealer_hand = rng.next_int(11) + 16

            print('Dealer\'s hand:', dealer_hand)
            print(f'Your hand is: {player_hand}\n')

            if dealer_hand > 21:
                player_wins += 1
                print('You win!')

            elif player_hand > dealer_hand and player_hand <= 21:
                player_wins += 1
                print('You win!')

            elif player_hand < dealer_hand and dealer_hand <= 21:
                dealer_wins += 1
                print('Dealer wins!')


            elif player_hand == dealer_hand:
                tie_games += 1
                print("It's a tie! No one wins!")


            elif player_hand > dealer_hand and player_hand == 21:
                player_wins += 1
                print('BLACKJACK! You win!')

            player_hand = 0
            game_num += 1
            new_card = rng.next_int(13) + 1
            player_hand += cards[1][new_card - 1]

            print(f'START GAME #{game_num}\n')
            print('Your card is a ' + cards[0][new_card - 1] + '!')
            print(f'Your hand is: {player_hand}\n')
            print(menu)

        elif menu_select == 1:
            # creates a new value from p1.random and sets it equal to the player's hand
            new_card = rng.next_int(13) + 1

            # adds the new card value to the player's hand
            player_hand += cards[1][new_card - 1]

            if player_hand > 21:
                print('Your card is a ' + cards[0][new_card - 1] + '!')
                print(f'Your hand is: {player_hand}\n')
                win(False, True, False, False, False,)
                print()
                player_wins += 0
                dealer_wins += 1
                player_hand = 0
                game_num += 1
                new_card = rng.next_int(13) + 1
                player_hand += cards[1][new_card - 1]
                print(f'START GAME #{game_num}\n')
                print('Your card is a ' + cards[0][new_card - 1] + '!')
                print(f'Your hand is: {player_hand}\n')
                print(menu)
            if player_hand == 21:
                print('Your card is a ' + cards[0][new_card - 1] + '!')
                print(f'Your hand is: {player_hand}\n')
                win(False, False, False, False, False, True)
                print()
                player_wins += 1
                player_hand = 0
                game_num += 1
                new_card = rng.next_int(13) + 1
                player_hand += cards[1][new_card - 1]
                print(f'START GAME #{game_num}\n')
                print('Your card is a ' + cards[0][new_card - 1] + '!')
                print(f'Your hand is: {player_hand}\n')
                print(menu)
            else:
                print('Your card is a ' + cards[0][new_card - 1] + '!')
                print(f'Your hand is: {player_hand}\n')
                print(menu)
        elif menu_select == 3:
            # calculate and print statistics
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie_games}')
            total_games = player_wins + dealer_wins + tie_games
            percentage_won = (player_wins / total_games) * 100
            print(f'Total # of games played is:  {total_games: }')
            print(f'Percentage of Player wins: {percentage_won:.1f}%')
            print()
            print(menu)

        elif menu_select == 4:
            game_continue = False
        else:
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.')
            print(menu)


        def main():
            game_continue()

if __name__ == '__main__':
    main()






