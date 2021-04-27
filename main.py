import random

deck = ["ace_heart", "ace_diamond", "ace_club", "ace_spade", 
        "two_heart", "two_diamond", "two_club", "two_spade",
        "three_heart", "three_diamond", "three_club", "three_spade",
        "four_heart", "four_diamond", "four_club", "four_spade",
        "five_heart", "five_diamond", "five_club", "five_spade",
        "six_heart", "six_diamond", "six_club", "six_spade",
        "seven_heart", "seven_diamond", "seven_club", "seven_spade",
        "eight_heart", "eight_diamond", "eight_club", "eight_spade",
        "nine_heart", "nine_diamond", "nine_club", "nine_spade",
        "ten_heart", "ten_diamond", "ten_club", "ten_spade",
        "jack_heart", "jack_diamond", "jack_club", "jack_spade",
        "queen_heart", "queen_diamond", "queen_club", "queen_spade",
        "queen_heart", "queen_diamond", "queen_club", "queen_spade",]


# What you see in terminal starts here

print("\n")
print ("******************************************")
print ("          Welcome to BlackJack!!!")
print ("******************************************")
print("\n")

print ("Please press enter to continue.")

input()

print ("Hello, ")
print ("Type 'play' to start playing.")
print ("Type 'rules' to look at the rules.")


# Game starts here

def start_game():

        hand = 0

        print("\n")

        print ("Press 'h' to hit or press 's' to stand.")

        h_s = input()

        print("\n")

        # If player 'hits'

        if h_s == "h":
                print ("hit!")

                print("\n")

                chosen_card = random.choice(deck)

                if chosen_card == "two_heart":
                        print ("Two of Hearts")
                        
                        added_value = 2

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "two_diamond":
                        print ("Two of Diamonds")

                        added_value = 2

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "two_club":
                        print ("Two of Clubs")

                        added_value = 2

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "two_spade":
                        print ("Two of Spades")

                        added_value = 2

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "three_heart":
                        print ("Three of Hearts")

                        added_value = 3

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "three_diamond":
                        print ("Three of Diamonds")

                        added_value = 3

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "three_club":
                        print ("Three of Clubs")

                        added_value = 3

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "three_spade":
                        print ("Three of Spades")

                        added_value = 3

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "four_heart":
                        print ("Four of Hearts")

                        added_value = 4

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "four_diamond":
                        print ("Four of Diamonds")

                        added_value = 4

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "four_club":
                        print ("Four of Clubs")

                        added_value = 4

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "four_spade":
                        print ("Four of Spades")

                        added_value = 4

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "five_heart":
                        print ("Five of Hearts")

                        added_value = 5

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "five_diamond":
                        print ("Five of Diamonds")

                        added_value = 5

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "five_club":
                        print ("Five of Clubs")

                        added_value = 5

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "five_spade":
                        print ("Five of Spades")

                        added_value = 5

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "six_heart":
                        print ("Six of Hearts")

                        added_value = 6

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "six_diamond":
                        print ("Six of Diamonds")

                        added_value = 6

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "six_club":
                        print ("Six of Clubs")

                        added_value = 6

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "six_spade":
                        print ("Six of Spades")

                        added_value = 6

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "seven_heart":
                        print ("Seven of Hearts")

                        added_value = 7

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "seven_diamond":
                        print ("Seven of Diamonds")

                        added_value = 7

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "seven_club":
                        print ("Seven of Clubs")

                        added_value = 7

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "seven_spade":
                        print ("Seven of Spades")

                        added_value = 7

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "eight_heart":
                        print ("Eight of Hearts")

                        added_value = 8

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "eight_diamond":
                        print ("Eight of Diamonds")

                        added_value = 8

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "eight_club":
                        print ("Eight of Clubs")

                        added_value = 8

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "eight_spade":
                        print ("Eight of Spades")

                        added_value = 8

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "nine_heart":
                        print ("Nine of Hearts")

                        added_value = 9

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "nine_diamond":
                        print ("Nine of Diamonds")

                        added_value = 9

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "nine_club":
                        print ("Nine of Clubs")

                        added_value = 9

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "nine_spade":
                        print ("Nine of Spades")

                        added_value = 9

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "ten_heart":
                        print ("Ten of Hearts")

                        added_value = 10

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "ten_diamond":
                        print ("Ten of Diamonds")

                        added_value = 10

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "ten_club":
                        print ("Ten of Clubs")

                        added_value = 10

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "ten_spade":
                        print ("Ten of Spades")

                        added_value = 10

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "jack_heart":
                        print ("Jack of Hearts")

                        added_value = 11

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "jack_diamond":
                        print ("Jack of Diamonds")

                        added_value = 11

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "jack_club":
                        print ("Jack of Clubs")

                        added_value = 11

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "jack_spade":
                        print ("Jack of Spades")

                        added_value = 11

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "queen_heart":
                        print ("Queen of Hearts")

                        added_value = 12

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "queen_diamond":
                        print ("Queen of Diamonds")

                        added_value = 12

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "queen_club":
                        print ("Queen of Clubs")

                        added_value = 12

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "queen_spade":
                        print ("Queen of Spades")

                        added_value = 12

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "king_heart":
                        print ("King of Hearts")

                        added_value = 13

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "king_diamond":
                        print ("King of Diamonds")

                        added_value = 13

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "king_club":
                        print ("King of Clubs")

                        added_value = 13

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                elif chosen_card == "king_spade":
                        print ("King of Spades")

                        added_value = 13

                        hand = hand + added_value

                        print("\n")

                        print ("The total value of your cards is:")
                        print (hand)

                # To determine the value of aces

                elif chosen_card == "ace_heart":
                        print ("Ace of Hearts")

                        print("\n")

                        print ("Do you want your Ace to be worth 1 or 11?")

                        def determine_ace_value(hand):

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)

                                elif ace_value == "11":
                                        added_value = 11

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)
                                else:
                                        print ("Please enter 1 or 11.")
                                        determine_ace_value()

                        a = determine_ace_value(hand)


                elif chosen_card == "ace_diamond":
                        print ("Ace of Diamonds")

                        print("\n")

                        print ("Do you want your Ace to be worth 1 or 11?")

                        def determine_ace_value(hand):

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)

                                elif ace_value == "11":
                                        added_value = 11

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)
                                else:
                                        print ("Please enter 1 or 11.")
                                        determine_ace_value()

                        a = determine_ace_value(hand)


                elif chosen_card == "ace_club":
                        print ("Ace of Clubs")

                        print("\n")

                        print ("Do you want your Ace to be worth 1 or 11?")

                        def determine_ace_value(hand):

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)

                                elif ace_value == "11":
                                        added_value = 11

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)
                                else:
                                        print ("Please enter 1 or 11.")
                                        determine_ace_value()

                        a = determine_ace_value(hand)


                elif chosen_card == "ace_spade":
                        print ("Ace of Spades")

                        print("\n")

                        print ("Do you want your Ace to be worth 1 or 11?")

                        def determine_ace_value(hand):

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)

                                elif ace_value == "11":
                                        added_value = 11

                                        hand = hand + added_value

                                        print("\n")

                                        print ("The total value of your cards is:")
                                        print (hand)
                                else:
                                        print ("Please enter 1 or 11.")
                                        determine_ace_value()

                        a = determine_ace_value(hand)


                # This should not happen, but if it does, it means that something went wrong and there was an error

                else:
                        print ("Something went wrong.")

        # If player 'stands'

        elif h_s == "s":
                print ("stand!")

        # If player hits something else

        else:
                print ("Please press 'h' or 's'.")

