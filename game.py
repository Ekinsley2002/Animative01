import configanimative
from events import game_event_handler
from player import Player
import pygame
import math
from game_state import GameState, CurrentGameState
import config
import utilities
from animative_factory import AnimativeFactory
from game_view.map import Map
from game_view.battle import Battle
from events import game_event_handler

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.animative_factory = AnimativeFactory
        self.map = Map(screen)
        self.battle = None
        self.maps = [self.map]
        self.player = None
        self.event = None
        room = Map(self.screen)
    def set_up(self):
        player = Player(3, 5)
        self.player = player
        print("Do set up")
        self.game_state = GameState.RUNNING
        self.map.load_room("0001", "0003", self.player)
    def update(self):

        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False

            self.screen.fill(config.BLACK)

            self.handle_events()

            if self.player_has_moved:
                self.determine_game_events()

            self.map.render(self.screen, self.player)



        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()

            if self.battle.animative.health <= 0:
                self.current_game_state = CurrentGameState.MAP

        if self.event is not None:
            self.event.render()
            self.event.update()


    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROOM_EXIT:
            self.player.position = self.map.player_exit_position[:]
            map_file = ("0001")
            map = Map(self.screen)
            config.MAP_CONFIG[map_file]["start_position"] = [12, 12]
            map.load(map_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return
        if map_tile == config.MAP_TILE_ROOM_4_EXIT_B:
            self.player.position = self.map.player_exit_position[:]
            map_file = ("0001")
            map = Map(self.screen)
            config.MAP_CONFIG[map_file]["start_position"] = [12, 19]
            map.load(map_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return

        if map_tile == config.MAP_TILE_ROOM_4_EXIT_C:
            self.player.position = self.map.player_exit_position[:]
            map_file = ("0001")
            map = Map(self.screen)
            config.MAP_CONFIG[map_file]["start_position"] = [12, 19]
            map.load(map_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return


        if map_tile == config.MAP_TILE_ROOM_3_EXIT_A:
            room_file = ("0004")
            map_file = ("0001")

            map = Map(self.screen)
            config.ROOM_CONFIG[map_file][room_file]["start_position"] = [6, 1]
            map.load_room(map_file, room_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return



        if map_tile == config.MAP_TILE_ROOM_3_EXIT_B:
            room_file = ("0004")
            map_file = ("0001")

            map = Map(self.screen)
            config.ROOM_CONFIG[map_file][room_file]["start_position"] = [6, 1]
            map.load_room(map_file, room_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return

        if map_tile == config.MAP_TILE_ROOM_3_EXIT_C:
            room_file = ("0004")
            map_file = ("0001")

            map = Map(self.screen)
            config.ROOM_CONFIG[map_file][room_file]["start_position"] = [6, 1]
            map.load_room(map_file, room_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return

        if map_tile == config.MAP_TILE_ROOM_4_EXIT_A:
            room_file = ("0003")
            map_file = ("0001")

            map = Map(self.screen)
            config.ROOM_CONFIG[map_file][room_file]["start_position"] = [7, 1]
            map.load_room(map_file, room_file, self.player)
            self.maps.pop()
            self.map = map
            self.maps.append(map)
            return




        #Check to see if the map tile is a door, we need a room
        if utilities.test_if_int(map_tile):
            room = Map(self.screen)
            room.load_room(self.map.file_name, map_tile, self.player)
            self.map = room
            self.maps.append(room)
            return

        for npc in self.map.objects:
            if npc == self.map.player:
                continue

            if npc.position[:] == self.map.player.position[:]:
                game_event_handler.handle(self, self.player, npc)


        #Going to a new map
        for exit_position in self.map.exit_positions:
            if self.player.position == exit_position['position'][:]:
                map_file = exit_position['map']
                map = Map(self.screen)
                config.MAP_CONFIG[map_file]['start_position'] = exit_position['new_start_position'][:]
                map.load(map_file, self.player)
                self.maps.pop()
                self.map = map
                self.maps.append(map)



        if self.player.animatives:
            self.determine_animative_found(map_tile)

    def determine_animative_found(self, map_tile):
        random_number = utilities.generate_random_number(1, 10)
        if map_tile not in config.ANIMATIVE_TYPES:
            return

        #Give a certain animative a 20% chance of spawning
        if random_number <= 2:
            found_animative = self.animative_factory.create_animative(self, map_tile)
            print("you found an animative!")
            print("Animative type:" + found_animative.type)
            print("attack:" + str(found_animative.attack))
            print("health:" + str(found_animative.health))

            self.battle = Battle(self.screen, found_animative, self.player)
            self.current_game_state = CurrentGameState.BATTLE

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
                #handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.NONE
                elif event.key == pygame.K_w: #Up
                    self.move_unit(self.player, [0,-1])
                elif event.key == pygame.K_s: #down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: #left
                    self.move_unit(self.player, [-1, 0])
                    self.player.image = pygame.image.load("images/playerLeft.png")
                    self.player.image = pygame.transform.scale(self.player.image, (config.SCALE, config.SCALE))
                elif event.key == pygame.K_d: #right
                    self.move_unit(self.player, [1, 0])
                    self.player.image = pygame.image.load("images/playerRight.png")
                    self.player.image = pygame.transform.scale(self.player.image, (config.SCALE, config.SCALE))
                elif event.key == pygame.K_UP: #Up
                    self.move_unit(self.player, [0, -10])
                elif event.key == pygame.K_DOWN: #down
                    self.move_unit(self.player, [0, 10])
                elif event.key == pygame.K_LEFT: #left
                    self.move_unit(self.player, [-10, 0])
                elif event.key == pygame.K_RIGHT: #right
                    self.move_unit(self.player, [10, 0])


#Check to see if the player is off map
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        #Check for valid movement
        if self.map.map_array[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return
        self.player_has_moved = True
        unit.update_position(new_position)










