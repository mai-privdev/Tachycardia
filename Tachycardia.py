
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
pygame.display.init()
pygame.font.init()
#import TileSys


#Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
blood = (115, 0, 5)
green = (0, 255, 0)
blue = (0, 0, 128)
MenuX, MenuY= (400, 400)

#Fonts
titlefont_insomnia = pygame.font.Font('/home/mai/Documents/A level/Lessons/Computer Science Lessons/Lesson scripts/Project/Assets/Font/Insomnia 1.ttf', 40)
font_insomnia = pygame.font.Font('/home/mai/Documents/A level/Lessons/Computer Science Lessons/Lesson scripts/Project/Assets/Font/Insomnia 1.ttf', 32)
font_necropsia = pygame.font.Font('/home/mai/Documents/A level/Lessons/Computer Science Lessons/Lesson scripts/Project/Assets/Font/Necropsia.ttf', 32)

Menu = Menu.Menu(font_insomnia, titlefont_insomnia, "Tachycardia")
#heart = Heart.Heart(60,200)
Display = Display.Display()

#Display




 
# Background clock
globalclock = pygame.time.Clock()
time = 0

#Checks
STEADY = pygame.USEREVENT + 1
HOMEOSTAIS = pygame.USEREVENT + 2

#Needed base variables
count = 0
Calm = False


#Functions


def Stressed(Calm):
    Calm = False
    print("calming")
    #turns off homeostasis for 5 seconds
    pygame.event.set_blocked(HOMEOSTAIS)
    pygame.time.set_timer(STEADY, 5000) #countdown til heart begins to decrease
    return(Calm)

''' 
MAIN GAME LOOPS
'''


#Menu()
if GameState == 1:
    Menu.load()   
    while GameState == 1:
        GameState = Menu.update()
    print(GameState)

        


#Main game code        
if GameState == 2:
    while GameState == 2:  
        print("BOOBS")
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
                heart.relax()
                print("relax")
                Calm = True
            #test scare input
            if event.type == pygame.locals.KEYUP:
                if event.key == K_x:
                    heart.heartfear()
                    Stressed(Calm)    
        
        if Calm == True:
            print("timer on")
            pygame.time.set_timer(HOMEOSTAIS, 1000, 200)
            Calm = False
        

        #bugtest timer
        milli = globalclock.tick()  #clock.tick() returns how many milliseconds passed since the last time it was called
        seconds = milli/1000.
        time += seconds
        #print(round(time, 5))

        #updates heartrate
        heart.update()
        #display
        game_screen.blit(text, textRect)
        #screen update
        pygame.display.update()


if GameState == 0:
   pygame.quit()
   pygame.display.quit()
   quit()