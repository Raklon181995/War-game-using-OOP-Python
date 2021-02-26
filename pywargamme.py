# Create War game using OOP
# Due 24 January 2021 23:59
# Instructions
# You need to use OOP concepts to create a war game between yourself and computer, here are basic rules of the game:

# The cards are divided equally in two players 26 each with face down.

# The Play:


# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.

#  If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
# https://en.wikipedia.org/wiki/War_(card_game)

# from random import shuffle

# # Two useful variables for creating Cards.
# SUITE = 'H D S C'.split()
# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# class Deck:
#     This is the Deck Class. This object will create a deck of cards to initiate
#     play. You can then use this Deck list of cards to split in half and give to
#     the players. It will use SUITE and RANKS to create the deck. It should also
#     have a method for splitting/cutting the deck in half and Shuffling the deck.

# class Hand:
#     This is the Hand class. Each player has a Hand, and can add or remove
#     cards from that hand. There should be an add and remove card method here.

# class Player:
#     This is the Player class, which takes in a name and an instance of a Hand
#     class object. The Payer can then play cards and check if they still have cards.
# Student work

from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print("Create an ordered deck")
        self.all_cards = [(su, rank) for su in suite for rank in ranks]
        # print(self.all_cards)

    def shuffle(self):
        print("To shuffle a Deck")
        shuffle(self.all_cards)

    def devide_into_half(self):
        print("splitting into two equal part")
        return (self.all_cards[0:26], self.all_cards[26:])

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def remove_a_card(self):
        return self.cards.pop()

    def add_cards(self, added_cards):
        self.cards.extend(added_cards)

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        draw_card = self.hand.remove_a_card()
        print(self.name , "has placed card ", draw_card)
        return draw_card

    def remove_war_card(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for card in range(3):
                war_cards.append(self.hand.cards.pop())

            return war_cards

    def check_cards_in_hand(self):
        flag = len(self.hand.cards)!= 0
        return flag


deck = Deck()
deck.shuffle()
player1_cards, player2_cards = deck.devide_into_half()
print(player1_cards, player2_cards)

computer = Player("My Computer",Hand(player1_cards) )
user = Player("Rakesh", Hand(player2_cards) )


rounds = 0
war_count = 0

while computer.check_cards_in_hand() and user.check_cards_in_hand():

    print("New round started: ")
    rounds = rounds+1
    print("Remaining Card: ")
    print(computer.name , "Has cards: ", computer.hand.cards)
    print(user.name , "Has cards: ", user.hand.cards)

    table_cards = [] 

    computer_card = computer.play_card()
    user_card = user.play_card()

    table_cards.append(computer_card)
    table_cards.append(user_card)

    if computer_card[1] == user_card[1]:
        print("Started a war:")
        war_count = war_count+1
        
        table_cards.extend(computer.remove_war_card())
        table_cards.extend(user.remove_war_card())

        computer_card = computer.play_card()
        user_card = user.play_card()

        table_cards.append(computer_card)
        table_cards.append(user_card)

        if ranks.index(computer_card[1]) < ranks.index(user_card[1]):
            print(user.name, "has the highest card")

            user.hand.add_cards(table_cards)
        else:
            computer.hand.add_cards(table_cards)

    else:
        if ranks.index(computer_card[1]) < ranks.index(user_card[1]):
            print(user.name, "has the highest card")

            user.hand.add_cards(table_cards)
        else:
            print(user.name, "has the highest card")

            computer.hand.add_cards(table_cards)

    print("==========================================")

print("Total rounds", rounds)
print("War count", war_count)
print("computer_cards", computer.hand.cards)
print("user_cards", user.hand.cards)



