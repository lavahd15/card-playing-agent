import unittest

from player_template import Player


class PlayerTemplateTest(unittest.TestCase):
    def test_get_name(self):
        player = Player()
        self.assertEqual("DEVIL", player.get_name())
