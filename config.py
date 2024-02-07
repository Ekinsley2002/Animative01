#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#set scale
SCALE = 64

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000


GREEN = (106, 229, 153)
YELLOW = (237, 208, 33)
RED = (251, 87, 60)


BATTLE_HEALTH_BAR_WIDTH = 102

MAP_TILE_GRASS = "w1ga"
MAP_TILE_GRASS2 = "g"
MAP_TILE_WATER = "W"
MAP_TILE_ROAD = "w1ra"
MAP_TILE_DOOR = "1"
MAP_TILE_DOORS = ["001", "002", "003", "004", "005", "006", "007", "008"]
MAP_TILE_GLOBAL_FLOOR_A = "grfa"
MAP_TILE_GLOBAL_WALL_A = "grwa"
MAP_TILE_ROOM_EXIT = "r1ea"
MAP_TILE_ROOM_4_EXIT_B = "r4eb"
MAP_TILE_ROOM_4_EXIT_C = "r4ec"
MAP_TILE_BUILDING = "...."
MAP_TILE_CARPET_A = "r3Ca"
MAP_TILE_ROOM_3_WALL_C = "r3wc"
MAP_TILE_ROOM_3_WALL_B = "r3wb"
MAP_TILE_ROOM_3_WALL_A = "r3wa"
MAP_TILE_ROOM_3_CORNER_B = "r3cb"
MAP_TILE_ROOM_3_CORNER_A = "r3ca"
MAP_TILE_ROOM_3_CORNER_C = "r3cc"
MAP_TILE_ROOM_3_BED_A = "r3ba"
MAP_TILE_ROOM_3_EXIT_A = "r3ea"
MAP_TILE_ROOM_3_EXIT_B = "r3eb"
MAP_TILE_ROOM_3_EXIT_C = "r3ec"
MAP_TILE_ROOM_4_EXIT_A = "r4ea"




ANIMATIVE_TYPES = ["g", "W", "S", "F"]

IMPASSIBLE = [MAP_TILE_WATER, MAP_TILE_GLOBAL_WALL_A, MAP_TILE_BUILDING, MAP_TILE_ROOM_3_BED_A, MAP_TILE_ROOM_3_BED_A, MAP_TILE_ROOM_3_WALL_B, MAP_TILE_ROOM_3_WALL_A, MAP_TILE_ROOM_3_WALL_C]


MAP_CONFIG = {
    "0001" : {
        "start_position": [1, 1],
        "exits" : [
        {
            "map" : "0002",
            "position" : [7, 0],
            "new_start_position": [7, 17],
        }],
        "buildings": [
            {
                "sprite": "04",
                "name": "Research Building",
                "position": [10, 7],
                "size" : [5, 5]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [10, 14],
                "size" : [5, 5]
            }
        ],
    },
    "0002" : {
        "start_position": [11,12],
        "exits" : [{
            "map" : "0001",
            "position" : [7, 18],
            "new_start_position" : [7, 1],
        }],

        "buildings": [
        ],
    },
    "0003": {
        "start_position": [3, 1],
        "exits": [
            {
                "map": "0002",
                "position": [3, 0],
                "new_start_position": [1, 8],
                "exit_position": [15, 16],
                "npcs": [],
            }],
        "buildings": [
        ],
    },
    "0004": {
        "start_position": [1, 1],
        "exits": [
            {
                "map": "0002",
                "position": [3, 0],
                "new_start_position": [1, 8],
                "exit_position": [15, 16],
                "npcs": [],
            }],
        "buildings": [
        ],
    },
}

ROOM_CONFIG = {
    "0001" : {
        "0001" : {
            "start_position" : [5,6],
            "exit_position" : [12,5],
            "npcs" : [
                {
                    "name" : "prof",
                    "image" : "prof",
                    "start_position" : [8,2]
                },
                {
                    "name" : "animativeF_capsul",
                    "image" : "animativeF_capsul",
                    "start_position": [10, 2]
                },
                {
                    "name" : "animativeG_capsul",
                    "image": "animativeG_capsul",
                    "start_position": [11, 2]
                },
                {
                    "name" : "animativeW_capsul",
                    "image": "animativeW_capsul",
                    "start_position": [12, 2]
                }
            ]
        },
        "0002" : {
            "start_position" : [1,1],
            "exit_position" : [12,7],
            "npcs" : [],
        },
        "0003": {
            "start_position": [1, 1],
            "exit_position": [12, 7],
            "npcs": [],
        },
        "0004": {
            "start_position": [1, 1],
            "exit_position": [12, 7],
            "npcs": [
                {
                    "name": "mom",
                    "image": "mom",
                    "start_position": [2, 2]
                },
            ],
        },

    }
}
