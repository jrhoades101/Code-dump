_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

import random


# Generates a card value for the player at random. The value are between 1 and 10, with 10 being 4x likely.
def deal_card():
    # Generates a random integer value from 1 to 10 with 10 being 4x as likely.
    card_one = random.randint(1, 13)
    if card_one == 11 or card_one == 12 or card_one == 13:
        card_one = 10
    # Returns the card value that was randomly chosen above.
    return card_one


# Handles the initial deal of two cards to the player and the "HIT or STAY" loop, returns the final player score.
def get_player_score():
    # player_sum adds together two random values that were drawn randomly in the function 'deal_card()'.
    player_sum = deal_card() + deal_card()
    print("Your hand of two cards now has a value of", str(player_sum) + ".")
    # This while loop preforms the 'Hit or Stay' loop.
    answer = input("Would you like to hit or stay? ")
    while answer == "Hit" or answer == "hit":
        # Adds an additional random value from the function 'deal_card()' to the player_sum variable.
        player_sum += deal_card()
        # If player_sum is greater than 21, player busts but is given the option to play the game again.
        if player_sum > 21:
            print("You BUSTED with a total value of", str(player_sum) + "!")
            print("** You lose. **")
            # This input sets up the if/elif statement to ask if the user would like to play.
            loop = input("Would you like to play again? (y/n) ")
            if loop == "Y" or loop == "y":
                main()
            elif loop == "N" or loop == "n":
                exit()
            else:
                print("Invalid input, now exiting the program.")
                exit()
        print("Your hand now has a total value of", str(player_sum) + ".")
        answer = input("Would you like to hit or stay? ")
    # If answer is stay, it prints the total value of the hand and returns that value.
    if answer == 'Stay' or answer == 'stay':
        print("Your hand now has a total of", str(player_sum) + ".")
        return player_sum
    # If anything else is inputted, it results in a invalid input and ends the program.
    else:
        print("Invalid input, now exiting the program.")
        exit()


# Generates the dealer's score at random using deal_card().
def get_dealer_score():
    # dealer_total adds together two random values drawn from the function 'deal_card()'.
    dealer_total = deal_card() + deal_card()
    # This while loop is performed when the dealer card value is less than 16.
    while dealer_total < 16:
        dealer_total += deal_card()
        # If dealer_total is greater than 21, the dealer will bust.
        if dealer_total > 21:
            print("The dealer BUSTED with a value of", str(dealer_total) + "!")
            return dealer_total
        elif dealer_total >= 16 and dealer_total <= 21:
            print("The dealer was dealt a hand of", str(dealer_total) + ".")
            return dealer_total
    # If dealer_total is over 16, it will bypass the loop and print the dealer's hand.
    print("The dealer was dealt a hand of", str(dealer_total) + ".")
    return dealer_total


# The main function which includes the main loop that repeats each hand.
def main():
    final_player_score = get_player_score()
    final_dealer_score = get_dealer_score()
    # If statement that will check to see if final player score is greater than the deal or if dealer score is over 21.
    if final_player_score > final_dealer_score or final_dealer_score > 21:
        print("** You win! **")
    else:
        print("** You lose. **")
    # Loop that will ask the player if they would like to play again.
    answer = input("Would you like to play again? (y/n) ")
    while answer == "Y" or answer == "y":
        main()
    if answer == "N" or answer == "n":
        exit()
    else:
        print("Invalid input, now exiting the program.")
        exit()


main()














