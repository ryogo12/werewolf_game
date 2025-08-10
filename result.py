from common import *


async def draw_result_scene(werewolf_is_winner):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    if werewolf_is_winner:
        text = '勝利したのは「人狼チーム」です！'
    else:
        text = '勝利したのは「村人チーム」です！'
    text_drawer.draw_text_with_line_break(text=text, font_size=
        FONT_SIZE_M, x=TEXT_X, y=TEXT_Y, w=TEXT_W)
    if werewolf_is_winner:
        image = IMAGE_WEREWOLF_BIG
    else:
        image = IMAGE_VILLAGER_BIG
    SCREEN.blit(image, (IMAGE_X, IMAGE_Y))
