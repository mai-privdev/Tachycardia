#display
class Display:
    def __init__(self):
        self.game_x = 896
        self.game_y = 504
        self.menu_x = 400
        self.menu_y = 400
        self.resolutions = [(512, 288), (896, 504), (1280, 720), (1920, 1080)]
        

   


    def resolution(self):
        return(self.game_x, self.game_y)

    def change_resolution(option):
        NewRes = self.resolutions[option]
        NewRes_x, NewRes_y = NewRes

    def LoadGame():
        game_screen = pygame.display.set_mode((GameX, GameY))

        

        

    