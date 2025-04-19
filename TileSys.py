import pygame, sys, numpy, Tachycardia
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
        




class TileMap:
    def __init__(self, TileWidth, TileLength, Map):
        self.size = (TileWidth, TileLength)
        self.map = Map
        w, l = self.size
        TileMap = [[0]*w]*l


'''
    def render(self):
        arr[x][y] = #num of elements
'''        


