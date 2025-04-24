#Heart
import pygame
pygame.display.init()


class Heart:
    def __init__(self,RestBPM,MaxBPM, font):
        import Tachycardia
        self.RestBPM = RestBPM
        self.MaxBPM = MaxBPM
        self.CurrentBPM = self.RestBPM
        self.bloodcolour = (115, 0, 5)
        self.heartcolour = (255, 0, 0)
        self.font = font


    def update():
        text = self.font.render(str(self.CurrentBPM), True, self.bloodcolour, self.heartcolour)
        textRect = text.get_rect()
        textRect.center = (896 * 0.1, 504 * 0.9)
        Display.screen.blit(text, textRect)

    def relax(self):
        if self.CurrentBPM < 60:
            self.CurrentBPM += 1
        elif self.CurrentBPM > 60:
            self.CurrentBPM -= 1
        else:
            pass

        return(self.CurrentBPM)

    def heartscare(self):
        self.CurrentBPM += 5
        return(self.CurrentBPM)

    def heartfear(self):
        self.CurrentBPM += 10
        return(self.CurrentBPM)

    def heartterror(self):
        self.CurrentBPM += 20
        return(self.CurrentBPM)
    
    def heartanesthetic(self):
        self.CurrentBPM -= 50
        return(self.CurrentBPM)
