GameState = 1
#Gamestate = 1 means menu
#= 2 means game
#= 0 means quit


# Imported modules
import pygame, sys, numpy, json
from pygame.locals import *
pygame.init()

import Heart
import Menu
import Display
import TileSys
pygame.display.init()
pygame.font.init()




#Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
blood = (115, 0, 5)
green = (0, 255, 0)
blue = (0, 0, 128)
MenuX, MenuY= (400, 400)

#Fonts
titlefont_insomnia = pygame.font.Font('Assets/Font/Insomnia 1.ttf', 40)
font_redundead = pygame.font.Font('Assets/Font/redundead.ttf', 24)
font_necropsia = pygame.font.Font('Assets/Font/Necropsia.ttf', 28)
font_arial = pygame.font.Font()
#spritesheet = Spritesheet('')

Display = Display.Display(font_necropsia, font_redundead, titlefont_insomnia, "Resolution_1")

Menu = Menu.Menu(font_redundead, titlefont_insomnia, "Tachycardia")
Heart = Heart.Heart()
from TileSys import *

#Display

# Background clock
globalclock = pygame.time.Clock()
time = 0

#Checks
STEADY = pygame.USEREVENT + 1
HOMEOSTAIS = pygame.USEREVENT + 2

#Needed base variables
selected_map = 0
count = 0
Calm = False


#Functions

def Pause(Paused):
    while Paused == True:
        Paused = Display.pause_menu()
        print(Paused)
    else:
        return()

def Stressed(Calm):
    Calm = False
    print("calming")
    #turns off homeostasis for 5 seconds
    pygame.event.set_blocked(HOMEOSTAIS)
    pygame.time.set_timer(STEADY, 5000) #countdown til Heart begins to decrease
    return(Calm)

''' 
MAIN GAME LOOPS
'''


#Menu()
if GameState == 1:
    Menu.load()   
    while GameState == 1:
        Framerate = Display.framerate
        resolution_x, resolution_y = Display.game_x, Display.game_y
        Resolution = str(resolution_x) + " X " + str(resolution_y)
        GameState = Menu.update(Resolution, Framerate)
        if GameState != 2:
            Display.change_resolution(Menu.change_resolution)
            Display.change_framerate(Menu.change_framerate)
        selected_map = Menu.selected_map
        


#Main game code        
if GameState == 2:
    pygame.display.set_caption("Tachycardia")
    Display.load()
    #Tile_map = TileSys.Tileset(selected_map, Display.resolution) 
    Paused = False
    #if selected_map == 0:
        #Map = TileMap("/Assets/maps/map_0.json",)
    #game loop
    while GameState == 2: 
        Display.clear()
        for event in pygame.event.get(): 
            #event checkers 
            # Quit to desktop
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            # Quit to menu
            
            # Calm Cooldown
            if event.type == STEADY:
                pygame.event.set_allowed(HOMEOSTAIS)
                Calm = True
                print("Calm = true")
            #homeostasis 1 sec tick loop
            if event.type == HOMEOSTAIS:
                Heart.relax()
                print("relax")
                Calm = True
            #test scare input
            if event.type == pygame.locals.KEYUP:
                if event.key == K_ESCAPE:
                    Paused = True
                    Paused = Pause(Paused)
                    

                if event.key == K_x:
                    Heart.heartfear()
                    Stressed(Calm)    
        
        if Calm == True:
            print("timer on")
            pygame.time.set_timer(HOMEOSTAIS, 1000, 200)
            Calm = False
        

        #bugtest timer
        milli = globalclock.tick()  #clock.tick() returns how many milliseconds passed since the last time it was called
        seconds = milli/1000.
        time += seconds

        #Map.draw_map(Display.screen)
        #updates heart on hud
        Display.heart_update(Heart.CurrentBPM)        
        #screen update    
        Display.update()


if GameState == 0:
   pygame.quit()
   pygame.display.quit()
   quit()