import pygame
from tiles import AnimatedTile
from random import randint


class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, '../graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        """
        moves enemy
        :return:
        """
        self.rect.x += self.speed

    def reverse_image(self):
        """
        reverse Sprite for enemy going
        :return:
        """
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        """
        reverse speed
        :return:
        """
        self.speed *= -1

    def update(self, shift):
        """
        updates Enemy object
        :param shift:
        :return:
        """
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()
