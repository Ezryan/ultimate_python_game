from unittest import TestCase

from code.main import Game

game = Game()


class TestGame(TestCase):
    def test_change_coins(self):
        game.change_coins(10)
