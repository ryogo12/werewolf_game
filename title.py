import pygame
from common import *
TITLE_X = SIDE // 24 * 2
TITLE_Y = SIDE // 24 * 10
BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S, x=
    BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_title_scene():
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text_drawer.draw_text(text='ワンナイト人狼', font_size=FONT_SIZE_L, x=
        TITLE_X, y=TITLE_Y)
    BUTTON.draw('村へ')


async def update_title_scene():
    pos = pygame.mouse.get_pos()
    scene = SCENE_TITLE
    if BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_VILLAGE
    return scene
