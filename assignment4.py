_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

import random


# Generates a card value for the player at random. The value are between 1 and 10, with 10 being 4x likely.
def deal_card():
    card_one = random.randint(1, 13)
    if card_one == 11 or card_one == 12 or card_one == 13:
        card_one = 10
    return card_one


# Handles the initial deal of two cards to the player and the "HIT or STAY" loop, returns the final player score.
def get_player_score():
    player_sum = deal_card() + deal_card()
    print("Your hand of two cards now has a value of", str(player_sum) + ".")
    answer = input("Would you like to hit or stay? ")
    while answer == "Hit" or answer == "hit":
        player_sum += deal_card()
        if player_sum > 21:
            print("You BUSTED with a total value of", str(player_sum) + "!")
            print("** You lose. **")
            loop = input("Would you like to play again? (y/n) ")
            if loop == "Y" or loop == "y":
                main()
            if loop == "N" or loop == "n":
                exit()
            else:
                print("Invalid input, now exiting the program.")
                exit()
        print("Your hand now has a total value of", str(player_sum) + ".")
        answer = input("Would you like to hit or stay? ")
    if answer == 'Stay' or answer == 'stay':
        print("Your hand now has a total of", str(player_sum) + ".")
        return player_sum
    else:
        print("Invalid input, now exiting the program.")
        exit()


# Generates the dealer's score at random using deal_card().
def get_dealer_score():
    dealer_total = deal_card() + deal_card()
    while dealer_total < 16:
        dealer_total += deal_card()
        if dealer_total > 21:
            print("The dealer BUSTED with a value of", str(dealer_total) + "!")
            return dealer_total
        elif dealer_total >= 16 and dealer_total <= 21:
            print("The dealer was dealt a hand of", str(dealer_total) + ".")
            return dealer_total
    print("The dealer was dealt a hand of", str(dealer_total) + ".")
    return dealer_total


# The main function which includes the main loop that repeats each hand.
def main():
    final_player_score = get_player_score()
    final_dealer_score = get_dealer_score()
    if final_player_score > final_dealer_score or final_dealer_score > 21:
        print("** You win! **")
    else:
        print("** You lose. **")
    answer = input("Would you like to play again? (y/n) ")
    while answer == "Y" or answer == "y":
        main()
    if answer == "N" or answer == "n":
        exit()
    else:
        print("Invalid input, now exiting the program.")


main()














