import pygame, sys, numpy, json
from pygame.locals import *
pygame.init()

class Tileset:
    def __init__(self):
        self.math
#Tilemap is made of 2d arrays
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


class Tile:
    def __init__(self, texture, tile_x, tile_y, sprite_sheet):
        self.image = pygame.image.load(image) 
        self.sprite = self.image.get_rect()
        self.sprite_x, self.sprite_y = tile_x, tile_y

    def load(self, surface):
        surface.blit(self.image, (self.sprite_x, self.sprite_y))


class TileMap():
    def __init__(self, filename, sprite_sheet, selected_map):
        with open("Assets/maps/map_"+ str(selected_map) +".json", "r") as map_file:
            self.map = json.load(map_file)
        self.spawn_x, self.spawn_y = self.map["spawn"]
        self.sprite_sheet = sprite_sheet
        self.tiles = self.tile_load(filename)
        self.map_surface = pygame.Surface((self.map["width"], self.map["height"]))
        self.map_surface.set_colorkey((0, 0, 0))
        self.tile_size = 16 #16x16 squares
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile_load(self.map_surface)

    def tile_load(self, file):
        tiles = []
        map = self.map
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(Tile('grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('grass2.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles



