from parametrs import *
import pygame
from os import listdir
from os.path import isfile, join


pygame.init()



def flip_image(sprites):
    """
    flipping sprites array with pygame.transform.flip
    :param sprites: array of sprites
    :return: array of flipped sprites
    """
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_list(dir_f, dir_s, width, height, is_directed=False):
    """
    loads sprite from file
    :param dir_f:
    :param dir_s:
    :param width:
    :param height:
    :param is_directed:
    :return: dictionary/hash_table of loaded sprites
    """
    path = join("img", dir_f, dir_s)
    images = [file for file in listdir(path) if isfile(join(path, file))]

    sprites_dict = {}

    for image in images:
        sprite_layer = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_layer.get_width() // width):
            surface_buffer = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect_buffer = pygame.Rect(i * width, 0, width, height)
            surface_buffer.blit(sprite_layer, (0, 0), rect_buffer)
            sprites.append(pygame.transform.scale2x(surface_buffer))

        if is_directed:
            sprites_dict[image.replace(".png", "") + "_right"] = sprites
            sprites_dict[image.replace(".png", "") + "_left"] = flip_image(sprites)
        else:
            sprites_dict[image.replace(".png", "")] = sprites

    return sprites_dict


def get_block(size):
    path = join("img", "terrain", "terrain.png")
    image_buffer = pygame.image.load(path).convert_alpha()
    surface_buffer = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect_buffer = pygame.Rect(TERRAIN_IM, 0, size, size)
    surface_buffer.blit(image_buffer, (0, 0), rect_buffer)
    return pygame.transform.scale2x(surface_buffer)
