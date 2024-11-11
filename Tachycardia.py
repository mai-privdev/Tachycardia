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
green = (0, 255, 0)
blue = (0, 0, 128)
#Display
X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
 
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font('freesansbold.ttf', 32)


 
# set the center of the rectangular object.

# Background clock
globalclock = pygame.time.Clock()
time = 0

#Checks
REST = pygame.USEREVENT + 1
CHECK2 = False

#Timers
pygame.time.set_timer(REST, 100) #tick between 

bpmraised = False
count = 0
while True:
    #event checkers
    for event in pygame.event.get():   
        if event.type == pygame.quit:
            pygame.quit()
            quit()
        if event.type == REST:
            count += 1
            print(count)
            print(round(time, 5))

    if bpmraised == True:
        count = 0        
    if count == 10:
        heart.relax()
        count = 0
        print(heart.CurrentBPM)

    #display
    

    #bugtest timer
    milli = globalclock.tick()  #clock.tick() returns how many milliseconds passed since the last time it was called
    seconds = milli/1000.
    time += seconds
    #print(round(time, 5))

    #updates heartrate
    text = font.render(str(heart.CurrentBPM), True, red, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    #display
    display_surface.blit(text, textRect)
    #screen update
    pygame.display.update()
    


    
        