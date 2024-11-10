'''
import pygame
from pygame.locals import *
'''
import Heart

heart = Heart.Heart(60,200)

heart.heartmove()
heart.heartmove()
heart.heartscare()

print(heart.CurrentBPM)
