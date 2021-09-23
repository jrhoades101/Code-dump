
adventure_points = 10
end_game = 0

def greet():
    global adventure_points
    """Greeting the gamer."""
    name: str = input("What is your name? ")
    print("Hello " + name + ".")
    print("You will now be participating in a adventure where you decide what happens next.")
    print('You will be starting off with 10 adventure points.')
    return name


def hallway():
    global adventure_points
    global end_game
    print('You have reached a hallway...')
    print('')
    print('You have three directions to choose from.')
    print('Go straight, go to the left, or go to the right')
    print('')
    direction = input('Which direction will you choose? ')
    if direction == 'Straight' or direction == 'straight':
        print('You have found a secret room and have collected a treasure map.')
        print('This treasure map allows you to see hidden traps throughout this cave')
        adventure_points = adventure_points + 10
        print('Enjoy 10 adventure points for your find!')
        print('')
        print('You not have', + adventure_points, 'adventure points')
        return adventure_points
    if direction == 'Left' or direction == 'left':
        print('You have stumbled upon a special drink')
        print('You decide to drink the unknown substance without being aware what is in it')
        print('')
        print('')
        print('You start to feel ill from the drink')
        print('You notice that you can buy an antidote from an unknown figure')
        print('This antidote will cost 5 adventure points')
        antidote = input('Do you wish to purchase this antidote? ')
        if antidote == 'Yes' or antidote == 'yes':
            adventure_points = adventure_points - 5
            print('You have spent 5 adventure points on the antidote')
            print('You now have', + adventure_points, 'adventure points remaining')
            return adventure_points
        if antidote == 'No' or antidote == 'no':
            print("You will slowly fade away into death now")
        else:
            print('Please make a decision regarding the purchase of the antidote')
            antidote_question = input('Do you wish to purchase this antidote? ')
            while antidote_question != 'yes' or antidote_question != 'no':
                if antidote_question == 'Yes' or antidote_question == 'yes':
                    adventure_points = adventure_points - 5
                    print('You have spent 5 adventure points on the antidote')
                    print('You now have', + adventure_points, 'adventure points remaining')
                    return adventure_points
                if antidote_question == 'No' or antidote_question == 'no':
                    print("You will slowly fade away into death now")
                    return
    if direction == 'Right' or direction == 'right':
        print('You have found a mysterious device')
        print('')
        print('You use this device and find that it teleports you to the outside of the cave')
        print('Enjoy 100 adventure points for finding the exit')
        adventure_points = adventure_points + 100
        print('')
        print('You have finished the game with', + adventure_points, 'adventure points')
        return end_game == 1





def doors():
    global adventure_points
    print("Two doors are in front of you.")
    x = input("Do you pick the left one or the right one?  ... or quit like a scaredy cat? ")
    if x == "left":
        # option_1 = 1
        adventure_points = adventure_points + 5
        return adventure_points
    if x == "right":
        # option_2 = 2
        adventure_points = adventure_points + 2
        return adventure_points
    else:
        print("Scared! ")
        return


def gameover():
    print('The game is over. Thanks for playing!')
    print('You have accumulated', + adventure_points, 'adventure points.')



def main():
    greet()
    # print('')
    print('')
    hallway()
    print('')
    if end_game == 0:
        doors()
        gameover()
    if end_game == 1:
        print('Thanks for playing!')
        return
    replay = input("Do you want to play again? ")
    while replay != 'yes' or replay != 'no':
        if replay == 'yes':
            print('')
            print("Hooray! ")
            main()
        if replay == 'no':
            print("Maybe some other time! Thanks for playing! ")
            return
        else:
            print('Invalid input, now exiting the game ')
            return




if __name__ == "__main__":
    main()
