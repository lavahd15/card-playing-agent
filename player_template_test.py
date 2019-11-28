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
        state = [["9", "8", "7", "6", "5", "4", "3", "2"], ["A", "K", "Q", "5", "3"],
                 ["A", "Q", "J", "T"], ["6", "5", "3"]]
        self.assertIn(get_card_to_play_first(["AS", "AC", "KH", "2C", "4D"], state), ("KH"))

    def test_get_card_to_play_first_case2(self):
        state = [["9", "8", "7", "6", "5", "4", "3", "2"], ["A", "Q", "5", "3"],
                 ["A", "Q", "J", "T"], ["6", "5", "3"]]
        self.assertEqual(get_card_to_play_first(["KS", "KC", "2C", "4D"], state), "2C")

    def test_get_card_to_play_first_case3(self):
        state = [["9", "8", "7", "6", "5", "4", "3", "2"], ["A", "K", "Q", "5", "3"],
                 ["A", "Q", "J", "T"], ["6", "5", "3"]]
        self.assertIn(get_card_to_play_first(["AS", "AC", "2C", "4D"], state), ("AS", "AC"))

    def test_get_card_to_play_first_case4(self):
        state = [["9", "8", "7", "6", "5", "4", "3", "2"], ["A", "K", "Q", "5", "3"],
                 ["A", "Q", "J", "T"], ["6", "5", "3"]]
        self.assertEqual(get_card_to_play_first(["KS", "KC", "7D"], state), "7D")

    def test_get_card_to_play_first_case5(self):
        state = [["9", "8", "7", "6", "5", "4", "3", "2"], ["A", "K", "Q", "5", "3"],
                 ["A", "Q", "J", "T"], ["6", "5", "3"]]
        self.assertEqual(get_card_to_play_first(["KS", "KC", "4D", "2S"], state), "2S")

