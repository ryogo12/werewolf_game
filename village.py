import pygame
import random
from common import *
from datetime import datetime
DESCRIPTION_Y = SIDE // 24
ROLE_X = SIDE // 24
IMAGE_VILLAGER_X = SIDE // 24 * 5
IMAGE_FORTUNE_TELLER_X = SIDE // 24 * 7
IMAGE_WEREWOLF_X = SIDE // 24 * 5
ROLE_DESCRIPTION_X = SIDE // 24 * 9
ROLE_DESCRIPTION_W = SIDE // 24 * 8
ROLE_NUMBER_X = SIDE // 24 * 19.5
VILLAGER_Y = SIDE // 24 * 3
FORTUNE_TELLER_Y = SIDE // 24 * 7
WEREWOLF_Y = SIDE // 24 * 12
INCREASE_BUTTON_X = SIDE // 24 * 22
DECREASE_BUTTON_X = SIDE // 24 * 18
INCREASE_OR_DECREASE_BUTTON_Y_1 = SIDE // 24 * 4
INCREASE_OR_DECREASE_BUTTON_Y_2 = SIDE // 24 * 8
INCREASE_OR_DECREASE_BUTTON_Y_3 = SIDE // 24 * 13
VILLAGER_MIN = 2
VILLAGER_MAX = 9
FORTUNE_TELLER_MIN = 1
FORTUNE_TELLER_MAX = 1
WEREWOLF_MIN = 2
WEREWOLF_MAX = 9
INCREASE_VILLAGER_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=INCREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y_1, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
DECREASE_VILLAGER_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=DECREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y_1, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
INCREASE_FORTUNE_TELLER_BUTTON = Button(font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S, x=INCREASE_BUTTON_X, y=
    INCREASE_OR_DECREASE_BUTTON_Y_2, w=INCREASE_OR_DECREASE_BUTTON_SIDE, h=
    INCREASE_OR_DECREASE_BUTTON_SIDE)
DECREASE_FORTUNE_TELLER_BUTTON = Button(font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S, x=DECREASE_BUTTON_X, y=
    INCREASE_OR_DECREASE_BUTTON_Y_2, w=INCREASE_OR_DECREASE_BUTTON_SIDE, h=
    INCREASE_OR_DECREASE_BUTTON_SIDE)
INCREASE_WEREWOLF_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=INCREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y_3, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
DECREASE_WEREWOLF_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=
    FONT_SIZE_S, x=DECREASE_BUTTON_X, y=INCREASE_OR_DECREASE_BUTTON_Y_3, w=
    INCREASE_OR_DECREASE_BUTTON_SIDE, h=INCREASE_OR_DECREASE_BUTTON_SIDE)
START_BUTTON = Button(font_file=JAPANESE_FONT_FILE, font_size=FONT_SIZE_S,
    x=BUTTON_X, y=BUTTON_Y, w=BUTTON_W, h=BUTTON_H)


