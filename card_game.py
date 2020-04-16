# This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
import time

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    def __init__(self):
        print("A new ordered deck is created.")
        self.all_cards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling all cards in the deck")
        shuffle(self.all_cards)

    def split_half(self):
        return (self.all_cards[:26],self.all_cards[26:])

class Hand():
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    def add(self,added_cards):
        self.cards.extend(added_cards)
    def remove_card(self):
        return self.cards.pop()

class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}\n".format(self.name, drawn_card))
        return drawn_card
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        '''
        This will return true if player still has cards.
        '''
        return len(self.hand.cards) != 0

# Create a new deck and split in split_half
d = Deck()
d.shuffle()
half1, half2 = d.split_half()

# Create both players
comp = Player('Computer',Hand(half1))
name = input('What is your name?\n')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

# Game logic
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name+" has the count: "+ str(len(user.hand.cards)))
    print(comp.name+" has the count: "+ str(len(comp.hand.cards)))
    print('Play a card')
    #print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:  # index 0 is suite, index 1 is ranking
        war_count += 1
        print("War")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)



print("Game Over!, Number of rounds: "+str(total_rounds))
print("A war happened "+str(war_count)+" times")
print("The computer still has cards? "+str(comp.still_has_cards()))
print("The user still has cards "+str(user.still_has_cards()))
