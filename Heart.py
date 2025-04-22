#Heart



class Heart:
    def __init__(self,RestBPM,MaxBPM, font):
        import Tachycardia
        self.RestBPM = RestBPM
        self.MaxBPM = MaxBPM
        self.CurrentBPM = self.RestBPM
        self.bloodcolour = (115, 0, 5)
        self.heartcolour = (255, 0, 0)
        self.font = font






    def update(self):
        text = self.font.render(str(heart.CurrentBPM), True, self.bloodcolour, self.heartcolour)
        textRect = text.get_rect()
        textRect.center = (GameX * 0.1, GameY * 0.9)

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
