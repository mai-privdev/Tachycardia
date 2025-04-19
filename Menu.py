import pygame, sys, numpy, Tachycardia
from pygame.locals import *
pygame.init()

class Menu:
    def __init__(self, font, titlefont, title):
        self.width = 400
        self.height = 400
        self.font = font
        self.titlefont = titlefont
        self.title = title
        self.white = (255, 255, 255)
        self.Black = (0,0,0)
        self.Red = (255,0,0)
        self.mouse = []
        self.highlightcolour = (175, 0, 0)
        self.buttoncolour = (120, 0 , 0)
        self.buttonhighlighcount = []
        
    
    def load(self):
        
        pygame.mouse.set_pos(self.width*0.5, self.height*0.5)
        self.screen = pygame.display.set_mode((self.width, self.height))
        #screen is 400x400
        

    def buttonhighlight(self):
        
        Value = self.buttonhighlighcount
        #print(Value)
        for i in Value:
            
            #if odd
            if (i + 1)%2 == 0:
                pygame.draw.rect(self.screen,self.buttoncolour,[self.width*0.25,self.height*(0.4+((i-1)*0.1)),200,40])
             
            #if even
            elif (i)%2 == 0:
                pygame.draw.rect(self.screen,self.highlightcolour,[self.width*0.25,self.height*(0.4+(i*0.1)),200,40])
                

            
        self.buttonhighlighcount.clear()       
        return(self.buttonhighlighcount)
    

    
    def update(self):
        #Title
        self.screen.blit(self.titlefont.render(self.title, True, self.Red), (self.width*0.1, self.height*0.15))
        #start/levels
        self.screen.blit(self.font.render("Start", True, self.white) , (self.width*0.25,self.height*0.4))
        #Options
        self.screen.blit(self.font.render("Options", True, self.white) , (self.width*0.25,self.height*0.6))
        #Quit
        self.screen.blit(self.font.render("Quit", True, self.white) , (self.width*0.25,self.height*0.8))

        mouse = pygame.mouse.get_pos()

        if (self.width*0.25 <= mouse[0] <= self.width*0.75) and (self.height*0.4 <= mouse[1] <= self.height*0.9):
            if self.height*0.4 <= mouse[1] <= self.height*0.5:
                self.buttonhighlighcount.append(0)
            else:
                self.buttonhighlighcount.append(1)
            if self.height*0.6 <= mouse[1] <= self.height*0.7:
                self.buttonhighlighcount.append(2)
            else:
                self.buttonhighlighcount.append(3)    
            if self.height*0.8 <= mouse[1] <= self.height*0.9:
                self.buttonhighlighcount.append(4)
            else:
                self.buttonhighlighcount.append(5)
        

        else:
            self.buttonhighlighcount.append(1)
            self.buttonhighlighcount.append(3)
            self.buttonhighlighcount.append(5)
        
        Menu.buttonhighlight(self)
                         
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                   #start
                    if self.height*0.4 <= mouse[1] <= self.height*0.5:
                        print("click 1")
                        GameState = 2
                        return(1)
                         #Options
                         
                    if self.height*0.6 <= mouse[1] <= self.height*0.7:
                        print("click 2")
                        #WIP

                        #Quit
                    if self.height*0.8 <= mouse[1] <= self.height*0.9:
                        print("Click 3")
                        GameState = 0
                        return(0)

                        

        #Title
        self.screen.blit(self.titlefont.render(self.title, True, self.Red), (self.width*0.1, self.height*0.15))
        #start/levels
        self.screen.blit(self.font.render("Start", True, self.Black) , (self.width*0.25,self.height*0.4))
        #Options
        self.screen.blit(self.font.render("Options", True, self.Black) , (self.width*0.25,self.height*0.6))
        #Quit
        self.screen.blit(self.font.render("Quit", True, self.Black) , (self.width*0.25,self.height*0.8))
        
        pygame.display.update()
        return(True)
    #Value 
    #
    #0 = 0.4 highlight
    #1 = 0.4 
    #2 = 0.6 highlight
    #3 = 0.6 
    #4 = 0.8 highlight
    #5 = 0.8 

    


                
                