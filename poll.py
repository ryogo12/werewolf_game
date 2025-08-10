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


async def draw_poll_scene(poll_index, player):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text_drawer.draw_text(text='プレイヤー', font_size=FONT_SIZE_M, x=
        SELECTED_PLAYER_X, y=SELECTED_PLAYER_Y)
    DECREASE_BUTTON.draw('-')
    text_drawer.draw_text(text=str(poll_index + 1), font_size=
        FONT_SIZE_M, x=PLAYER_NUMBER_X, y=SELECTED_PLAYER_Y)
    INCREASE_BUTTON.draw('+')
    text_drawer.draw_text(text='に投票する。', font_size=FONT_SIZE_M, x=
        SELECTED_PLAYER_X, y=ADDITIONAL_TEXT_Y)
    if player['role'] == '村人':
        image = IMAGE_VILLAGER_BIG
    elif player['role'] == '占い師':
        image = IMAGE_FORTUNE_TELLER_BIG
    elif player['role'] == '人狼':
        image = IMAGE_WEREWOLF_BIG
    SCREEN.blit(image, (IMAGE_X, IMAGE_Y))
    SELECT_BUTTON.draw('決定')


async def update_poll_scene(player_index_for_poll, poll_index,
    poll_index_max, players):
    scene = SCENE_POLL
    pos = pygame.mouse.get_pos()
    if INCREASE_BUTTON.get_rect().collidepoint(pos):
        poll_index += 1
        if poll_index > poll_index_max:
            poll_index = poll_index_max
    elif DECREASE_BUTTON.get_rect().collidepoint(pos):
        poll_index -= 1
        if poll_index < 0:
            poll_index = 0
    elif SELECT_BUTTON.get_rect().collidepoint(pos):
        players[poll_index]['poll_count'] += 1
        player_index_for_poll += 1
        scene = SCENE_PLAYER_FOR_POLL
    return scene, player_index_for_poll, poll_index, players
