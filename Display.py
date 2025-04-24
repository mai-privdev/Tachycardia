#display
import pygame, sys, json
from pygame.locals import *
pygame.init()

class Display:
    def __init__(self):
        #"current_resolution" is a 0-3 value, correspondng to the index of the self.resolutions tuple
        self.current_resolution = 1
        self.game_x = 896
        self.game_y = 504
        self.menu_x = 400
        self.menu_y = 400
        self.resolutions = [(512, 288), (896, 504), (1280, 720), (1920, 1080)]
        self.active_state = ()
        self.screen = ()
        

   


    def resolution(self):
        resolution = self.resolutions[self.current_resolution]
        print(resolution)
        return(resolution)

    def change_resolution(option):
        NewRes = self.resolutions[option]
        NewRes_x, NewRes_y = NewRes

    def load(self):
        pygame.mouse.set_pos(self.game_x*0.5, self.game_y*0.5)
        self.screen = pygame.display.set_mode((self.game_x, self.game_y))
        self.active_state = 0
    
    def update(self):
        pygame.display.update()

        
        

        

    