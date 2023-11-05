from parametrs import *
import pygame
from work_with_files import load_sprite_list

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    """
    Player class
    """
    COLOR = (255, 0, 0)
    SPRITES = load_sprite_list("player", "MaskSkin", 32, 32, True)
    ANIMATION_PING = 5

    def __init__(self, x_pos, y_pos, width, height):
        """
        Simple constructor
        :param x_pos:
        :param y_pos:
        :param width:
        :param height:
        """
        super().__init__()
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.x_speed = 0
        self.y_speed = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.sprite = None
        self.jump_count = 0
        self.count = 0

    def jump(self):
        """
        jump method
        :return:
        """
        self.y_speed = -GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, delta_x, delta_y):
        """
        updates radius vector of Player class object
        adds (delta_x, delta_y) -> vector of movement
        :param delta_x: axis x movement
        :param delta_y: axis y movement
        :return:
        """
        self.rect.x += delta_x
        self.rect.y += delta_y

    def move_left(self, speed):
        """
        moves Player in left direction with x-axis speed = speed
        :param speed: speed of movement
        :return: None
        """
        self.x_speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, speed):
        """
        moves Player in right direction with x-axis speed = speed
        :param speed: speed of movement
        :return: None
        """
        self.x_speed = speed
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        """
        updates animation
        :param fps:
        :return: None
        """
        self.y_speed += min(1, (self.fall_count / fps) * GRAVITY)
        self.move(self.x_speed, self.y_speed)

        self.fall_count += 1
        self.update_outfit()

    def landed(self):
        """
        landing
        :return:
        """
        self.fall_count = 0
        self.y_speed = 0
        self.jump_count = 0

    def hit_head(self):
        """
        hitting
        :return:
        """
        self.count = 0
        self.y_speed *= -1

    def update_outfit(self):
        """
        updates sprite
        :return:
        """
        sprite_list = "idle"
        if self.y_speed != 0:
            if self.jump_count == 1:
                sprite_list = "jump"
            elif self.jump_count == 2:
                sprite_list = "double_jump"
        elif self.y_speed > GRAVITY * 2:
            sprite_list = "fall"
        if self.x_speed != 0:
            sprite_list = "run"

        sprite_list_name = sprite_list + "_" + self.direction
        sprites = self.SPRITES[sprite_list_name]
        sprite_ind = (self.animation_count // self.ANIMATION_PING) % len(sprites)
        self.sprite = sprites[sprite_ind]
        self.animation_count += 1
        self.update()

    def update(self):
        """
        update condition
        :return:
        """
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def display(self, screen, shift_x):
        """
        draw Player class object
        :param screen: screen in which draws
        :param shift_x: offset in x-axis to move camera
        :return: None
        """
        screen.blit(self.sprite, (self.rect.x - shift_x, self.rect.y))
