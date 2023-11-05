# import random
from object import *
from movement import *
from os.path import join
from parametrs import *
from player import Player, window
import pygame


pygame.init()

pygame.display.set_caption("Ultimate MIPT Game")


def get_background(name):
    """
    generate background
    :param name: image path
    :return: array of 'blocks' and background image
    """
    bg_image = pygame.image.load(join("img", "back_space", name))
    _, _, im_width, im_height = bg_image.get_rect()
    blocks = []
    for i in range(WIDTH // im_width + 1):
        for j in range(HEIGHT // im_height + 1):
            blocks.append((i * im_width, j * im_height))
    return blocks, bg_image


def display(screen, background, image, player, objs, shift_x):
    """
    Displays background on the screen
    :param screen: window in which you wanna draw background
    :param background: generated background
    :param image: image for background
    :param player: player which will be displayed
    :param objs:
    :param shift_x:
    :return: None
    """
    for block in background:  # block - is rectangle in which it's been drawn
        screen.blit(image, block)

    for obj in objs:
        obj.display(screen, shift_x)

    player.display(screen, shift_x)

    pygame.display.update()  # updates your display


def get_map_surf(floor):
    """
    generate surface for map
    may be random in future
    :param floor:
    :return:
    """
    return [*floor, Block(0, HEIGHT - BLOCK_SIZE * 2, BLOCK_SIZE),
            Block(3 * BLOCK_SIZE, HEIGHT - BLOCK_SIZE * 4, BLOCK_SIZE)]


def main(screen):
    """
    main function of the game
    :param screen: window in wich game starts
    :return: None
    """
    timer = pygame.time.Clock()
    background, bg_img = get_background("gray.png")

    player = Player(100, 100, 50, 50)
    floor = [Block(i * BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
             for i in range(-WIDTH // BLOCK_SIZE, WIDTH * 2 // BLOCK_SIZE)]
    map_surf = get_map_surf(floor)
    shift_x = 0

    run = True
    while run:
        timer.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player.jump_count < 2:
                    player.jump()

        # I draw objects here
        player.loop(FPS)
        move_processing(player, map_surf)
        display(screen, background, bg_img, player, map_surf, shift_x)

        if (player.rect.right - shift_x >= WIDTH - VIEW_AREA_WIDTH and player.x_speed > 0) or (
                player.rect.left - shift_x <= VIEW_AREA_WIDTH and player.x_speed < 0):
            shift_x += player.x_speed

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
