class Player(object):
    def __init__(self):
        pass

    def get_name(self):
        """
        Returns a string of the agent's name
        """
        pass

    def get_hand(self):
        """
        Returns a list of two character strings reprsenting cards in the agent's hand
        """
        pass

    def new_hand(self, names):
        """
        Takes a list of names of all agents in the game in clockwise playing order
        and returns nothing. This method is also responsible for clearing any data
        necessary for your agent to start a new round.
        """
        pass

    def add_cards_to_hand(self, cards):
        """
        Takes a list of two character strings representing cards as an argument
        and returns nothing.
        This list can be any length.
        """
        pass

    def play_card(self, lead, trick):
        """
        Takes a a string of the name of the player who lead the trick and
        a list of cards in the trick so far as arguments.

        Returns a two character string from the agents hand of the card to be played
        into the trick.
        """
        pass

    def collect_trick(self, lead, winner, trick):
        """
        Takes three arguements. Lead is the name of the player who led the trick.
        Winner is the name of the player who won the trick. And trick is a four card
        list of the trick that was played. Should return nothing.
        """
        pass

    def score(self):
        """
        Calculates and returns the score for the game being played.
        """
        pass