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
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    deck = []
    for suit in suits:
        temp = []
        for rank in ranks:
            temp.append(rank + suit)
        deck.append(temp)
    print(deck)
    return deck


def get_random_card_to_play(hand):
    return random.choice(hand)


def is_lead_suit_exists(my_hand, first_card_of_trick: str):
    return any(first_card_of_trick[1] in card[1] for card in my_hand)


def get_card_to_play_last(trick, hand):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    suit_in_play = trick[0][1]
    highest_rank_in_play = "2"
    for card in trick:
        if ranks.index(card[0]) > ranks.index(highest_rank_in_play):
            highest_rank_in_play = card[0]
    cards_can_be_played = hand[suit_in_play]
    rank_cards_to_be_played = [ranks.index(card[0]) for card in cards_can_be_played]

    if len(cards_can_be_played) > 0:
        higher_rank_cards_to_be_played = [card_rank for card_rank in rank_cards_to_be_played if
                                          card_rank > ranks.index(highest_rank_in_play)]
        if len(higher_rank_cards_to_be_played) > 0:
            return ranks[min(higher_rank_cards_to_be_played)] + suit_in_play
        else:
            return ranks[min(rank_cards_to_be_played)] + suit_in_play
    else:
        remaining_non_suit_cards = [v for v_arr in hand.values() for v in v_arr]
        min_rank = min([ranks.index(card[0]) for card in remaining_non_suit_cards])
        likely_cards = [card for card in remaining_non_suit_cards if ranks.index(card[0]) == min_rank]
        random.shuffle(likely_cards)
        return likely_cards[0]


def get_card_to_play_first(my_hand, state):
    weights = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ["H", "S", "C", "D"]
    def sort_cards():
        sorted_cards = []
        # sort all the cards according to weights not suits
        for suit in suits:
            new_suit_cards = []
            for weight in weights:
                for card in my_hand:
                    if card[0] == weight and card[1] == suit:
                        new_suit_cards.append(card)
            sorted_cards.append(new_suit_cards)
        return sorted_cards

    def get_bigger_card(card, state):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suit = card[1]
        suit_cards = state[suit]
        card_index = ranks.index(card[0])
        for index in range(card_index+1, len(ranks)-1):
            crd = ranks[index]
            if crd in suit_cards:
                crd = crd + suit
                return crd
        return None

    # sort cards suit wise and rank wise
    # e.g. sorted_cards = [['AS', 'KS', '8S'], ['7H', '4H'], ['8D', '5D', '3D'], ['4C', '2C']]
    sorted_cards = sort_cards()
    # Select the card to play from sorted list
    for suit in sorted_cards:
        card = suit[0]
        bigger_card = get_bigger_card(card, state)
        if not bigger_card:
            return card

    suit_lengths = [len(suit) for suit in sorted_cards]
    max_length_suit = max(suit_lengths)
    max_length_suit_index = suit_lengths.index(max_length_suit)
    return sorted_cards[max_length_suit_index][max_length_suit-1]


def get_card_to_play(trick, my_hand, state):
    hand = dict()

    for x in my_hand:
        suit = x[1]
        if suit in hand.keys():
            hand[suit].append([x])
        else:
            hand[suit] = [x]

    if len(trick) == 0:
        pass

    elif len(trick) == 1 or len(trick) == 2:
        first_card = trick[0]
        first_suit = first_card[1]

        if first_suit == 'S':
            pass
        elif first_suit == 'H':
            pass
        elif first_suit == 'C':
            pass
        elif first_suit == 'D':
            pass

    elif len(trick) == 3:
        get_card_to_play_last(trick, hand)


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
