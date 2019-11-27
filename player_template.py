"""
Team Name: Devil's Den
Team members:
Harshil Dhariwal
Aarsh Oza
Dhaval Patel
Kaustubh Dhokte
"""

import random


def get_new_deck():
    suits = ["H", "S", "C", "D"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        temp =[]
        for rank in ranks:
            temp.append(rank + suit)
        deck.append(temp)
    print(deck)
    return deck


def get_random_card_to_play(hand):
    return random.choice(hand)


def is_lead_suit_exists(my_hand, first_card_of_trick: str):
    return any(first_card_of_trick[1] in card[1] for card in my_hand)


def get_card_to_play_last(trick, my_hand, state):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suit_in_play = trick[0][1]
    highest_rank_in_play = "2"
    for card in trick:
        if ranks.index(card[0]) > ranks.index(highest_rank_in_play):
            highest_rank_in_play = card[0]
    

def get_card_to_play(trick, my_hand, state):
    if len(trick) == 0:
        pass
    elif len(trick) == 1 or len(trick) == 2:
        pass
    elif len(trick) == 3:
        get_card_to_play_last(trick, my_hand, state)


class Player(object):
    agent_name = 'DEVIL'
    my_hand = []
    player_names = []
    played_cards = []
    point = dict()
    state = []
    heart = 0
    spades = 1
    club = 2
    diamond = 3

    def __init__(self):
        pass

    def get_name(self):
        """
        Returns a string of the agent's name
        """
        return self.agent_name

    def get_hand(self):
        """
        Returns a list of two character strings reprsenting cards in the agent's hand
        """
        return self.my_hand

    def new_hand(self, names):
        """
        Takes a list of names of all agents in the game in clockwise playing order
        and returns nothing. This method is also responsible for clearing any data
        necessary for your agent to start a new round.
        """
        self.player_names = names
        for name in names:
            self.point[name] = 0
        self.state = get_new_deck()
        self.my_hand = []

    def add_cards_to_hand(self, cards):
        """
        Takes a list of two character strings representing cards as an argument
        and returns nothing.
        This list can be any length.
        """
        self.my_hand = self.my_hand + cards

    def play_card(self, lead, trick):
        """
        Takes a a string of the name of the player who lead the trick and
        a list of cards in the trick so far as arguments.

        Returns a two character string from the agents hand of the card to be played
        into the trick.
        """

        card_to_play = get_card_to_play(trick, self.my_hand, self.state)
        self.my_hand.remove(card_to_play)
        return card_to_play

    def collect_trick(self, lead, winner, trick):
        """
        Takes three arguements. Lead is the name of the player who led the trick.
        Winner is the name of the player who won the trick. And trick is a four card
        list of the trick that was played. Should return nothing.
        """

        self.played_cards = self.played_cards + trick
        self.point[winner] = self.point[winner] + 1
        print("Scores after the round", self.point)

        pass

    def score(self):
        """
        Calculates and returns the score for the game being played.
        """
        pass
