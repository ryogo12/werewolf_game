import pygame
SIDE = 512
SCREEN = pygame.display.set_mode((SIDE, SIDE))
BUTTON_X = SIDE // 24 * 12
BUTTON_Y = SIDE // 24 * 20
BUTTON_W = SIDE // 24 * 9
BUTTON_H = SIDE // 24 * 3
BUTTON_LEFT_X = SIDE // 24 * 7
BUTTON_RIGHT_X = SIDE // 24 * 17
TEXT_X = SIDE // 24 * 3
TEXT_Y = SIDE // 24 * 7
LONG_TEXT_Y = SIDE // 24 * 4
TEXT_W = SIDE // 24 * 20
IMAGE_X = SIDE // 24 * 10
IMAGE_Y = SIDE // 24 * 13
TIMEDELTA_TEXT_X = SIDE // 24 * 7
TIMEDELTA_TEXT_Y = SIDE // 24 * 15
SELECTED_PLAYER_X = SIDE // 24 * 4
SELECTED_PLAYER_Y = SIDE // 24 * 6
INCREASE_BUTTON_X = SIDE // 24 * 19
DECREASE_BUTTON_X = SIDE // 24 * 15
INCREASE_OR_DECREASE_BUTTON_Y = SIDE // 24 * 7
PLAYER_NUMBER_X = SIDE // 24 * 16.5
ADDITIONAL_TEXT_Y = SIDE // 24 * 9
INCREASE_OR_DECREASE_BUTTON_SIDE = SIDE // 24 * 2
JAPANESE_FONT_FILE = 'ipaexg.ttf'
FONT_SIZE_L = 60
FONT_SIZE_M = 40
FONT_SIZE_S = 20
PLAYER_X = SIDE // 24 * 2
PLAYER_Y = SIDE // 24 * 8
PLAYER_W = SIDE // 24 * 22
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE_STRONG = '#3879CE'
BLUE_LIGHT = '#e0ffff'
SCENE_TITLE = 0
SCENE_VILLAGE = 1
SCENE_PLAYER = 2
SCENE_ROLE = 3
SCENE_VILLAGER_POLL = 4
SCENE_FORTUNE_TELLER_SELECT = 5
SCENE_FORTUNE_TELLER = 6
SCENE_FORTUNE_TELLER_ROLE = 7
SCENE_WEREWOLF = 8
SCENE_DISCUSS = 9
SCENE_PLAYER_FOR_POLL = 10
SCENE_POLL = 11
SCENE_PUNISHMENT = 12
SCENE_RESULT = 13
IMAGE_VILLAGER = pygame.image.load(
    'images/character_murabito_young_man_green.png')
IMAGE_FORTUNE_TELLER = pygame.image.load('images/character_uranaishi_02.png')
IMAGE_WEREWOLF = pygame.image.load('images/character_jujin_okami_man_gray.png')
IMAGE_VILLAGER_BIG = pygame.image.load(
    'images/character_murabito_young_man_green (1).png')
IMAGE_FORTUNE_TELLER_BIG = pygame.image.load(
    'images/character_uranaishi_02 (1).png')
IMAGE_WEREWOLF_BIG = pygame.image.load(
    'images/character_jujin_okami_man_gray (1).png')
MAPTILE_GRASS_1 = pygame.image.load('images/maptile_sogen_01.png')
MAPTILE_GRASS_2 = pygame.image.load('images/maptile_sogen_02.png')
MAPTILE_SUN = pygame.image.load('images/weather_sunny.png')
MAPTILE_CLOUD = pygame.image.load('images/weather_cloudy_white.png')
MAPTILE_MOON = pygame.image.load('images/moon_lightyellow.png')
MAPTILE_STAR = pygame.image.load('images/kirakira_02_lightyellow.png')
MAPTILE_CHURCH = pygame.image.load('images/kyokai_02_brown.png')
MAP_DICT = {'g1': MAPTILE_GRASS_1, 'g2': MAPTILE_GRASS_2, 'sun':
    MAPTILE_SUN, 'cloud': MAPTILE_CLOUD, 'm': MAPTILE_MOON, 'star':
    MAPTILE_STAR, 'church': MAPTILE_CHURCH}
