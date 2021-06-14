import random
import os

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
        "king_heart", "king_diamond", "king_club", "king_spade",]


# What you see in terminal starts here

os.system('cls' if os.name == 'nt' else 'clear')

print("\n")
print ("******************************************")
print ("          Welcome to BlackJack!!!")
print ("******************************************")
print("\n")

print ("Type 'play' to start playing.")
print ("Type 'rules' to look at the rules.")
print ("Type 'exit' to exit.")


# Game starts here

def start_game():

        # Player variables
        hand = 0

        added_value = 0


        # Dealer variables
        dealer_hand = 0

        added_value_dealer = 0


        print("\n")


        # To pick and remove the first two cards drawn from the deck for the player and the dealer

        first_card_drawn = random.choice(deck)
        deck.remove(first_card_drawn)

        second_card_drawn = random.choice(deck)
        deck.remove(second_card_drawn)


        first_card_drawn_dealer = random.choice(deck)
        deck.remove(first_card_drawn_dealer)

        second_card_drawn_dealer = random.choice(deck)
        deck.remove(second_card_drawn_dealer)


        # To determine the value of the first card drawn

        if first_card_drawn == "two_heart":
                first_card_drawn = "Two of Hearts"
                added_value = 2

        elif first_card_drawn == "two_diamond":
                first_card_drawn = "Two of Diamonds"
                added_value = 2

        elif first_card_drawn == "two_club":
                first_card_drawn = "Two of Clubs"
                added_value = 2

        elif first_card_drawn == "two_spade":
                first_card_drawn = "Two of Spades"
                added_value = 2

        elif first_card_drawn == "three_heart":
                first_card_drawn = "Three of Hearts"
                added_value = 3

        elif first_card_drawn == "three_diamond":
                first_card_drawn = "Three of Diamonds"
                added_value = 3

        elif first_card_drawn == "three_club":
                first_card_drawn = "Three of Clubs"
                added_value = 3

        elif first_card_drawn == "three_spade":
                first_card_drawn = "Three of Spades"
                added_value = 3

        elif first_card_drawn == "four_heart":
                first_card_drawn = "Four of Hearts"
                added_value = 4

        elif first_card_drawn == "four_diamond":
                first_card_drawn = "Four of Diamonds"
                added_value = 4

        elif first_card_drawn == "four_club":
                first_card_drawn = "Four of Clubs"
                added_value = 4

        elif first_card_drawn == "four_spade":
                first_card_drawn = "Four of Spades"
                added_value = 4

        elif first_card_drawn == "five_heart":
                first_card_drawn = "Five of Hearts"
                added_value = 5

        elif first_card_drawn == "five_diamond":
                first_card_drawn = "Five of Diamonds"
                added_value = 5

        elif first_card_drawn == "five_club":
                first_card_drawn = "Five of Clubs"
                added_value = 5

        elif first_card_drawn == "five_spade":
                first_card_drawn = "Five of Spades"
                added_value = 5

        elif first_card_drawn == "six_heart":
                first_card_drawn = "Six of Hearts"
                added_value = 6

        elif first_card_drawn == "six_diamond":
                first_card_drawn = "Six of Diamonds"
                added_value = 6

        elif first_card_drawn == "six_club":
                first_card_drawn = "Six of Clubs"
                added_value = 6

        elif first_card_drawn == "six_spade":
                first_card_drawn = "Six of Spades"
                added_value = 6

        elif first_card_drawn == "seven_heart":
                first_card_drawn = "Seven of Hearts"
                added_value = 7

        elif first_card_drawn == "seven_diamond":
                first_card_drawn = "Seven of Diamonds"
                added_value = 7

        elif first_card_drawn == "seven_club":
                first_card_drawn = "Seven of Clubs"
                added_value = 7

        elif first_card_drawn == "seven_spade":
                first_card_drawn = "Seven of Spades"
                added_value = 7

        elif first_card_drawn == "eight_heart":
                first_card_drawn = "Eight of Hearts"
                added_value = 8

        elif first_card_drawn == "eight_diamond":
                first_card_drawn = "Eight of Diamonds"
                added_value = 8

        elif first_card_drawn == "eight_club":
                first_card_drawn = "Eight of Clubs"
                added_value = 8

        elif first_card_drawn == "eight_spade":
                first_card_drawn = "Eight of Spades"
                added_value = 8

        elif first_card_drawn == "nine_heart":
                first_card_drawn = "Nine of Hearts"
                added_value = 9

        elif first_card_drawn == "nine_diamond":
                first_card_drawn = "Nine of Diamonds"
                added_value = 9

        elif first_card_drawn == "nine_club":
                first_card_drawn = "Nine of Clubs"
                added_value = 9

        elif first_card_drawn == "nine_spade":
                first_card_drawn = "Nine of Spades"
                added_value = 9

        elif first_card_drawn == "ten_heart":
                first_card_drawn = "Ten of Hearts"
                added_value = 10

        elif first_card_drawn == "ten_diamond":
                first_card_drawn = "Ten of Diamonds"
                added_value = 10

        elif first_card_drawn == "ten_club":
                first_card_drawn = "Ten of Clubs"
                added_value = 10

        elif first_card_drawn == "ten_spade":
                first_card_drawn = "Ten of Spades"
                added_value = 10

        elif first_card_drawn == "jack_heart":
                first_card_drawn = "Jack of Hearts"
                added_value = 10

        elif first_card_drawn == "jack_diamond":
                first_card_drawn = "Jack of Diamonds"
                added_value = 10

        elif first_card_drawn == "jack_club":
                first_card_drawn = "Jack of Clubs"
                added_value = 10

        elif first_card_drawn == "jack_spade":
                first_card_drawn = "Jack of Spades"
                added_value = 10

        elif first_card_drawn == "queen_heart":
                first_card_drawn = "Queen of Hearts"
                added_value = 10

        elif first_card_drawn == "queen_diamond":
                first_card_drawn = "Queen of Diamonds"
                added_value = 10

        elif first_card_drawn == "queen_club":
                first_card_drawn = "Queen of Clubs"
                added_value = 10

        elif first_card_drawn == "queen_spade":
                first_card_drawn = "Queen of Spades"
                added_value = 10

        elif first_card_drawn == "king_heart":
                first_card_drawn = "King of Hearts"
                added_value = 10

        elif first_card_drawn == "king_diamond":
                first_card_drawn = "King of Diamonds"
                added_value = 10

        elif first_card_drawn == "king_club":
                first_card_drawn = "King of Clubs"
                added_value = 10

        elif first_card_drawn == "king_spade":
                first_card_drawn = "King of Spades"
                added_value = 10

        elif first_card_drawn == "ace_heart":
                first_card_drawn = "Ace of Hearts"

                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11
                

        elif first_card_drawn == "ace_diamond":
                first_card_drawn = "Ace of Diamonds"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        elif first_card_drawn == "ace_club":
                first_card_drawn = "Ace of Clubs"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        elif first_card_drawn == "ace_spade":
                first_card_drawn = "Ace of Spades"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        hand = hand + added_value


        # To determine the value of the second card drawn

        if second_card_drawn == "two_heart":
                second_card_drawn = "Two of Hearts"
                added_value = 2

        elif second_card_drawn == "two_diamond":
                second_card_drawn = "Two of Diamonds"
                added_value = 2

        elif second_card_drawn == "two_club":
                second_card_drawn = "Two of Clubs"
                added_value = 2

        elif second_card_drawn == "two_spade":
                second_card_drawn = "Two of Spades"
                added_value = 2

        elif second_card_drawn == "three_heart":
                second_card_drawn = "Three of Hearts"
                added_value = 3

        elif second_card_drawn == "three_diamond":
                second_card_drawn = "Three of Diamonds"
                added_value = 3

        elif second_card_drawn == "three_club":
                second_card_drawn = "Three of Clubs"
                added_value = 3

        elif second_card_drawn == "three_spade":
                second_card_drawn = "Three of Spades"
                added_value = 3

        elif second_card_drawn == "four_heart":
                second_card_drawn = "Four of Hearts"
                added_value = 4

        elif second_card_drawn == "four_diamond":
                second_card_drawn = "Four of Diamonds"
                added_value = 4

        elif second_card_drawn == "four_club":
                second_card_drawn = "Four of Clubs"
                added_value = 4

        elif second_card_drawn == "four_spade":
                second_card_drawn = "Four of Spades"
                added_value = 4

        elif second_card_drawn == "five_heart":
                second_card_drawn = "Five of Hearts"
                added_value = 5

        elif second_card_drawn == "five_diamond":
                second_card_drawn = "Five of Diamonds"
                added_value = 5

        elif second_card_drawn == "five_club":
                second_card_drawn = "Five of Clubs"
                added_value = 5

        elif second_card_drawn == "five_spade":
                second_card_drawn = "Five of Spades"
                added_value = 5

        elif second_card_drawn == "six_heart":
                second_card_drawn = "Six of Hearts"
                added_value = 6

        elif second_card_drawn == "six_diamond":
                second_card_drawn = "Six of Diamonds"
                added_value = 6

        elif second_card_drawn == "six_club":
                second_card_drawn = "Six of Clubs"
                added_value = 6

        elif second_card_drawn == "six_spade":
                second_card_drawn = "Six of Spades"
                added_value = 6

        elif second_card_drawn == "seven_heart":
                second_card_drawn = "Seven of Hearts"
                added_value = 7

        elif second_card_drawn == "seven_diamond":
                second_card_drawn = "Seven of Diamonds"
                added_value = 7

        elif second_card_drawn == "seven_club":
                second_card_drawn = "Seven of Clubs"
                added_value = 7

        elif second_card_drawn == "seven_spade":
                second_card_drawn = "Seven of Spades"
                added_value = 7

        elif second_card_drawn == "eight_heart":
                second_card_drawn = "Eight of Hearts"
                added_value = 8

        elif second_card_drawn == "eight_diamond":
                second_card_drawn = "Eight of Diamonds"
                added_value = 8

        elif second_card_drawn == "eight_club":
                second_card_drawn = "Eight of Clubs"
                added_value = 8

        elif second_card_drawn == "eight_spade":
                second_card_drawn = "Eight of Spades"
                added_value = 8

        elif second_card_drawn == "nine_heart":
                second_card_drawn = "Nine of Hearts"
                added_value = 9

        elif second_card_drawn == "nine_diamond":
                second_card_drawn = "Nine of Diamonds"
                added_value = 9

        elif second_card_drawn == "nine_club":
                second_card_drawn = "Nine of Clubs"
                added_value = 9

        elif second_card_drawn == "nine_spade":
                second_card_drawn = "Nine of Spades"
                added_value = 9

        elif second_card_drawn == "ten_heart":
                second_card_drawn = "Ten of Hearts"
                added_value = 10

        elif second_card_drawn == "ten_diamond":
                second_card_drawn = "Ten of Diamonds"
                added_value = 10

        elif second_card_drawn == "ten_club":
                second_card_drawn = "Ten of Clubs"
                added_value = 10

        elif second_card_drawn == "ten_spade":
                second_card_drawn = "Ten of Spades"
                added_value = 10

        elif second_card_drawn == "jack_heart":
                second_card_drawn = "Jack of Hearts"
                added_value = 10

        elif second_card_drawn == "jack_diamond":
                second_card_drawn = "Jack of Diamonds"
                added_value = 10

        elif second_card_drawn == "jack_club":
                second_card_drawn = "Jack of Clubs"
                added_value = 10

        elif second_card_drawn == "jack_spade":
                second_card_drawn = "Jack of Spades"
                added_value = 10

        elif second_card_drawn == "queen_heart":
                second_card_drawn = "Queen of Hearts"
                added_value = 10

        elif second_card_drawn == "queen_diamond":
                second_card_drawn = "Queen of Diamonds"
                added_value = 10

        elif second_card_drawn == "queen_club":
                second_card_drawn = "Queen of Clubs"
                added_value = 10

        elif second_card_drawn == "queen_spade":
                second_card_drawn = "Queen of Spades"
                added_value = 10

        elif second_card_drawn == "king_heart":
                second_card_drawn = "King of Hearts"
                added_value = 10

        elif second_card_drawn == "king_diamond":
                second_card_drawn = "King of Diamonds"
                added_value = 10

        elif second_card_drawn == "king_club":
                second_card_drawn = "King of Clubs"
                added_value = 10

        elif second_card_drawn == "king_spade":
                second_card_drawn = "King of Spades"
                added_value = 10

        elif second_card_drawn == "ace_heart":
                second_card_drawn = "Ace of Hearts"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        elif second_card_drawn == "ace_diamond":
                second_card_drawn = "Ace of Diamonds"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        elif second_card_drawn == "ace_club":
                second_card_drawn = "Ace of Clubs"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        elif second_card_drawn == "ace_spade":
                second_card_drawn = "Ace of Spades"
                
                print("\n")

                print ("Do you want your Ace to be worth 1 or 11?")
                print ("Type '1' for your Ace to be worth 1.")
                print ("Type anything else for your Ace to be worth 11.")

                ace_value = input()

                if ace_value == "1":
                        added_value = 1

                else:
                        added_value = 11


        hand = hand + added_value


        # To determine the value of the first card drawn by the dealer

        if first_card_drawn_dealer == "two_heart":
                first_card_drawn_dealer = "Two of Hearts"
                added_value_dealer = 2

        elif first_card_drawn_dealer == "two_diamond":
                first_card_drawn_dealer = "Two of Diamonds"
                added_value_dealer = 2

        elif first_card_drawn_dealer == "two_club":
                first_card_drawn_dealer = "Two of Clubs"
                added_value_dealer = 2

        elif first_card_drawn_dealer == "two_spade":
                first_card_drawn_dealer = "Two of Spades"
                added_value_dealer = 2

        elif first_card_drawn_dealer == "three_heart":
                first_card_drawn_dealer = "Three of Hearts"
                added_value_dealer = 3

        elif first_card_drawn_dealer == "three_diamond":
                first_card_drawn_dealer = "Three of Diamonds"
                added_value_dealer = 3

        elif first_card_drawn_dealer == "three_club":
                first_card_drawn_dealer = "Three of Clubs"
                added_value_dealer = 3

        elif first_card_drawn_dealer == "three_spade":
                first_card_drawn_dealer = "Three of Spades"
                added_value_dealer = 3

        elif first_card_drawn_dealer == "four_heart":
                first_card_drawn_dealer = "Four of Hearts"
                added_value_dealer = 4

        elif first_card_drawn_dealer == "four_diamond":
                first_card_drawn_dealer = "Four of Diamonds"
                added_value_dealer = 4

        elif first_card_drawn_dealer == "four_club":
                first_card_drawn_dealer = "Four of Clubs"
                added_value_dealer = 4

        elif first_card_drawn_dealer == "four_spade":
                first_card_drawn_dealer = "Four of Spades"
                added_value_dealer = 4

        elif first_card_drawn_dealer == "five_heart":
                first_card_drawn_dealer = "Five of Hearts"
                added_value_dealer = 5

        elif first_card_drawn_dealer == "five_diamond":
                first_card_drawn_dealer = "Five of Diamonds"
                added_value_dealer = 5

        elif first_card_drawn_dealer == "five_club":
                first_card_drawn_dealer = "Five of Clubs"
                added_value_dealer = 5

        elif first_card_drawn_dealer == "five_spade":
                first_card_drawn_dealer = "Five of Spades"
                added_value_dealer = 5

        elif first_card_drawn_dealer == "six_heart":
                first_card_drawn_dealer = "Six of Hearts"
                added_value_dealer = 6

        elif first_card_drawn_dealer == "six_diamond":
                first_card_drawn_dealer = "Six of Diamonds"
                added_value_dealer = 6

        elif first_card_drawn_dealer == "six_club":
                first_card_drawn_dealer = "Six of Clubs"
                added_value_dealer = 6

        elif first_card_drawn_dealer == "six_spade":
                first_card_drawn_dealer = "Six of Spades"
                added_value_dealer = 6

        elif first_card_drawn_dealer == "seven_heart":
                first_card_drawn_dealer = "Seven of Hearts"
                added_value_dealer = 7

        elif first_card_drawn_dealer == "seven_diamond":
                first_card_drawn_dealer = "Seven of Diamonds"
                added_value_dealer = 7

        elif first_card_drawn_dealer == "seven_club":
                first_card_drawn_dealer = "Seven of Clubs"
                added_value_dealer = 7

        elif first_card_drawn_dealer == "seven_spade":
                first_card_drawn_dealer = "Seven of Spades"
                added_value_dealer = 7

        elif first_card_drawn_dealer == "eight_heart":
                first_card_drawn_dealer = "Eight of Hearts"
                added_value_dealer = 8

        elif first_card_drawn_dealer == "eight_diamond":
                first_card_drawn_dealer = "Eight of Diamonds"
                added_value_dealer = 8

        elif first_card_drawn_dealer == "eight_club":
                first_card_drawn_dealer = "Eight of Clubs"
                added_value_dealer = 8

        elif first_card_drawn_dealer == "eight_spade":
                first_card_drawn_dealer = "Eight of Spades"
                added_value_dealer = 8

        elif first_card_drawn_dealer == "nine_heart":
                first_card_drawn_dealer = "Nine of Hearts"
                added_value_dealer = 9

        elif first_card_drawn_dealer == "nine_diamond":
                first_card_drawn_dealer = "Nine of Diamonds"
                added_value_dealer = 9

        elif first_card_drawn_dealer == "nine_club":
                first_card_drawn_dealer = "Nine of Clubs"
                added_value_dealer = 9

        elif first_card_drawn_dealer == "nine_spade":
                first_card_drawn_dealer = "Nine of Spades"
                added_value_dealer = 9

        elif first_card_drawn_dealer == "ten_heart":
                first_card_drawn_dealer = "Ten of Hearts"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "ten_diamond":
                first_card_drawn_dealer = "Ten of Diamonds"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "ten_club":
                first_card_drawn_dealer = "Ten of Clubs"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "ten_spade":
                first_card_drawn_dealer = "Ten of Spades"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "jack_heart":
                first_card_drawn_dealer = "Jack of Hearts"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "jack_diamond":
                first_card_drawn_dealer = "Jack of Diamonds"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "jack_club":
                first_card_drawn_dealer = "Jack of Clubs"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "jack_spade":
                first_card_drawn_dealer = "Jack of Spades"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "queen_heart":
                first_card_drawn_dealer = "Queen of Hearts"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "queen_diamond":
                first_card_drawn_dealer = "Queen of Diamonds"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "queen_club":
                first_card_drawn_dealer = "Queen of Clubs"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "queen_spade":
                first_card_drawn_dealer = "Queen of Spades"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "king_heart":
                first_card_drawn_dealer = "King of Hearts"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "king_diamond":
                first_card_drawn_dealer = "King of Diamonds"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "king_club":
                first_card_drawn_dealer = "King of Clubs"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "king_spade":
                first_card_drawn_dealer = "King of Spades"
                added_value_dealer = 10

        elif first_card_drawn_dealer == "ace_heart":
                first_card_drawn_dealer = "Ace of Hearts"
                added_value_dealer = 11
                

        elif first_card_drawn_dealer == "ace_diamond":
                first_card_drawn_dealer = "Ace of Diamonds"
                added_value_dealer = 11


        elif first_card_drawn_dealer == "ace_club":
                first_card_drawn_dealer = "Ace of Clubs"
                added_value_dealer = 11


        elif first_card_drawn_dealer == "ace_spade":
                first_card_drawn_dealer = "Ace of Spades"
                added_value_dealer = 11


        dealer_hand = dealer_hand + added_value_dealer


        # To determine the value of the second card drawn by the dealer

        if second_card_drawn_dealer == "two_heart":
                second_card_drawn_dealer = "Two of Hearts"
                added_value_dealer = 2

        elif second_card_drawn_dealer == "two_diamond":
                second_card_drawn_dealer = "Two of Diamonds"
                added_value_dealer = 2

        elif second_card_drawn_dealer == "two_club":
                second_card_drawn_dealer = "Two of Clubs"
                added_value_dealer = 2

        elif second_card_drawn_dealer == "two_spade":
                second_card_drawn_dealer = "Two of Spades"
                added_value_dealer = 2

        elif second_card_drawn_dealer == "three_heart":
                second_card_drawn_dealer = "Three of Hearts"
                added_value_dealer = 3

        elif second_card_drawn_dealer == "three_diamond":
                second_card_drawn_dealer = "Three of Diamonds"
                added_value_dealer = 3

        elif second_card_drawn_dealer == "three_club":
                second_card_drawn_dealer = "Three of Clubs"
                added_value_dealer = 3

        elif second_card_drawn_dealer == "three_spade":
                second_card_drawn_dealer = "Three of Spades"
                added_value_dealer = 3

        elif second_card_drawn_dealer == "four_heart":
                second_card_drawn_dealer = "Four of Hearts"
                added_value_dealer = 4

        elif second_card_drawn_dealer == "four_diamond":
                second_card_drawn_dealer = "Four of Diamonds"
                added_value_dealer = 4

        elif second_card_drawn_dealer == "four_club":
                second_card_drawn_dealer = "Four of Clubs"
                added_value_dealer = 4

        elif second_card_drawn_dealer == "four_spade":
                second_card_drawn_dealer = "Four of Spades"
                added_value_dealer = 4

        elif second_card_drawn_dealer == "five_heart":
                second_card_drawn_dealer = "Five of Hearts"
                added_value_dealer = 5

        elif second_card_drawn_dealer == "five_diamond":
                second_card_drawn_dealer = "Five of Diamonds"
                added_value_dealer = 5

        elif second_card_drawn_dealer == "five_club":
                second_card_drawn_dealer = "Five of Clubs"
                added_value_dealer = 5

        elif second_card_drawn_dealer == "five_spade":
                second_card_drawn_dealer = "Five of Spades"
                added_value_dealer = 5

        elif second_card_drawn_dealer == "six_heart":
                second_card_drawn_dealer = "Six of Hearts"
                added_value_dealer = 6

        elif second_card_drawn_dealer == "six_diamond":
                second_card_drawn_dealer = "Six of Diamonds"
                added_value_dealer = 6

        elif second_card_drawn_dealer == "six_club":
                second_card_drawn_dealer = "Six of Clubs"
                added_value_dealer = 6

        elif second_card_drawn_dealer == "six_spade":
                second_card_drawn_dealer = "Six of Spades"
                added_value_dealer = 6

        elif second_card_drawn_dealer == "seven_heart":
                second_card_drawn_dealer = "Seven of Hearts"
                added_value_dealer = 7

        elif second_card_drawn_dealer == "seven_diamond":
                second_card_drawn_dealer = "Seven of Diamonds"
                added_value_dealer = 7

        elif second_card_drawn_dealer == "seven_club":
                second_card_drawn_dealer = "Seven of Clubs"
                added_value_dealer = 7

        elif second_card_drawn_dealer == "seven_spade":
                second_card_drawn_dealer = "Seven of Spades"
                added_value_dealer = 7

        elif second_card_drawn_dealer == "eight_heart":
                second_card_drawn_dealer = "Eight of Hearts"
                added_value_dealer = 8

        elif second_card_drawn_dealer == "eight_diamond":
                second_card_drawn_dealer = "Eight of Diamonds"
                added_value_dealer = 8

        elif second_card_drawn_dealer == "eight_club":
                second_card_drawn_dealer = "Eight of Clubs"
                added_value_dealer = 8

        elif second_card_drawn_dealer == "eight_spade":
                second_card_drawn_dealer = "Eight of Spades"
                added_value_dealer = 8

        elif second_card_drawn_dealer == "nine_heart":
                second_card_drawn_dealer = "Nine of Hearts"
                added_value_dealer = 9

        elif second_card_drawn_dealer == "nine_diamond":
                second_card_drawn_dealer = "Nine of Diamonds"
                added_value_dealer = 9

        elif second_card_drawn_dealer == "nine_club":
                second_card_drawn_dealer = "Nine of Clubs"
                added_value_dealer = 9

        elif second_card_drawn_dealer == "nine_spade":
                second_card_drawn_dealer = "Nine of Spades"
                added_value_dealer = 9

        elif second_card_drawn_dealer == "ten_heart":
                second_card_drawn_dealer = "Ten of Hearts"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "ten_diamond":
                second_card_drawn_dealer = "Ten of Diamonds"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "ten_club":
                second_card_drawn_dealer = "Ten of Clubs"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "ten_spade":
                second_card_drawn_dealer = "Ten of Spades"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "jack_heart":
                second_card_drawn_dealer = "Jack of Hearts"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "jack_diamond":
                second_card_drawn_dealer = "Jack of Diamonds"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "jack_club":
                second_card_drawn_dealer = "Jack of Clubs"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "jack_spade":
                second_card_drawn_dealer = "Jack of Spades"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "queen_heart":
                second_card_drawn_dealer = "Queen of Hearts"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "queen_diamond":
                second_card_drawn_dealer = "Queen of Diamonds"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "queen_club":
                second_card_drawn_dealer = "Queen of Clubs"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "queen_spade":
                second_card_drawn_dealer = "Queen of Spades"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "king_heart":
                second_card_drawn_dealer = "King of Hearts"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "king_diamond":
                second_card_drawn_dealer = "King of Diamonds"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "king_club":
                second_card_drawn_dealer = "King of Clubs"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "king_spade":
                second_card_drawn_dealer = "King of Spades"
                added_value_dealer = 10

        elif second_card_drawn_dealer == "ace_heart":

                second_card_drawn_dealer = "Ace of Hearts"

                if dealer_hand <= 10:
                        added_value_dealer = 11
                else:
                        added_value_dealer = 1
                

        elif second_card_drawn_dealer == "ace_diamond":

                second_card_drawn_dealer = "Ace of Diamonds"

                if dealer_hand <= 10:
                        added_value_dealer = 11
                else:
                        added_value_dealer = 1


        elif second_card_drawn_dealer == "ace_club":

                second_card_drawn_dealer = "Ace of Clubs"

                if dealer_hand <= 10:
                        added_value_dealer = 11
                else:
                        added_value_dealer = 1
   

        elif second_card_drawn_dealer == "ace_spade":

                second_card_drawn_dealer = "Ace of Spades"

                if dealer_hand <= 10:
                        added_value_dealer = 11
                else:
                        added_value_dealer = 1


        dealer_hand = dealer_hand + added_value_dealer
        

        # Prints the names of the first two cards drawn by the player.
        os.system('cls' if os.name == 'nt' else 'clear')

        print ("The dealer deals you a",first_card_drawn,"and a",second_card_drawn,".")

        print("\n")


        # If player get's a Blackjack

        if ( (first_card_drawn == "Ace of Hearts" or first_card_drawn == "Ace of Diamonds" or first_card_drawn == "Ace of Clubs" or first_card_drawn == "Ace of Spades") and (second_card_drawn == "Ten of Hearts" or second_card_drawn == "Ten of Diamonds" or second_card_drawn == "Ten of Clubs" or second_card_drawn == "Ten of Spades" or second_card_drawn == "Jack of Hearts" or second_card_drawn == "Jack of Diamonds" or second_card_drawn == "Jack of Clubs" or second_card_drawn == "Jack of Spades" or second_card_drawn == "Queen of Hearts" or second_card_drawn == "Queen of Diamonds" or second_card_drawn == "Queen of Clubs" or second_card_drawn == "Queen of Spades" or second_card_drawn == "King of Hearts" or second_card_drawn == "King of Diamonds" or second_card_drawn == "King of Clubs" or second_card_drawn == "King of Spades") ) or ( (first_card_drawn == "Ten of Hearts" or first_card_drawn == "Ten of Diamonds" or first_card_drawn == "Ten of Clubs" or first_card_drawn == "Ten of Spades" or first_card_drawn == "Jack of Hearts" or first_card_drawn == "Jack of Diamonds" or first_card_drawn == "Jack of Clubs" or first_card_drawn == "Jack of Spades" or first_card_drawn == "Queen of Hearts" or first_card_drawn == "Queen of Diamonds" or first_card_drawn == "Queen of Clubs" or first_card_drawn == "Queen of Spades" or first_card_drawn == "King of Hearts" or first_card_drawn == "King of Diamonds" or first_card_drawn == "King of Clubs" or first_card_drawn == "King of Spades") and (second_card_drawn == "Ace of Hearts" or second_card_drawn == "Ace of Diamonds" or second_card_drawn == "Ace of Clubs" or second_card_drawn == "Ace of Spades") ):
                
                print ("That's a Blackjack!")

                print("\n")
                print ("You Win!")
                print("\n")

                print ("Would you like to play again?")
                print ("Type 'yes' play again?")
                print ("Type anything else to exit.")

                yes_no = input ()

                if yes_no == "yes":
                        start_game ()
                else:
                        print("\n")
                        print ("Have a nice day!")
                        print ("\n")

                        exit()


        # Prints the value of the player's hand

        print ("The total value of your cards is:")
        print (hand)


        # Prints the name of the first card drawn by the dealer.

        print("\n")

        print ("The dealer draws a",first_card_drawn_dealer,"and another card that is hidden.")




        # Player chooses wether to 'hit' or 'stand'

        while hand < 21:
                
                print("\n")

                print ("Press 'h' to hit or press 's' to stand.")

                h_s = input()

                print("\n")

                # If player 'hits'

                if h_s == "h":
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n")

                        print ("hit!")

                        print("\n")

                        chosen_card = random.choice(deck)

                        deck.remove(chosen_card)


                        if chosen_card == "two_heart":
                                print ("Two of Hearts")
                                added_value = 2

                        elif chosen_card == "two_diamond":
                                print ("Two of Diamonds")
                                added_value = 2

                        elif chosen_card == "two_club":
                                print ("Two of Clubs")
                                added_value = 2

                        elif chosen_card == "two_spade":
                                print ("Two of Spades")
                                added_value = 2

                        elif chosen_card == "three_heart":
                                print ("Three of Hearts")
                                added_value = 3

                        elif chosen_card == "three_diamond":
                                print ("Three of Diamonds")
                                added_value = 3

                        elif chosen_card == "three_club":
                                print ("Three of Clubs")
                                added_value = 3

                        elif chosen_card == "three_spade":
                                print ("Three of Spades")
                                added_value = 3

                        elif chosen_card == "four_heart":
                                print ("Four of Hearts")
                                added_value = 4

                        elif chosen_card == "four_diamond":
                                print ("Four of Diamonds")
                                added_value = 4

                        elif chosen_card == "four_club":
                                print ("Four of Clubs")
                                added_value = 4

                        elif chosen_card == "four_spade":
                                print ("Four of Spades")
                                added_value = 4

                        elif chosen_card == "five_heart":
                                print ("Five of Hearts")
                                added_value = 5

                        elif chosen_card == "five_diamond":
                                print ("Five of Diamonds")
                                added_value = 5

                        elif chosen_card == "five_club":
                                print ("Five of Clubs")
                                added_value = 5

                        elif chosen_card == "five_spade":
                                print ("Five of Spades")
                                added_value = 5

                        elif chosen_card == "six_heart":
                                print ("Six of Hearts")
                                added_value = 6

                        elif chosen_card == "six_diamond":
                                print ("Six of Diamonds")
                                added_value = 6

                        elif chosen_card == "six_club":
                                print ("Six of Clubs")
                                added_value = 6

                        elif chosen_card == "six_spade":
                                print ("Six of Spades")
                                added_value = 6

                        elif chosen_card == "seven_heart":
                                print ("Seven of Hearts")
                                added_value = 7

                        elif chosen_card == "seven_diamond":
                                print ("Seven of Diamonds")
                                added_value = 7

                        elif chosen_card == "seven_club":
                                print ("Seven of Clubs")
                                added_value = 7

                        elif chosen_card == "seven_spade":
                                print ("Seven of Spades")
                                added_value = 7

                        elif chosen_card == "eight_heart":
                                print ("Eight of Hearts")
                                added_value = 8

                        elif chosen_card == "eight_diamond":
                                print ("Eight of Diamonds")
                                added_value = 8

                        elif chosen_card == "eight_club":
                                print ("Eight of Clubs")
                                added_value = 8

                        elif chosen_card == "eight_spade":
                                print ("Eight of Spades")
                                added_value = 8

                        elif chosen_card == "nine_heart":
                                print ("Nine of Hearts")
                                added_value = 9

                        elif chosen_card == "nine_diamond":
                                print ("Nine of Diamonds")
                                added_value = 9

                        elif chosen_card == "nine_club":
                                print ("Nine of Clubs")
                                added_value = 9

                        elif chosen_card == "nine_spade":
                                print ("Nine of Spades")
                                added_value = 9

                        elif chosen_card == "ten_heart":
                                print ("Ten of Hearts")
                                added_value = 10

                        elif chosen_card == "ten_diamond":
                                print ("Ten of Diamonds")
                                added_value = 10

                        elif chosen_card == "ten_club":
                                print ("Ten of Clubs")
                                added_value = 10

                        elif chosen_card == "ten_spade":
                                print ("Ten of Spades")
                                added_value = 10

                        elif chosen_card == "jack_heart":
                                print ("Jack of Hearts")
                                added_value = 10

                        elif chosen_card == "jack_diamond":
                                print ("Jack of Diamonds")
                                added_value = 10

                        elif chosen_card == "jack_club":
                                print ("Jack of Clubs")
                                added_value = 10

                        elif chosen_card == "jack_spade":
                                print ("Jack of Spades")
                                added_value = 10

                        elif chosen_card == "queen_heart":
                                print ("Queen of Hearts")
                                added_value = 10

                        elif chosen_card == "queen_diamond":
                                print ("Queen of Diamonds")
                                added_value = 10

                        elif chosen_card == "queen_club":
                                print ("Queen of Clubs")
                                added_value = 10

                        elif chosen_card == "queen_spade":
                                print ("Queen of Spades")
                                added_value = 10

                        elif chosen_card == "king_heart":
                                print ("King of Hearts")
                                added_value = 10

                        elif chosen_card == "king_diamond":
                                print ("King of Diamonds")
                                added_value = 10

                        elif chosen_card == "king_club":
                                print ("King of Clubs")
                                added_value = 10

                        elif chosen_card == "king_spade":
                                print ("King of Spades")
                                added_value = 10

                        elif chosen_card == "ace_heart":
                                print ("Ace of Hearts")
                                
                                print("\n")

                                print ("Do you want your Ace to be worth 1 or 11?")
                                print ("Type '1' for your Ace to be worth 1.")
                                print ("Type anything else for your Ace to be worth 11.")

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                else:
                                        added_value = 11


                        elif chosen_card == "ace_diamond":
                                print ("Ace of Diamonds")
                                
                                print("\n")

                                print ("Do you want your Ace to be worth 1 or 11?")
                                print ("Type '1' for your Ace to be worth 1.")
                                print ("Type anything else for your Ace to be worth 11.")

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                else:
                                        added_value = 11


                        elif chosen_card == "ace_club":
                                print ("Ace of Clubs")
                                
                                print("\n")

                                print ("Do you want your Ace to be worth 1 or 11?")
                                print ("Type '1' for your Ace to be worth 1.")
                                print ("Type anything else for your Ace to be worth 11.")

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                else:
                                        added_value = 11


                        elif chosen_card == "ace_spade":
                                print ("Ace of Spades")
                                
                                print("\n")

                                print ("Do you want your Ace to be worth 1 or 11?")
                                print ("Type '1' for your Ace to be worth 1.")
                                print ("Type anything else for your Ace to be worth 11.")

                                ace_value = input()

                                if ace_value == "1":
                                        added_value = 1

                                else:
                                        added_value = 11


                        # This should not happen, but if it does, it means that something went wrong and there was an error

                        else:
                                print ("Something went wrong.")

                # If player 'stands'

                elif h_s == "s":
                        os.system('cls' if os.name == 'nt' else 'clear')


                        print("\n")
                        print ("stand!")
                        print("\n")


                        print ("The dealer reveals their second card.")
                        print("\n")
                        print (f"It's a {second_card_drawn_dealer}.")
                        print("\n")
                        print (f"The dealer has a {first_card_drawn_dealer} and a {second_card_drawn_dealer}.")
                        print("\n")
                        print (f"The total value of their hand is {dealer_hand}.")
                        print ("\n")
                        print (f"The total value of your hand is {hand}.")
                        print ("\n")

                        
                        # Dealer hits if necessary.

                        if dealer_hand < 17:
                                print ("The dealer must keep hitting until they reach a total hand value of 17 or more.")
                                print("\n")

                                
                                while dealer_hand < 17:
                                        print ("Press ENTER to continue.")
                                        input ()
                                        print("\n")

                                        os.system('cls' if os.name == 'nt' else 'clear')

                                        print("\n")
                                        print ("hit!")
                                        print("\n")

                                        chosen_card_dealer = random.choice(deck)

                                        deck.remove(chosen_card_dealer)


                                        if chosen_card_dealer == "two_heart":
                                                chosen_card_dealer = "Two of Hearts"
                                                added_value_dealer = 2

                                        elif chosen_card_dealer == "two_diamond":
                                                chosen_card_dealer = "Two of Diamonds"
                                                added_value_dealer = 2

                                        elif chosen_card_dealer == "two_club":
                                                chosen_card_dealer = "Two of Clubs"
                                                added_value_dealer = 2

                                        elif chosen_card_dealer == "two_spade":
                                                chosen_card_dealer = "Two of Spades"
                                                added_value_dealer = 2

                                        elif chosen_card_dealer == "three_heart":
                                                chosen_card_dealer = "Three of Hearts"
                                                added_value_dealer = 3

                                        elif chosen_card_dealer == "three_diamond":
                                                chosen_card_dealer = "Three of Diamonds"
                                                added_value_dealer = 3

                                        elif chosen_card_dealer == "three_club":
                                                chosen_card_dealer = "Three of Clubs"
                                                added_value_dealer = 3

                                        elif chosen_card_dealer == "three_spade":
                                                chosen_card_dealer = "Three of Spades"
                                                added_value_dealer = 3

                                        elif chosen_card_dealer == "four_heart":
                                                chosen_card_dealer = "Four of Hearts"
                                                added_value_dealer = 4

                                        elif chosen_card_dealer == "four_diamond":
                                                chosen_card_dealer = "Four of Diamonds"
                                                added_value_dealer = 4

                                        elif chosen_card_dealer == "four_club":
                                                chosen_card_dealer = "Four of Clubs"
                                                added_value_dealer = 4

                                        elif chosen_card_dealer == "four_spade":
                                                chosen_card_dealer = "Four of Spades"
                                                added_value_dealer = 4

                                        elif chosen_card_dealer == "five_heart":
                                                chosen_card_dealer = "Five of Hearts"
                                                added_value_dealer = 5

                                        elif chosen_card_dealer == "five_diamond":
                                                chosen_card_dealer = "Five of Diamonds"
                                                added_value_dealer = 5

                                        elif chosen_card_dealer == "five_club":
                                                chosen_card_dealer = "Five of Clubs"
                                                added_value_dealer = 5

                                        elif chosen_card_dealer == "five_spade":
                                                chosen_card_dealer = "Five of Spades"
                                                added_value_dealer = 5

                                        elif chosen_card_dealer == "six_heart":
                                                chosen_card_dealer = "Six of Hearts"
                                                added_value_dealer = 6

                                        elif chosen_card_dealer == "six_diamond":
                                                chosen_card_dealer = "Six of Diamonds"
                                                added_value_dealer = 6

                                        elif chosen_card_dealer == "six_club":
                                                chosen_card_dealer = "Six of Clubs"
                                                added_value_dealer = 6

                                        elif chosen_card_dealer == "six_spade":
                                                chosen_card_dealer = "Six of Spades"
                                                added_value_dealer = 6

                                        elif chosen_card_dealer == "seven_heart":
                                                chosen_card_dealer = "Seven of Hearts"
                                                added_value_dealer = 7

                                        elif chosen_card_dealer == "seven_diamond":
                                                chosen_card_dealer = "Seven of Diamonds"
                                                added_value_dealer = 7

                                        elif chosen_card_dealer == "seven_club":
                                                chosen_card_dealer = "Seven of Clubs"
                                                added_value_dealer = 7

                                        elif chosen_card_dealer == "seven_spade":
                                                chosen_card_dealer = "Seven of Spades"
                                                added_value_dealer = 7

                                        elif chosen_card_dealer == "eight_heart":
                                                chosen_card_dealer = "Eight of Hearts"
                                                added_value_dealer = 8

                                        elif chosen_card_dealer == "eight_diamond":
                                                chosen_card_dealer = "Eight of Diamonds"
                                                added_value_dealer = 8

                                        elif chosen_card_dealer == "eight_club":
                                                chosen_card_dealer = "Eight of Clubs"
                                                added_value_dealer = 8

                                        elif chosen_card_dealer == "eight_spade":
                                                chosen_card_dealer = "Eight of Spades"
                                                added_value_dealer = 8

                                        elif chosen_card_dealer == "nine_heart":
                                                chosen_card_dealer = "Nine of Hearts"
                                                added_value_dealer = 9

                                        elif chosen_card_dealer == "nine_diamond":
                                                chosen_card_dealer = "Nine of Diamonds"
                                                added_value_dealer = 9

                                        elif chosen_card_dealer == "nine_club":
                                                chosen_card_dealer = "Nine of Clubs"
                                                added_value_dealer = 9

                                        elif chosen_card_dealer == "nine_spade":
                                                chosen_card_dealer = "Nine of Spades"
                                                added_value_dealer = 9

                                        elif chosen_card_dealer == "ten_heart":
                                                chosen_card_dealer = "Ten of Hearts"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "ten_diamond":
                                                chosen_card_dealer = "Ten of Diamonds"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "ten_club":
                                                chosen_card_dealer = "Ten of Clubs"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "ten_spade":
                                                chosen_card_dealer = "Ten of Spades"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "jack_heart":
                                                chosen_card_dealer = "Jack of Hearts"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "jack_diamond":
                                                chosen_card_dealer = "Jack of Diamonds"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "jack_club":
                                                chosen_card_dealer = "Jack of Clubs"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "jack_spade":
                                                chosen_card_dealer = "Jack of Spades"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "queen_heart":
                                                chosen_card_dealer = "Queen of Hearts"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "queen_diamond":
                                                chosen_card_dealer = "Queen of Diamonds"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "queen_club":
                                                chosen_card_dealer = "Queen of Clubs"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "queen_spade":
                                                chosen_card_dealer = "Queen of Spades"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "king_heart":
                                                chosen_card_dealer = "King of Hearts"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "king_diamond":
                                                chosen_card_dealer = "King of Diamonds"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "king_club":
                                                chosen_card_dealer = "King of Clubs"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "king_spade":
                                                chosen_card_dealer = "King of Spades"
                                                added_value_dealer = 10

                                        elif chosen_card_dealer == "ace_heart":

                                                chosen_card_dealer = "Ace of Hearts"

                                                if dealer_hand <= 10:
                                                        added_value_dealer = 11
                                                else:
                                                        added_value_dealer = 1
                                                

                                        elif chosen_card_dealer == "ace_diamond":

                                                chosen_card_dealer = "Ace of Diamonds"

                                                if dealer_hand <= 10:
                                                        added_value_dealer = 11
                                                else:
                                                        added_value_dealer = 1


                                        elif chosen_card_dealer == "ace_club":

                                                chosen_card_dealer = "Ace of Clubs"

                                                if dealer_hand <= 10:
                                                        added_value_dealer = 11
                                                else:
                                                        added_value_dealer = 1
                                

                                        elif chosen_card_dealer == "ace_spade":

                                                chosen_card_dealer = "Ace of Spades"

                                                if dealer_hand <= 10:
                                                        added_value_dealer = 11
                                                else:
                                                        added_value_dealer = 1


                                        print (chosen_card_dealer)
                                        print ("\n")


                                        # To calculate the value of the dealer's hand

                                        dealer_hand = dealer_hand + added_value_dealer

                                        print (f"The total value of the dealer's hand is {dealer_hand}.")
                                        print ("\n")

                        

                        # To determine who wins.

                        if dealer_hand == 21:
                                print("\n")
                                print ("You lose!")
                        elif dealer_hand > 21:
                                print ("\n")
                                print ("You win!")
                        else:
                                if hand > dealer_hand:
                                        print ("You win!")
                                elif hand < dealer_hand:
                                        print ("You lose!")
                                else:
                                        print ("It's a tie.")

                                
                        # To ask the player if they want to play again.

                        print ("\n")
                        print ("Would you like to play again?")
                        print ("Type 'yes' play again?")
                        print ("Type anything else to exit.")

                        yes_no = input ()

                        if yes_no == "yes":
                                start_game ()
                        else:
                                print("\n")
                                print ("Have a nice day!")
                                print ("\n")

                                exit()


                # If player hits something else

                else:
                        print ("You should've pressed 'h' or 's'.")
                        print("\n")
                        exit()


                # Calculates value of player's hand

                hand = hand + added_value

                print("\n")

                print ("The total value of your cards is:")
                print (hand)


        # If player's hand exceeds 20.

        if hand == 21:
                print("\n")
                print ("You Win!")
        else:
                print("\n")
                print ("You Lose!")


        # To ask the player if they want to play again.
        
        print ("\n")
        print ("Would you like to play again?")
        print ("Type 'yes' play again?")
        print ("Type anything else to exit.")

        yes_no = input ()

        if yes_no == "yes":
                start_game ()
        else:
                print("\n")
                print ("Have a nice day!")
                print ("\n")

                exit()