async def draw_village_scene(villager_count, fortune_teller_count,
    werewolf_count):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    text_drawer.draw_text(text='役職の合計を（参加人数＋２）人にしてください。', font_size=
        FONT_SIZE_S, x=ROLE_X, y=DESCRIPTION_Y)
    text_drawer.draw_text(text='村人', font_size=FONT_SIZE_M, x=ROLE_X,
        y=VILLAGER_Y)
    SCREEN.blit(IMAGE_VILLAGER, (IMAGE_VILLAGER_X, VILLAGER_Y))
    text_drawer.draw_text_with_line_break(text='村人チームです。特に役割はありません。',
        font_size=FONT_SIZE_S, x=ROLE_DESCRIPTION_X, y=VILLAGER_Y, w=
        ROLE_DESCRIPTION_W)
    DECREASE_VILLAGER_BUTTON.draw('-')
    text_drawer.draw_text(text=str(villager_count), font_size=
        FONT_SIZE_M, x=ROLE_NUMBER_X, y=VILLAGER_Y)
    INCREASE_VILLAGER_BUTTON.draw('+')
    text_drawer.draw_text(text='占い師', font_size=FONT_SIZE_M, x=ROLE_X,
        y=FORTUNE_TELLER_Y)
    SCREEN.blit(IMAGE_FORTUNE_TELLER, (IMAGE_FORTUNE_TELLER_X,
        FORTUNE_TELLER_Y))
    text_drawer.draw_text_with_line_break(text=
        '村人チームです。プレイヤー1人か墓地の2枚の役職がわかります。', font_size=FONT_SIZE_S, x=
        ROLE_DESCRIPTION_X, y=FORTUNE_TELLER_Y, w=ROLE_DESCRIPTION_W)
    DECREASE_FORTUNE_TELLER_BUTTON.draw('-')
    text_drawer.draw_text(text=str(fortune_teller_count), font_size=
        FONT_SIZE_M, x=ROLE_NUMBER_X, y=FORTUNE_TELLER_Y)
    INCREASE_FORTUNE_TELLER_BUTTON.draw('+')
    text_drawer.draw_text(text='人狼', font_size=FONT_SIZE_M, x=ROLE_X,
        y=WEREWOLF_Y)
    SCREEN.blit(IMAGE_WEREWOLF, (IMAGE_WEREWOLF_X, WEREWOLF_Y))
    text_drawer.draw_text_with_line_break(text=
        '人狼チームです。村人チームには、自分が人狼だとバレないようにしましょう。', font_size=FONT_SIZE_S, x=
        ROLE_DESCRIPTION_X, y=WEREWOLF_Y, w=ROLE_DESCRIPTION_W)
    DECREASE_WEREWOLF_BUTTON.draw('-')
    text_drawer.draw_text(text=str(werewolf_count), font_size=
        FONT_SIZE_M, x=ROLE_NUMBER_X, y=WEREWOLF_Y)
    INCREASE_WEREWOLF_BUTTON.draw('+')
    START_BUTTON.draw('スタート')


async def update_village_scene(villager_count, fortune_teller_count,
    werewolf_count, players):
    scene = SCENE_VILLAGE
    pos = pygame.mouse.get_pos()
    if START_BUTTON.get_rect().collidepoint(pos):
        roles = []
        for _ in range(villager_count):
            roles.append('村人')
        for _ in range(fortune_teller_count):
            roles.append('占い師')
        for _ in range(werewolf_count):
            roles.append('人狼')
        now = datetime.now()
        milliseconds = int(now.timestamp() * 1000)
        random.seed(milliseconds)
        random.shuffle(roles)
        for i in range(villager_count + fortune_teller_count + werewolf_count):
            if i < villager_count + fortune_teller_count + werewolf_count - 2:
                name = f'プレイヤー{i + 1}'
            else:
                name = '墓地'
            players.append({'name': name, 'role': roles.pop(),
                'villager_poll_count': 0, 'poll_count': 0})
        scene = SCENE_PLAYER
    elif INCREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        villager_count += 1
        if villager_count > VILLAGER_MAX:
            villager_count = VILLAGER_MAX
    elif DECREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        villager_count -= 1
        if villager_count < VILLAGER_MIN:
            villager_count = VILLAGER_MIN
    elif INCREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        fortune_teller_count += 1
        if fortune_teller_count > FORTUNE_TELLER_MAX:
            fortune_teller_count = FORTUNE_TELLER_MAX
    elif DECREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        fortune_teller_count -= 1
        if fortune_teller_count < FORTUNE_TELLER_MIN:
            fortune_teller_count = FORTUNE_TELLER_MIN
    elif INCREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        werewolf_count += 1
        if werewolf_count > WEREWOLF_MAX:
            werewolf_count = WEREWOLF_MAX
    elif DECREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        werewolf_count -= 1
        if werewolf_count < WEREWOLF_MIN:
            werewolf_count = WEREWOLF_MIN
    return scene, villager_count, fortune_teller_count, werewolf_count, players
