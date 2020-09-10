_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

import random

card_value = None
card_total = None
dealer_card = None


# Generate a card value for the player (using random).
def deal_card():
    card_one = random.randint(1, 10)
    card_two = random.randint(1, 10)
    card_value = card_one + card_two
    return card_value


# Generate the player's score (using random).
def get_player_score():
    card_value = deal_card()
    print("Your hand of two cards has a total value of", str(card_value) + ".", )
    answer = input("Would you like to take another card? (y/n) ")
    if answer == "Y" or answer == "y":
        card_sum = card_value + random.randint(1,10)
        if card_sum > 21:
            print("You lose!")
        elif card_sum < 21:
            print("Your hand of two cards has a total value of", str(card_sum) + ".", )
    elif answer == "N" or answer == "n":
        print("You have stopped taking more cards with a hand value of", str(card_value) + ".")
    return card_value



# Generate the dealer's score (using random).
def get_dealer_score():
    dealer_score = deal_card()
    dealer_card = dealer_score + random.randint(16,21)
    if dealer_card > 21:
        print("The dealer has busted with a value of", str(dealer_card)+ ".")
    elif dealer_card < 21:





# The main function which will include the main loop
def main():
    get_player_score()
    get_dealer_score()


   




main()





































