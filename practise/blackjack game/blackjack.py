###################### Our Blackjack House Rules ######################
## The deck is of unllimited size
## There are no jokers
## The Jack/Queen/King all count as 10
## The Ace can count as 11 or 1
## Each has an equal probability of being drawn
## A card is not removed from the deck as they are drawn 

import random

cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    comp_hand = random.choices(cards, k=2)
    my_hand = random.choices(cards, k=2)
    
    #user and comp total
    comp_total = comp_hand[0] + comp_hand[1]
    my_total = my_hand[0] + my_hand[1]
    
    #reveal my hands
    print(f'my hand: {my_hand[:2]} current score: {my_hand[0] + my_hand[1]}')
    #reveal comp's first hand
    print(f'comp first hand: {comp_hand[0]}')
    
    

    
    #detect if a blackjack is drawn
    if comp_hand[0] == cards[0] or comp_hand[1] == cards[0]:
        if comp_hand[0] == 10 or comp_hand[1] == 10:
            comp_total = comp_hand[0] + comp_hand[1]
            return comp_total
    elif my_hand[0] == cards[0] or my_hand[1] == cards[0]:
        if my_hand[0] == 10 or my_hand[1] == 10:
            my_total = my_hand[0] + my_hand[1]
            return my_total


    #If Ace is drawn
    if comp_hand[0] == cards[0] or comp_hand[1] == cards[0]:
        if comp_total >= 21:
            comp_total -= 10
    elif my_hand[0] == cards[0] or my_hand[1] == cards[0]:
        if my_total >= 21:
            my_total -= 10
            



    print(f'comp total: {comp_total}')
    print(f'my total: {my_total}')     
            
blackjack()