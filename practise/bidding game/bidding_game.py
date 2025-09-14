from art import logo
from clear_console import clear

def bidding_game():
    print(logo)
    print('welcome to the secret auction program.')
    bidders = {}
    continue_bidding = 'yes'
    
    while continue_bidding == "yes":
        name = input("What is your name?: ")
        amount = int(input("What amount do you bid?: ksh "))
        bidders[name] = amount  

        continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        
        if continue_bidding == 'yes':
            clear()

    return bidders

def find_winner(bidders):
    winner_bid = max(bidders.values())

    for key, value in bidders.items():
        if value == winner_bid:
            print(f'the winner is {key} with a bid of {winner_bid}')

all_bidders = bidding_game()
find_winner(all_bidders)