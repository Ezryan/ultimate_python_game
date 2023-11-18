import pygame
from support import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        """

        :param size:
        :param x:
        :param y:
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        """

        :param shift:
        :return:
        """
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        """

        :param size:
        :param x:
        :param y:
        :param surface:
        """
        super().__init__(size, x, y)
        self.image = surface


class Crate(StaticTile):
    def __init__(self, size, x, y):
        """

        :param size:
        :param x:
        :param y:
        """
        super().__init__(
            size,
            x,
            y,
            pygame.image.load("../graphics/terrain/crate.png").convert_alpha(),
        )
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):
        """

        :param size:
        :param x:
        :param y:
        :param path:
        """
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        """

        :return:
        """
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        """

        :param shift:
        :return:
        """
        self.animate()
        self.rect.x += shift


class Coin(AnimatedTile):
    def __init__(self, size, x, y, path, value):
        """

        :param size:
        :param x:
        :param y:
        :param path:
        :param value:
        """
        super().__init__(size, x, y, path)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.value = value


class Palm(AnimatedTile):
    def __init__(self, size, x, y, path, offset):
        """

        :param size:
        :param x:
        :param y:
        :param path:
        :param offset:
        """
        super().__init__(size, x, y, path)
        offset_y = y - offset
        self.rect.topleft = (x, offset_y)
