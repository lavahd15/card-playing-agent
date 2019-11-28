import unittest

from player_template import Player, get_card_to_play_last, get_card_to_play_first, get_card_to_play


class PlayerTemplateTest(unittest.TestCase):
    def test_get_name(self):
        player = Player()
        self.assertEqual("DEVIL", player.get_name())

    def test_get_card_to_play_last_same_suit(self):
        print(get_card_to_play_last(["TD", "8D", "7D"], {"D": ["4D", "JD", "KD", ]}))

    def test_get_card_to_play_last_different_suit(self):
        print(get_card_to_play_last(["TD", "8D", "7D"], {"D":[],"H": ["4H"], "S": ["4S", "KS", ]}))

    def test_get_card_to_play_first_case1(self):
        state = {"S": ["2", "3", "4", "5", "6", "7", "8", "9"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]}
        self.assertIn(get_card_to_play_first(["AS", "AC", "KH", "2C", "4D"], state), ("AS", "AC"))

    def test_get_card_to_play_first_case2(self):
        state = {"S": ["2", "3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["KS", "KC", "KH", "2C", "4D"], state), "KC")

    def test_get_card_to_play_first_case3(self):
        state = {"S": ["2", "3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["KS", "KC", "KH", "2C", "4D"], state), "KC")

    def test_get_card_to_play_first_case4(self):
        state = {"S": ["2", "3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["KS", "KH", "2C", "4D"], state), "2C")

    def test_get_card_to_play_first_case5(self):
        state = {"S": ["2", "3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["KS", "KH", "2C", "4D"], state), "2C")

    def test_get_card_to_play_first_case6(self):
        state = {"S": ["3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["KS", "KH", "2C", "4D", "2S"], state), "2S")

    def test_get_card_to_play_first_case7(self):
        state = {"S": ["3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6", "8"]
                 }
        self.assertEqual(get_card_to_play_first(["TS", "3H", "4H", "7C", "4D"], state), "3H")

    def test_get_card_to_play_first_case8(self):
        state = {"S": ["3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        self.assertEqual(get_card_to_play_first(["TS", "3H", "4H", "7C", "4D"], state), "7C")

    # Test if the card is removed from my hand
    def test_get_card_to_play_first_case9(self):
        state = {"S": ["3", "4", "5", "6", "7", "8", "9", "A"],
                 "D": ["3", "5", "Q", "K", "A"],
                 "H": ["T", "J", "Q", "A"],
                 "C": ["3", "5", "6"]
                 }
        my_hand = ["TS", "3H", "4H", "7C", "4D"]
        get_card_to_play([], my_hand, state)
        self.assertEqual(my_hand, ["TS", "3H", "4H", "4D"])