# Game ends here





# Rules start here

def show_rules():
        print("\n")

        print ("The goal of BlackJack is to get as close to 21 as possible without going over it.")
        print ("You must do this by 'hitting'.")
        print ("When you 'hit', you will receive a random card from the deck of 52 cards.")
        print ("You can 'hit' as many times as you want and you have to add up the value of all your cards.")
        print ("However, the combined value of your cards cannot exceed 21 or else you automatically lose.")
        print ("If you deem that the value of all your cards is high enough and it's too risky to 'hit', you can 'stand'.")
        print ("Once you 'stand', you will no longer pick up any cards and you must wait until everyone else 'stands'.")
        print ("Once everyone is 'standing' you must compare your cards with that of the other players.")
        print ("Whoever's cards have a combined value closest to 21, without exceeding it, wins.")
        print ("Note: an Ace can either be worth a 1 or an 11 based on your choosing and Jokers are not present in this game.")

        print("\n")

        print("Type 'play' when you are ready to play.")


        def exit_rules():
                type_play = input()

                if type_play == "play":
                        start_game()
                else:
                        print("\n")
                        print("Please type 'play' to start the game.")

                        exit_rules()

        
        x = exit_rules()

        

# Rules end here


def choose_play_rules ():

        play_rules = input ()

        if play_rules == "play":
                start_game()
        elif play_rules == "rules":
                show_rules()
        else:
                print("\n")

                print ("Please type 'play' or 'rules'.")

                choose_play_rules()
        
        print("\n")


y = choose_play_rules ()