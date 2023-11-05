import pygame
from work_with_files import get_block

pygame.init()


class Object(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def display(self, screen, shift_x):
        screen.blit(self.image, (self.rect.x - shift_x, self.rect.y))


class Block(Object):
    def __init__(self, x_pos, y_pos, size):
        super().__init__(x_pos, y_pos, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
