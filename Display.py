#display
class Display:
    def __init__(self):
        #"current_resolution" is a 0-3 value, correspondng to the index of the self.resolutions tuple
        self.current_resolution = 1
        self.game_x = 896
        self.game_y = 504
        self.menu_x = 400
        self.menu_y = 400
        self.resolutions = [(512, 288), (896, 504), (1280, 720), (1920, 1080)]
        

   


    def resolution(self):
        resolution = self.resolutions[self.current_resolution]
        print(resolution)
        return(resolution)

    def change_resolution(option):
        NewRes = self.resolutions[option]
        NewRes_x, NewRes_y = NewRes

    def LoadGame():
        game_screen = pygame.display.set_mode((GameX, GameY))

        

        

    