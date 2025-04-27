import pygame, json

class PlayerPosition:
    def __init__(self, player_x, player_y):
        self.player = 1
        self.player_x = player_x
        self.player_y = player_y

    def move(self, direction, distance):
        #direction == 0 means x
        #direction == 1 means y
        #distance is total distance in one axis
        if direction == 0:
            self.player_x += distance
        if direction == 1:
            self.player_y += distance



#Tilemap is made of 2d arrays
class Tileset:
    def __init__(self, selected_map, resolution):
        self.resolution_x, self.resolution_y = resolution
        self.selected_map = selected_map
        with open("/Assets/maps/map_" + selected_map +".json", "r") as map_file:
            self.map = json.load(map_file)
        self.spawn_x, self.spawn_y = self.map["Spawn"]
        self.tiles = tile.load
        self.surface = pygame.Surface(self.map["width"], self.map["length"])
        self.tile_size = 16
        self.load_map
    
    def print_map(self, surface):
        surface.blit(self.surface,(int(self.resolution_x)/16*3.5,0))
    
    def load_map(self):
        for tile in self.tiles:
            tile_load(self.surface)

    def tile_load(self, file):
        tiles = []
        map = self.map
        tile_x, tile_y = 0, 0
        for row in map["data"]:
            tile_x = 0
            for tile in row:
                if tile == "0":
                    tiles.append(Tile('floor.png', tile_x * self.tile_size, tile_y * self.tile_size, self.sprite_sheet))
                if tile == "19":
                    tiles.append(Tile('wall.png',  tile_x * self.tile_size, tile_y * self.tile_size, self.sprite_sheet))
                if tile == "27":
                    tiles.append(Tile('door.png',  tile_x * self.tile_size, tile_y * self.tile_size, self.sprite_sheet))
                tile_x += 1
            tile_y += 1
        return(tiles)