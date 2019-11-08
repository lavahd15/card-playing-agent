import random


class Player(object):
    agent_name = 'DEVIL'
    my_hand = []
    player_names = []
    played_cards = []
    point = dict()

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
        pass

    def add_cards_to_hand(self, cards):
        """
        Takes a list of two character strings representing cards as an argument
        and returns nothing.
        This list can be any length.
        """
        self.my_hand = self.my_hand + cards
        print(self.agent_name, len(self.my_hand), self.my_hand)

        pass

    def play_card(self, lead, trick):
        """
        Takes a a string of the name of the player who lead the trick and
        a list of cards in the trick so far as arguments.

        Returns a two character string from the agents hand of the card to be played
        into the trick.
        """
        if len(trick) == 0 and lead == self.agent_name:
            card_to_play = self.my_hand[0]
            self.my_hand = self.my_hand[1:]
            return card_to_play

        pass

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
