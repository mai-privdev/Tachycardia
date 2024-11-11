# Imported modules
import pygame, sys
from pygame.locals import *
pygame.init()
#
import Heart

heart = Heart.Heart(60,200)
#Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
blood = (115, 0, 5)
green = (0, 255, 0)
blue = (0, 0, 128)
#Display
X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
 
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font('/home/mai/Documents/Lessons/Computer Science Lessons/Lesson scripts/Project/Font/Necropsia.ttf', 32)


 
# set the center of the rectangular object.

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
    pygame.time.set_timer(STEADY, 5000) #countdown til heart begins to decrease
    return(Calm)




while True:
    for event in pygame.event.get(): 
        #event checkers 
        # Quit 
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        # Calm Cooldown
        if event.type == STEADY:
            Calm = True
            print("Calm = true")
        if event.type == HOMEOSTAIS:
            heart.relax()
            print("relax")
            Calm = True
        # Test 
        if event.type == pygame.locals.KEYUP:
            if event.key == K_x:
                heart.heartfear()
                Stressed(Calm)
    
    if Calm == True:
        print("timer on")
        pygame.time.set_timer(HOMEOSTAIS, 1000)
        Calm = False        
    

    #bugtest timer
    milli = globalclock.tick()  #clock.tick() returns how many milliseconds passed since the last time it was called
    seconds = milli/1000.
    time += seconds
    #print(round(time, 5))

    #updates heartrate
    text = font.render(str(heart.CurrentBPM), True, blood, red)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    #display
    display_surface.blit(text, textRect)
    #screen update
    pygame.display.update()


