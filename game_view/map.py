import pygame
import config
import math
import utilities
from npc import Npc
from building import Building

class Map():
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]
        self.file_name = None
        self.player_exit_position = [1, 1]
        self.objects = []
        self.exit_positions = []

    def load(self, file_name, player):
        self.file_name = file_name
        self.player = player
        self.objects = [player]

        with open("maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []

                for i in range(0, len(line), 5):  # Change the range step to 3 to read three characters at a time
                    tiles.append(line[i:i + 4])
                self.map_array.append(tiles)
            print(self.map_array)

        map_config = config.MAP_CONFIG[file_name]

        player.position = map_config['start_position'][:]

        for building_data in map_config["buildings"]:
            building = Building(building_data["sprite"], building_data["position"], building_data["size"])
            self.objects.append(building)

        for exit_position in map_config['exits']:
            self.exit_positions.append(exit_position)



    def load_room(self, map_name, room_name, player):
        self.player = player
        self.objects = [player]

        room_config = config.ROOM_CONFIG[map_name][str(room_name).zfill(2)]
        self.player.position = room_config['start_position'][:]
        self.player.player_exit_position = room_config['exit_position'][:]
        self.player_exit_position = room_config['exit_position'][:]

        #Draw Npc
        for npc_data in room_config['npcs']:
            npc = Npc(npc_data['name'], npc_data['image'], npc_data['start_position'][0], npc_data['start_position'][1])
            self.objects.append(npc)

        with open("rooms/" + str(room_name).zfill(2) + ".txt") as room_file:
            for line in room_file:
                tiles = []

                for i in range(0, len(line), 5):  # Change 2 to 4 to read four characters at a time
                    tiles.append(line[i:i + 4])
                self.map_array.append(tiles)
            print(self.map_array)
        pass






    def render(self, screen, player):
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                if tile not in map_tile_image:
                    x_pos = x_pos + 1
                    continue
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE), y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1
            y_pos = y_pos + 1

        #Draw all objects on map
        for object in self.objects:
            object.render(self.screen, self.camera)

    def determine_camera(self, player):
        max_y_position = len(self.map_array) - config.SCREEN_HEIGHT / config.SCALE
        y_position = player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))
        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

        max_x_position = len(self.map_array[0]) - config.SCREEN_WIDTH / config.SCALE
        x_position = player.position[0] - math.ceil(round(config.SCREEN_WIDTH/ config.SCALE / 2))
        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position




map_tile_image = {
    config.MAP_TILE_GRASS: pygame.transform.scale(pygame.image.load("images/map1/grass1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_GRASS2: pygame.transform.scale(pygame.image.load("images/map1/grass2.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER: pygame.transform.scale(pygame.image.load("images/map1/water.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD: pygame.transform.scale(pygame.image.load("images/map1/road.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_GLOBAL_FLOOR_A: pygame.transform.scale(pygame.image.load("images/rooms/lab_floor.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_EXIT: pygame.transform.scale(pygame.image.load("images/rooms/lab_exit.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_GLOBAL_WALL_A: pygame.transform.scale(pygame.image.load("images/rooms/lab_wall.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_CARPET_A: pygame.transform.scale(pygame.image.load("images/carpet.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_WALL_C: pygame.transform.scale(pygame.image.load("images/room_B_wall.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_WALL_A: pygame.transform.scale(pygame.image.load("images/room_T_wall.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_WALL_B: pygame.transform.scale(pygame.image.load("images/room_L_wall.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_CORNER_C: pygame.transform.scale(pygame.image.load("images/room_L_corner.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_CORNER_A: pygame.transform.scale(pygame.image.load("images/room_LT_corner.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_CORNER_B: pygame.transform.scale(pygame.image.load("images/room_RT_corner.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_BED_A: pygame.transform.scale(pygame.image.load("images/room_bed.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_EXIT_A: pygame.transform.scale(pygame.image.load("images/stairs_down1.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_EXIT_B: pygame.transform.scale(pygame.image.load("images/stairs_down2.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_3_EXIT_C: pygame.transform.scale(pygame.image.load("images/stairs_down3.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_4_EXIT_A: pygame.transform.scale(pygame.image.load("images/stairs_up1.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_4_EXIT_B: pygame.transform.scale(pygame.image.load("images/door.png"),(config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_4_EXIT_C: pygame.transform.scale(pygame.image.load("images/door1.png"),(config.SCALE, config.SCALE)),
}




