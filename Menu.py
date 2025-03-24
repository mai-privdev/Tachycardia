class Menu:
    def __init__(self, length, width, font, title):
        self.length = length
        self.width = width
        self.font = font
        self.title = title
    
    def load(self):
        menu_screen = pygame.display.set_mode((self.length, self.width))

