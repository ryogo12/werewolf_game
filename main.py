import asyncio
import pygame
import sys
import random
from common import *
from title import draw_title_scene, update_title_scene
from village import draw_village_scene, update_village_scene
from player import draw_player_scene, update_player_scene
from role import draw_role_scene, update_role_scene
from villager_poll import draw_villager_poll_scene, update_villager_poll_scene
from fortune_teller_select import draw_fortune_teller_select_scene, update_fortune_teller_select_scene
from fortune_teller import draw_fortune_teller_scene, update_fortune_teller_scene
from fortune_teller_role import draw_fortune_teller_role_scene, update_fortune_teller_role_scene
from werewolf import draw_werewolf_scene, update_werewolf_scene
from dicuss import draw_discuss_scene, update_discuss_scene
from player_for_poll import draw_player_for_poll_scene, update_player_for_poll_scene
from poll import draw_poll_scene, update_poll_scene
from punishment import draw_punishment_scene, update_punishment_scene
from result import draw_result_scene
VILLAGER_DEFAULT = 2
FORTUNE_TELLER_DEFAULT = 1
WEREWOLF_DEFAULT = 2


async def main():
    pygame.init()
    pygame.display.set_caption('ワンナイト人狼')
    scene = SCENE_TITLE
    villager_count = VILLAGER_DEFAULT
    fortune_teller_count = FORTUNE_TELLER_DEFAULT
    werewolf_count = WEREWOLF_DEFAULT
    players = []
    player_index = 0
    villager_poll_index = 0
    fortune_tell_index = 0
    is_grave = False
    most_suspicious_player = []
    discuss_start_time = 0
    player_index_for_poll = 0
    poll_index = 0
    poll_result = []
    werewolf_is_winner = True
    while True:
        await asyncio.sleep(0)
        if scene < SCENE_DISCUSS:
            SCREEN.fill(BLUE_STRONG)
            map_data = MAP_DATA_NIGHT
        else:
            SCREEN.fill(BLUE_LIGHT)
            map_data = MAP_DATA_DAY
        map = Map(MAP_DICT, map_data, 32)
        map.draw()
        SCREEN.blit(LAYER, (0, 0))
        if scene == SCENE_TITLE:
            await draw_title_scene()
        elif scene == SCENE_VILLAGE:
            await draw_village_scene(villager_count=villager_count,
                fortune_teller_count=fortune_teller_count, werewolf_count=
                werewolf_count)
        elif scene == SCENE_PLAYER:
            if player_index < len(players) - 2:
                await draw_player_scene(player=players[player_index])
            else:
                villager_poll = sorted(players[:-2], key=lambda p: p[
                    'villager_poll_count'], reverse=True)
                for i in range(len(villager_poll)):
                    if i == 0 or villager_poll[i - 1]['villager_poll_count'
                        ] == villager_poll[i]['villager_poll_count']:
                        most_suspicious_player.append(villager_poll[i])
                    else:
                        break
                discuss_start_time = pygame.time.get_ticks()
                scene = SCENE_DISCUSS
        elif scene == SCENE_ROLE:
            await draw_role_scene(player=players[player_index])
        elif scene == SCENE_VILLAGER_POLL:
            await draw_villager_poll_scene(villager_poll_index=
                villager_poll_index)
        elif scene == SCENE_FORTUNE_TELLER_SELECT:
            await draw_fortune_teller_select_scene()
        elif scene == SCENE_FORTUNE_TELLER:
            await draw_fortune_teller_scene(fortune_tell_index)
        elif scene == SCENE_FORTUNE_TELLER_ROLE:
            await draw_fortune_teller_role_scene(players,
                fortune_tell_index, is_grave)
        elif scene == SCENE_WEREWOLF:
            await draw_werewolf_scene(players)
        elif scene == SCENE_DISCUSS:
            scene = await draw_discuss_scene(discuss_start_time,
                most_suspicious_player)
        elif scene == SCENE_PLAYER_FOR_POLL:
            if player_index_for_poll < len(players) - 2:
                await draw_player_for_poll_scene(player=players[
                    player_index_for_poll])
            else:
                poll = sorted(players[:-2], key=lambda p: p['poll_count'],
                    reverse=True)
                for i in range(len(poll)):
                    if i == 0 or poll[i - 1]['poll_count'] == poll[i][
                        'poll_count']:
                        poll_result.append(poll[i])
                        if poll[i]['role'] == '人狼':
                            werewolf_is_winner = False
                    else:
                        break
                if len(poll_result) == len(poll):
                    poll_result = ['平和村']
                    for p in poll:
                        if p['role'] == '人狼':
                            werewolf_is_winner = True
                            break
                        else:
                            werewolf_is_winner = False
                scene = SCENE_PUNISHMENT
        elif scene == SCENE_POLL:
            await draw_poll_scene(poll_index, players[player_index_for_poll])
        elif scene == SCENE_PUNISHMENT:
            await draw_punishment_scene(poll_result)
        elif scene == SCENE_RESULT:
            await draw_result_scene(werewolf_is_winner)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scene == SCENE_TITLE:
                    scene = await update_title_scene()
                elif scene == SCENE_VILLAGE:
                    (scene, villager_count, fortune_teller_count,
                        werewolf_count, players) = (await
                        update_village_scene(villager_count=villager_count,
                        fortune_teller_count=fortune_teller_count,
                        werewolf_count=werewolf_count, players=players))
                elif scene == SCENE_PLAYER:
                    scene = await update_player_scene()
                elif scene == SCENE_ROLE:
                    scene = await update_role_scene(player=players[
                        player_index])
                elif scene == SCENE_VILLAGER_POLL:
                    scene, player_index, villager_poll_index, players = (await
                        update_villager_poll_scene(player_index=
                        player_index, villager_poll_index=
                        villager_poll_index, villager_poll_index_max=
                        players.index(players[-1]) - 2, players=players))
                elif scene == SCENE_FORTUNE_TELLER_SELECT:
                    scene, is_grave = await update_fortune_teller_select_scene(
                        is_grave)
                elif scene == SCENE_FORTUNE_TELLER:
                    scene, fortune_tell_index = (await
                        update_fortune_teller_scene(fortune_tell_index=
                        fortune_tell_index, fortune_tell_index_max=players.
                        index(players[-1]) - 2))
                elif scene == SCENE_FORTUNE_TELLER_ROLE:
                    scene, player_index = (await
                        update_fortune_teller_role_scene(player_index))
                elif scene == SCENE_WEREWOLF:
                    scene, player_index = await update_werewolf_scene(
                        player_index)
                elif scene == SCENE_DISCUSS:
                    scene = await update_discuss_scene()
                elif scene == SCENE_PLAYER_FOR_POLL:
                    poll_index = 0
                    scene = await update_player_for_poll_scene()
                elif scene == SCENE_POLL:
                    scene, player_index_for_poll, poll_index, players = (await
                        update_poll_scene(player_index_for_poll=
                        player_index_for_poll, poll_index=poll_index,
                        poll_index_max=players.index(players[-1]) - 2,
                        players=players))
                elif scene == SCENE_PUNISHMENT:
                    scene = await update_punishment_scene()
        pygame.display.update()


if __name__ == '__main__':
    asyncio.run(main())
