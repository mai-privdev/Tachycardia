#display
class Display:
    def __init__(self):
        self.default_x = 896
        self.default_y = 504
        self.defmenu_x = 400
        self.defmenu_y = 400
        #0 = black
        #1 = blood
        #2 = heart
        #3 = white
        #4 = green
        #5 = blue
        self.colour = [(0,0,0), (115, 0, 5), (255, 0, 0), (255, 255,255), (0, 255, 0), (0, 0, 128) ]

    def colour(self, colour):
        return(self.colour[colour])