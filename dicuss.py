import pygame
from common import *
SECOND = 60
BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S, x=
    BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_discuss_scene(discuss_start_time, most_suspicious_player):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text = '誰が人狼か明らかにするための議論を開始してください。村人から最も怪しまれているのは'
    for player in most_suspicious_player:
        text += f"「{player['name']}」"
    text += 'です。'
    text_drawer.draw_text_with_line_break(text=text, font_size=
        FONT_SIZE_M, x=TEXT_X, y=LONG_TEXT_Y, w=TEXT_W)
    timedelta = pygame.time.get_ticks() - discuss_start_time
    text_drawer.draw_text(text=
        f'{SECOND - timedelta // 1000}秒後に画面移動します。', font_size=FONT_SIZE_S,
        x=TIMEDELTA_TEXT_X, y=TIMEDELTA_TEXT_Y)
    BUTTON.draw('投票へ')
    scene = SCENE_DISCUSS
    if timedelta > SECOND * 1000:
        scene = SCENE_PLAYER_FOR_POLL
    return scene


async def update_discuss_scene():
    pos = pygame.mouse.get_pos()
    scene = SCENE_DISCUSS
    if BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_PLAYER_FOR_POLL
    return scene
