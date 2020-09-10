_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'


import random

card_value = None
card_total = None
dealer_card = None
card_sum = None



# generate a card value for the player (using random). This should be used within the get_player_score function. The value should be between 1 and 10.
def deal_card():
    card_one = random.randint(1, 10)
    card_two = random.randint(1, 10)
    card_value = card_one + card_two
    return card_value





# handles the initial deal of two cards to the player and the "HIT or STAY" loop. It should return the final player score.
def get_player_score():
    player_card = deal_card
    print("Your hand now has a value of", str(player_card) + "." )
    answer = input("Would you like to hit or stay?")
    # while answer != 'EXIT':
    if answer == "Hit" or answer == "hit":
        player_sum = player_card + deal_card()
        print("Your hand now has a total value of", str(player_sum) + ".")
        return player_sum
    elif answer == "Stay" or answer == "stay":
        print("You have stopped taking more cards with a hand value of", str(player_card) + ".")
        return player_card







# generate the dealer's score (using random)
def get_dealer_score():
    dealer_card_one = random.randint(16,21)
    dealer_card_two = random.randint(16,21)
    dealer_sum = dealer_card_one + dealer_card_two
    if dealer_sum > 21:
        print("The dealer BUSTED with a value of", str(dealer_sum) + "!")
    if dealer_sum < 16:
        dealer_sum + random.randint(1, 10)





# the main function, which should have the main loop that repeats for each hand
def main():
    loop = input("Would you like to play a game of blackjack? (y/n)" )
    # while loop != 'EXIT':
    if loop == "Y" or loop == "y":
        get_player_score()
        get_dealer_score()
    elif loop == "N" or loop == "n":
        exit()





# Deal two cards to the user, compute the sum, and display it to the user. (Remember, a card is just a random number form 1 to 10)
deal_card()

#Ask the user if he/she wishes to HIT or STAY.
answer = input("Would you like to hit or stay? ")

#Each time the user chooses to HIT, deal him/her a new card, update the total, and check to see if he/she has gone bust (over the limit of 21)
if answer == "Y" or answer == "y":
    card_sum = card_value + random.randint(1,10)
    if card_value > 21:
        print("You lose")
    elif card_value < 21:
        input("Would you like to hit or stay? (y/n) ")
elif answer == "N" or answer == 'n':
    print("Your hand now has a total value of", str(card_value) + ".")

#Eventually, the player will choose to stay or go bust. If the player goes bust, he/she automatically loses. If not, then the computer gets its turn
if card_value > 21:
    print("**You lose!**")
    exit()
elif card_value < 21:
    get_dealer_score()

#Generate the computer's score and compare it to the player's score and determine who wins. The computer's score should be a random number between 16 and 21
dealer_score = get_dealer_score()
if dealer_score:


#Ask the user if he or she is ready to play a new hand of blackjack. If so, your program should go to back to step 1. If not, your program should quit.
input_answer = input("Would you like to play a new hand of blackjack? (y/n)" )
if input_answer == 'Y' or answer == 'y':
    main()
elif input_answer == "N" or input_answer == 'n':
    exit()












