#Menu
import pygame, sys, json
from pygame.locals import *
pygame.init()

class Menu:
    def __init__(self, font, titlefont, title):
        import Display
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
        #Menu state
        #0 = Main menu
        #1 = Level Menu
        #2 = Settings Menu
        self.MenuState = ()
        self.selected_map = 0
        self.change_resolution = []
        self.change_framerate = []
         
    def load(self):
        pygame.mouse.set_pos(self.width*0.5, self.height*0.5)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.MenuState = 0
        #screen is 400x400
        
    def buttonhighlight(self):
        #Buttonhighlightcount values 
        #0 = 0.4 highlight top
        #1 = 0.4 unhighlight top
        #2 = 0.6 highlight middle
        #3 = 0.6 unhighlight middle
        #4 = 0.8 highlight bottom
        #5 = 0.8 unhighlight bottom
        #6 = 0.4 highlight top left 
        #7 = 0.4 unhighlight top left
        #8 = 0.4 highlight top right
        #9 = 0.4 unhighlight top right
        #10 = 0.6 highlight top left 
        #11 = 0.6 unhighlight top left
        #12 = 0.6 highlight top right
        #13 = 0.6 unhighlight top right
        Value = self.buttonhighlighcount
        for i in Value:
            #if odd
            if (i + 1)%2 == 0:
                if self.MenuState == 2:
                    if (6 <= i < 8):
                        pygame.draw.polygon(self.screen, self.buttoncolour, ([self.width*0.1, self.height*0.45], [self.width*0.2, self.height*0.4], [self.width*0.2, self.height*0.5]))
                    if (8 <= i < 10):
                        pygame.draw.polygon(self.screen, self.buttoncolour, ([self.width*0.8, self.height*0.4], [self.width*0.9, self.height*0.45], [self.width*0.8, self.height*0.5]))
                    if (10 <= i < 12):
                        pygame.draw.polygon(self.screen, self.buttoncolour, ([self.width*0.1, self.height*0.65], [self.width*0.2, self.height*0.6], [self.width*0.2, self.height*0.7]))  
                    if (12 <= i < 14):
                        pygame.draw.polygon(self.screen, self.buttoncolour, ([self.width*0.8, self.height*0.6], [self.width*0.9, self.height*0.65], [self.width*0.8, self.height*0.7]))
                              
                pygame.draw.rect(self.screen,self.buttoncolour,[self.width*0.25,self.height*(0.4+((i-1)*0.1)),200,40])
            #if even
            elif (i)%2 == 0:
                if self.MenuState == 2:
                    if (6 <= i < 8):
                        pygame.draw.polygon(self.screen, self.highlightcolour, ([self.width*0.1, self.height*0.45], [self.width*0.2, self.height*0.4], [self.width*0.2, self.height*0.5]))                        
                    if (8 <= i <10):
                        pygame.draw.polygon(self.screen, self.highlightcolour, ([self.width*0.8, self.height*0.4], [self.width*0.9, self.height*0.45], [self.width*0.8, self.height*0.5]))                       
                    if (10 <= i < 12):
                        pygame.draw.polygon(self.screen, self.highlightcolour, ([self.width*0.1, self.height*0.65], [self.width*0.2, self.height*0.6], [self.width*0.2, self.height*0.7]))  
                    if (12 <= i < 14):
                        pygame.draw.polygon(self.screen, self.highlightcolour, ([self.width*0.8, self.height*0.6], [self.width*0.9, self.height*0.65], [self.width*0.8, self.height*0.7]))
                    
                pygame.draw.rect(self.screen,self.highlightcolour,[self.width*0.25,self.height*(0.4+(i*0.1)),200,40])        

        self.buttonhighlighcount.clear()       
        return(self.buttonhighlighcount)
    
    def update(self, current_resolution, current_framerate):
        #clears previous cycle
        self.change_resolution.clear()
        self.change_framerate.clear()
        self.screen.fill(self.Black)
        mouse = pygame.mouse.get_pos()
        #Main Menu
        if self.MenuState == 0:
            self.confirm_resolution = False
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
            #Button commands              
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.width*0.25 <= mouse[0] <= self.width*0.75:
                                #Level Select
                            if self.height*0.4 <= mouse[1] <= self.height*0.5:
                                self.MenuState = 1
                                #Options
                            if self.height*0.6 <= mouse[1] <= self.height*0.7:
                                self.MenuState = 2
                                #Quit
                            if self.height*0.8 <= mouse[1] <= self.height*0.9:
                                return(0)              
            #Text
            #Title
            self.screen.blit(self.titlefont.render(self.title, True, self.Red), (self.width*0.1, self.height*0.15))
            #start/levels
            self.screen.blit(self.font.render("Start", True, self.Black) , (self.width*0.25,self.height*0.4))
            #Options
            self.screen.blit(self.font.render("Options", True, self.Black) , (self.width*0.25,self.height*0.6))
            #Quit
            self.screen.blit(self.font.render("Quit", True, self.Black) , (self.width*0.25,self.height*0.8))

        #Levels Menu
        if self.MenuState == 1:
            self.screen.fill(self.Black)
             
            if (self.width*0.25 <= mouse[0] <= self.width*0.75) and (self.height*0.4 <= mouse[1] <= self.height*0.9):
                if self.height*0.4 <= mouse[1] <= self.height*0.5:
                    self.buttonhighlighcount.append(0)
                else:
                    self.buttonhighlighcount.append(1)

                if self.height*0.8 <= mouse[1] <= self.height*0.9:
                    self.buttonhighlighcount.append(4)
                else:
                    self.buttonhighlighcount.append(5)    
            else:
                self.buttonhighlighcount.append(1)
                self.buttonhighlighcount.append(5)
            self.buttonhighlighcount.append(3)
            
            
            Menu.buttonhighlight(self)
            #Button commands             
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.width*0.25 <= mouse[0] <= self.width*0.75:
                            #lvl 1
                            if self.height*0.4 <= mouse[1] <= self.height*0.5:
                                self.selected_map = 0
                                return(2)
                            #Lvl 2 (Doesnt exist)
                            if self.height*0.6 <= mouse[1] <= self.height*0.7:
                                pass
                            #return
                            if self.height*0.8 <= mouse[1] <= self.height*0.9:
                                self.MenuState = 0

                            
            #Text
            #Title
            self.screen.blit(self.titlefont.render("Level Select", True, self.Red), (self.width*0.12, self.height*0.15))
            #level 1
            self.screen.blit(self.font.render("Level I", True, self.Black) , (self.width*0.25,self.height*0.4))
            #level 2 (not made)
            self.screen.blit(self.font.render("LOCKED", True, self.Black) , (self.width*0.25,self.height*0.6))
            #return
            self.screen.blit(self.font.render("Return", True, self.Black) , (self.width*0.25,self.height*0.8))
            
        #Options Menu
        if self.MenuState == 2:
            self.screen.fill(self.Black)
            #if inside the center buttons
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
                self.buttonhighlighcount.append(7)
                self.buttonhighlighcount.append(9)
                self.buttonhighlighcount.append(11)
                self.buttonhighlighcount.append(13)      
            #if inside the top side buttons    
            elif (self.height*0.4 <= mouse[1] <= self.height*0.5):
                if self.width*0.1 <= mouse[0] <= self.width*0.2:
                    self.buttonhighlighcount.append(6)
                else:
                    self.buttonhighlighcount.append(7)
                if self.width*0.8 <= mouse[0] <= self.width*0.9:
                    self.buttonhighlighcount.append(8)
                else:
                    self.buttonhighlighcount.append(9)
                #I HATE .APPEND WHY CANT I APPEND AS A LIST STUPID PYTHJON
                self.buttonhighlighcount.append(1)
                self.buttonhighlighcount.append(3)
                self.buttonhighlighcount.append(5)
                self.buttonhighlighcount.append(11)
                self.buttonhighlighcount.append(13)
            #if inside the middle side buttons
            elif (self.height*0.6 <= mouse[1] <= self.height*0.7):
                if self.width*0.1 <= mouse[0] <= self.width*0.2:
                    self.buttonhighlighcount.append(10)
                else:
                    self.buttonhighlighcount.append(11)
                if self.width*0.8 <= mouse[0] <= self.width*0.9:
                    self.buttonhighlighcount.append(12)
                else:
                    self.buttonhighlighcount.append(13)
                self.buttonhighlighcount.append(1)
                self.buttonhighlighcount.append(3)
                self.buttonhighlighcount.append(5)
                self.buttonhighlighcount.append(7)
                self.buttonhighlighcount.append(9)
            else:
                self.buttonhighlighcount.append(1)
                self.buttonhighlighcount.append(3)
                self.buttonhighlighcount.append(5)
                self.buttonhighlighcount.append(7)
                self.buttonhighlighcount.append(9)
                self.buttonhighlighcount.append(11)
                self.buttonhighlighcount.append(13)
            Menu.buttonhighlight(self)
            #Button commands                
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #centre buttons
                        if self.width*0.25 <= mouse[0] <= self.width*0.75:
                            #Resolution confirm
                            if self.height*0.4 <= mouse[1] <= self.height*0.5:
                                self.change_resolution.clear()
                                self.change_resolution.append(3)
                            #framerate confirm
                            if self.height*0.6 <= mouse[1] <= self.height*0.7:
                                self.change_framerate.clear()
                                self.change_framerate.append(3)
                                print("confirm")
                            #return
                            if self.height*0.8 <= mouse[1] <= self.height*0.9:
                                self.change_resolution.clear()
                                self.change_resolution.append(2)
                                self.MenuState = 0
                        #upper side buttons
                        elif (self.height*0.4 <= mouse[1] <= self.height*0.5):
                            if self.width*0.1 <= mouse[0] <= self.width*0.2:
                                self.change_resolution.clear()
                                self.change_resolution.append(0)
                            if self.width*0.8 <= mouse[0] <= self.width*0.9:
                                self.change_resolution.clear()
                                self.change_resolution.append(1)
                        #middle side buttons
                        elif (self.height*0.6 <= mouse[1] <= self.height*0.7):
                            if self.width*0.1 <= mouse[0] <= self.width*0.2:
                                self.change_framerate.clear()
                                self.change_framerate.append(0)
                                print("-1")
                            if self.width*0.8 <= mouse[0] <= self.width*0.9:
                                self.change_framerate.clear()
                                self.change_framerate.append(1)
                                print("+1")                            
            #Text 
            #Title
            self.screen.blit(self.titlefont.render("Settings", True, self.Red), (self.width*0.23, self.height*0.15))
            #Resolution select
            self.screen.blit(self.font.render("Resolution", True, self.white) , (self.width*0.25,self.height*0.32))
            self.screen.blit(self.font.render((current_resolution), True, self.Black) , (self.width*0.25,self.height*0.4))
            #Framerate select
            self.screen.blit(self.font.render("Framerate (FPS)", True, self.white) , (self.width*0.25,self.height*0.52))
            self.screen.blit(self.font.render(str(current_framerate), True, self.Black) , (self.width*0.25,self.height*0.6))
            #Return
            self.screen.blit(self.font.render("Return", True, self.Black) , (self.width*0.25,self.height*0.8))
        
        self.change_framerate.append(4)
        self.change_resolution.append(4)
        pygame.display.update()
        return(1)     