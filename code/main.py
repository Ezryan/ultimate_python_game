import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI


class Game:
    def __init__(self):

        # game attributes
        self.max_level = 0
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # overworld creation
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = "overworld"

        # user interface
        self.ui = UI(screen)

    def create_level(self, current_level):
        """

        :param current_level:
        :return:
        """
        self.level = Level(
            current_level,
            screen,
            self.create_overworld,
            self.change_coins,
            self.change_health,
        )
        self.status = "level"

    def create_overworld(self, current_level, new_max_level):
        """

        :param current_level:
        :param new_max_level:
        :return:
        """
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(
            current_level, self.max_level, screen, self.create_level
        )
        self.status = "overworld"

    def change_coins(self, amount):
        """

        :param amount:
        :return:
        """
        self.coins += amount

    def change_health(self, amount):
        """

        :param amount:
        :return:
        """
        self.cur_health += amount

    def check_game_over(self):
        """

        :return:
        """
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = "overworld"

    def run(self):
        """

        :return:
        """
        if self.status == "overworld":
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("grey")
    game.run()

    # unit test
    if game.cur_health < 100:
        print("Health is decrease")

    pygame.display.update()
    clock.tick(60)
