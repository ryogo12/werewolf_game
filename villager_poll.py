import pygame
from common import *
INCREASE_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=INCREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
DECREASE_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=DECREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
SELECT_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S,
    x=BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_villager_poll_scene(villager_poll_index):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text_drawer.draw_text(text='プレイヤー', font_size=FONT_SIZE_M, x=
        SELECTED_PLAYER_X, y=SELECTED_PLAYER_Y)
    DECREASE_BUTTON.draw('-')
    text_drawer.draw_text(text=str(villager_poll_index + 1),
        font_size=FONT_SIZE_M, x=PLAYER_NUMBER_X, y=SELECTED_PLAYER_Y)
    INCREASE_BUTTON.draw('+')
    text_drawer.draw_text(text='が怪しいと思う。', font_size=FONT_SIZE_M, x=
        SELECTED_PLAYER_X, y=ADDITIONAL_TEXT_Y)
    SCREEN.blit(IMAGE_VILLAGER_BIG, (IMAGE_X, IMAGE_Y))
    SELECT_BUTTON.draw('決定')


async def update_villager_poll_scene(player_index, villager_poll_index,
    villager_poll_index_max, players):
    scene = SCENE_VILLAGER_POLL
    pos = pygame.mouse.get_pos()
    if INCREASE_BUTTON.get_rect().collidepoint(pos):
        villager_poll_index += 1
        if villager_poll_index > villager_poll_index_max:
            villager_poll_index = villager_poll_index_max
    elif DECREASE_BUTTON.get_rect().collidepoint(pos):
        villager_poll_index -= 1
        if villager_poll_index < 0:
            villager_poll_index = 0
    elif SELECT_BUTTON.get_rect().collidepoint(pos):
        players[villager_poll_index]['villager_poll_count'] += 1
        villager_poll_index = 0
        player_index += 1
        scene = SCENE_PLAYER
    return scene, player_index, villager_poll_index, players
