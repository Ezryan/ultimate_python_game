from parametrs import*
import pygame


pygame.init()


def vertical_collision_processing(player, objects, delta_y):
    """
    this function handling vertical collisions
    :param player:
    :param objects:
    :param delta_y:
    :return:
    """
    touched_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if delta_y > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif delta_y < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

        touched_objects.append(obj)

    return touched_objects


def touch(player, objs, delta_x):
    """
    this function checking objects which in touch with player
    :param player:
    :param objs:
    :param delta_x:
    :return:
    """
    player.move(delta_x, 0)
    player.update()
    touched_obj = None
    for obj in objs:
        if pygame.sprite.collide_mask(player, obj):
            touched_obj = obj
            break

    player.move(-delta_x, 0)
    player.update()
    return touched_obj


def move_processing(player, objects):
    """
    processing keys pressing for moving
    :param player:
    :param objects:
    :return:
    """
    keys = pygame.key.get_pressed()

    player.x_speed = 0
    touch_left = touch(player, objects, -PLAYER_SPEED * 2)
    touch_right = touch(player, objects, PLAYER_SPEED * 2)

    if keys[pygame.K_a] and not touch_left:
        player.move_left(PLAYER_SPEED)
    if keys[pygame.K_d] and not touch_right:
        player.move_right(PLAYER_SPEED)

    vertical_collision_processing(player, objects, player.y_speed)
