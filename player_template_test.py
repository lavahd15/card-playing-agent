import unittest

from player_template import Player, get_card_to_play_last


class PlayerTemplateTest(unittest.TestCase):
    def test_get_name(self):
        player = Player()
        self.assertEqual("DEVIL", player.get_name())

    def test_get_card_to_play_last_same_suit(self):
        print(get_card_to_play_last(["TD", "8D", "7D"], {"D": ["4D", "JD", "KD", ]}))

    def test_get_card_to_play_last_different_suit(self):
        print(get_card_to_play_last(["TD", "8D", "7D"], {"D":[],"H": ["4H"], "S": ["4S", "KS", ]}))