MAP_DATA_NIGHT = [['', '', '', '', '', '', '', '', '', '', '', '', '', '',
    '', ''], ['', '', '', '', '', '', '', 'star', '', '', '', '', '', '',
    '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', 'm', '', '',
    ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', 'star', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', '', 'church', '', '', '', '', '', '', '', '', 'star', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', '', '', '', '', '', 'star', '', '', '', '', '', '', '', ''], ['',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['g1',
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1',
    'g1', 'g1', 'g1'], ['g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1',
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1'], ['g1', 'g1', 'g1',
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1',
    'g1'], ['g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1',
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1'], ['g1', 'g1', 'g1', 'g1', 'g1',
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1'], [
    'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1', 'g1',
    'g1', 'g1', 'g1', 'g1']]
MAP_DATA_DAY = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    ''], ['', '', '', '', '', '', '', 'cloud', '', '', '', '', '', '', '',
    ''], ['', '', '', '', '', '', '', '', '', '', '', '', 'sun', '', '', ''
    ], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], [
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', 'cloud', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', '', 'church', '', '', '', '', '', '', '', '', 'cloud', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['',
    '', '', '', '', '', '', 'cloud', '', '', '', '', '', '', '', ''], ['',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['g2',
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2',
    'g2', 'g2', 'g2'], ['g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2',
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2'], ['g2', 'g2', 'g2',
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2',
    'g2'], ['g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2',
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2'], ['g2', 'g2', 'g2', 'g2', 'g2',
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2'], [
    'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2',
    'g2', 'g2', 'g2', 'g2']]
LAYER = pygame.Surface((SIDE, SIDE), flags=pygame.SRCALPHA)
LAYER.fill((0, 0, 0, 160))


class TextDrawer:

    def __init__(self, font_file):
        self.font_file = font_file

    def draw_text(self, text, font_size, x, y, color=WHITE):
        font = pygame.font.Font(self.font_file, font_size)
        text_surface = font.render(text, True, color)
        SCREEN.blit(text_surface, (x, y))

    def draw_text_with_line_break(self, text, font_size, x, y, w,
        color=WHITE):
        font = pygame.font.Font(self.font_file, font_size)
        blit_x = x
        blit_y = y
        for character in text:
            character_surface = font.render(character, True, color)
            if blit_x + character_surface.get_rect().w >= x + w:
                blit_x = x
                blit_y += character_surface.get_rect().h
            SCREEN.blit(character_surface, (blit_x, blit_y))
            blit_x += character_surface.get_rect().w


class Button:

    def __init__(self, font_file, font_size, x, y, w, h, color=BLACK,
        bg_color=WHITE):
        self.font_file = font_file
        self.font_size = font_size
        self.x = x - w // 2
        self.y = y - h // 2
        self.w = w
        self.h = h
        self.color = color
        self.bg_color = bg_color

    def draw(self, text):
        font = pygame.font.Font(self.font_file, self.font_size)
        button_rect = self.get_rect()
        button_text_surface = font.render(text, True, self.color)
        button_text_rect = button_text_surface.get_rect(center=(self.
            x + self.w // 2, self.y + self.h // 2))
        pygame.draw.rect(SCREEN, self.bg_color, button_rect)
        SCREEN.blit(button_text_surface, button_text_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


class Map:

    def __init__(self, map_dict, map_data, tile_size):
        self.map_dict = map_dict
        self.map_data = map_data
        self.tile_size = tile_size

    def draw(self):
        i_max = len(self.map_data[0])
        j_max = len(self.map_data)
        for i in range(i_max):
            for j in range(j_max):
                try:
                    image = self.map_dict[self.map_data[i][j]]
                    SCREEN.blit(image, (j * self.tile_size, i * self.tile_size)
                        )
                except KeyError:
                    pass
