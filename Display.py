#display
import pygame, sys, json
from pygame.locals import *
pygame.init()

class Display:
    def __init__(self, font_necropsia, font_redundead, titlefont_insomnia, default_resolution):
        with open("Assets/config/config.json", "r") as file:
            self.config = json.load(file)
        #"current_resolution" is a 0-3 value, correspondng to index of the resolutions in the config json file
        self.current_resolution = "Resolution_" + str(self.config["Resolution"])
        self.previous_resolution = self.current_resolution 
        self.resolution = self.config[(self.current_resolution)]      
        self.clock = pygame.time.Clock()
        self.current_framerate = "framerate_" + str(self.config["framerate"])
        self.framerate = self.config[(self.current_framerate)]
        self.previous_framerate = self.current_framerate
        self.game_x = self.resolution[0]
        self.game_y = self.resolution[-1]
        self.menu_x = 400
        self.menu_y = 400
        self.active_state = ()
        self.screen = ()
        self.title_font = titlefont_insomnia
        self.font_1 = font_redundead
        self.font_2 = font_necropsia
        self.bloodcolour = (115, 0, 5)
        self.heartcolour = (255, 0, 0)
        self.black = (0,0,0)
        self.heart_background = pygame.image.load("Assets/Non Map Sprites/heart_background.png")
        

    def update_resolution(self):
            self.previous_resolution = self.current_resolution

    def change_resolution(self, direction):
        #direction 0 is down, 1 is up, 2 resets to last resolution, 3 confirms and updates last resolution and 4 does nothing
        for i in direction:
            if i == 0 and self.current_resolution != "Resolution_0":
                self.current_resolution = "Resolution_" + str(int(self.current_resolution[-1])-1)
            if i == 1 and self.current_resolution != "Resolution_3":
                self.current_resolution = "Resolution_" + str(int(self.current_resolution[-1])+1)
            if i == 2:
                self.current_resolution = self.previous_resolution
            if i == 3:
                self.previous_resolution = self.current_resolution
                self.config["Resolution"] = int(self.current_resolution[-1])
                with open("Assets/config/config.json", "w") as file:
                    json.dump(self.config, file)
            if i == 4:
                pass
            self.resolution = self.config[(self.current_resolution)]
            self.game_x = self.resolution[0]
            self.game_y = self.resolution[-1]

    def update_framerate(self):
            self.previous_framerate = self.current_framerate

    def change_framerate(self, direction):
        for i in direction:
            #current framerate is an index 0-3 meaning 30,60,90,120 in that order
            #framerate are the actual values
            #previous framerate is the saved last framerate
            if i == 0 and self.current_framerate != "framerate_0":
                self.current_framerate = "framerate_" + str(int(self.current_framerate[-1])-1)
                self.framerate = self.config[(self.current_framerate)]
            if i == 1 and self.current_framerate != "framerate_3":
                self.current_framerate = "framerate_" + str(int(self.current_framerate[-1])+1)
                self.framerate = self.config[(self.current_framerate)]
            if i == 2:
                self.current_framerate = self.previous_framerate
            if i == 3:
                self.framerate = self.config[(self.current_framerate)]
                self.previous_framerate = self.current_framerate
                self.config["framerate"] = self.current_framerate[-1]
                with open("Assets/config/config.json", "w") as file:
                    json.dump(self.config, file)
            if i == 4:
                pass

    def load(self):
        pygame.mouse.set_pos(self.game_x*0.5, self.game_y*0.5)
        self.screen = pygame.display.set_mode((self.game_x, self.game_y))
        self.active_state = 0

    def update(self):
        self.screen.fill(self.black)
        pygame.display.update()

    def heart_update(self, CurrentBPM):
        self.screen.blit(self.heart_background, (self.game_x*0.1, self.game_y*0.9))
        BPM = self.font_2.render(str(CurrentBPM), True, self.bloodcolour, self.heartcolour)
        BPM_rect = BPM.get_rect()
        BPM_rect.center = (self.game_x * 0.1, self.game_y * 0.9)
        self.screen.blit(BPM, BPM_rect)
        self.clock.tick(self.framerate)

    def pause_menu(self):
        print("Paused")
        pygame.draw.rect(self.screen, (255,255,255), [self.game_x*0.25, self.game_y*0.2, self.game_x*0.5, self.game_y*0.6])
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYUP:
                print("PRESSED")
                if event.key == K_ESCAPE:
                    return(False)
        pygame.display.update()
        return(True)

        

    