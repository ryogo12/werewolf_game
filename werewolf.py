import pygame
from common import *
BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S, x=
    BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_werewolf_scene(players):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text = '人狼は'
    for player in players:
        if player['name'] != '墓地' and player['role'] == '人狼':
            text += f"「{player['name']}」"
    text += 'です。'
    text_drawer.draw_text_with_line_break(text=text, font_size=
        FONT_SIZE_M, x=TEXT_X, y=TEXT_Y, w=TEXT_W)
    BUTTON.draw('確認')


async def update_werewolf_scene(player_index):
    pos = pygame.mouse.get_pos()
    scene = SCENE_WEREWOLF
    if BUTTON.get_rect().collidepoint(pos):
        player_index += 1
        scene = SCENE_PLAYER
    return scene, player_index