# Game ends here





# Rules start here

def show_rules():
        print("\n")

        print ("The goal of BlackJack is to get as close to 21 as possible without going over it.")
        print ("Cards 2 through 10 are worth their face value, royal cards are each worth 10 and Aces can either be worth 1 or 11 based on the player's choosing.")
        print ("Note: Jokers are not present in this game.")
        print ("You start the game with 2 cards and the dealer also starts with 2 cards but you can only see one of their cards.")
        print ("If the first two cards you are given are an Ace and a card with a value of 10, that's a Blackjack.")
        print ("If you have a Blackjack and the dealer doesn't also have a Blackjack, then you automatically win.")
        print ("If there are no Blackjacks or you and the dealer both have Blackjacks, then the game continues like normal.")
        print ("As the player, you always start and you can either 'hit' or 'stand'.")
        print ("When you 'hit', you will receive a random card from the deck of 52 cards.")
        print ("You can 'hit' as many times as you want and you have to add up the value of all your cards.")
        print ("However, the combined value of your cards cannot exceed 21 or else you automatically lose.")
        print ("If you deem that the value of all your cards is high enough and it's too risky to 'hit', you can 'stand'.")
        print ("Once you 'stand', you will no longer pick up any cards.")
        print ("The dealer must then 'hit' until they have a combined card value of 17 or higher, after that they can no longer 'hit'.")
        print ("You will then compare your cards with that of the dealer.")
        print ("Whoever's cards have a combined value closest to 21, without exceeding it, wins.")
        print ("If the value of your cards, and that of the dealer are the same, then it's a draw.")
        print ("If both you, as the player, and the dealer bust, then you, as the player, lose.")

        print("\n")

        print("Type 'play' when you are ready to play or type 'exit' to exit the program.")


        def exit_rules():
                type_play = input()

                if type_play == "play":
                        start_game()
                elif type_play == "exit":
                        print("\n")
                        print ("Have a good day!")
                        print("\n")

                        exit()
                else:
                        print("\n")
                        print("Please type 'play' or 'exit'.")

                        exit_rules()

        
        x = exit_rules()

        

# Rules end here


def choose_play_rules_exit ():

        play_rules_exit = input ()


        if play_rules_exit == "play":
                start_game()

        elif play_rules_exit == "rules":
                show_rules()

        elif play_rules_exit == "exit":
                print("\n")

                print ("Have a nice day!")

                print("\n")

                exit()

        else:
                print("\n")

                print ("Please type 'play', 'rules', or 'exit'.")

                choose_play_rules_exit()
        
        print("\n")


y = choose_play_rules_exit ()