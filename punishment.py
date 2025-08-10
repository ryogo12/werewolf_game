import pygame
from common import *
BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S, x=
    BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_punishment_scene(poll_result):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    if '平和村' in poll_result:
        text = '全員の投票数が同数だったので、処刑は行われませんでした。'
    else:
        text = '処刑されたのは'
        for p in poll_result:
            text += f"「{p['name']}」"
        text += 'です。'
    text_drawer.draw_text_with_line_break(text=text, font_size=
        FONT_SIZE_M, x=TEXT_X, y=TEXT_Y, w=TEXT_W)
    BUTTON.draw('結果へ')


async def update_punishment_scene():
    pos = pygame.mouse.get_pos()
    scene = SCENE_PUNISHMENT
    if BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_RESULT
    return scene
