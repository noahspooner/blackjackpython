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

        added_value = 0


        print("\n")


        # First two cards drawn

        first_card_drawn = random.choice(deck)

        second_card_drawn = random.choice(deck)

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
        

        os.system('cls' if os.name == 'nt' else 'clear')

        print ("The dealer deals you a",first_card_drawn,"and a",second_card_drawn,".")

        print("\n")

        print ("The total value of your cards is:")
        print (hand)




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


        if hand == 21:
                print("\n")
                print ("You Win!")
        else:
                print("\n")
                print ("You Lose!")

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