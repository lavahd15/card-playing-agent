import random

from player_template import Player


def main():
    deck = get_randomized_deck()
    #
    # player1 = Player()
    # player1.agent_name = "Player1"
    # player1.add_cards_to_hand(deck[:13])
    #
    # player2 = Player()
    # player2.agent_name = "Player2"
    # player2.add_cards_to_hand(deck[13:26])
    #
    # player3 = Player()
    # player3.agent_name = "Player3"
    # player3.add_cards_to_hand(deck[26:39])
    #
    # player4 = Player()
    # player4.agent_name = "Player4"
    # player4.add_cards_to_hand(deck[39:52])

    player1 = Player()
    player1.agent_name = "DEVIL"

    clockwise_name = ["DEVIL", "J", "H", "B"]
    player1.new_hand(clockwise_name)
    player1.add_cards_to_hand(["4D", "5D", "TD", "2C", "8C", "2H", "3H", "4H", "7H", "8H", "9H", "5S", "AS"])

    played_card = player1.play_card("DEVIL", [])
    print(played_card)

    player1.collect_trick("B", "H", ["4D", "9D", "8D", "QD"])


def get_randomized_deck():
    suits = ["H", "S", "C", "D"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    random.shuffle(deck)
    return deck


if __name__ == '__main__':
    main()
