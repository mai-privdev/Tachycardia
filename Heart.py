class Heart:
    def __init__(self,RestBPM,MaxBPM):
        self.RestBPM = RestBPM
        self.MaxBPM = MaxBPM
        self.CurrentBPM = self.RestBPM

    def relax(self):
        if self.CurrentBPM < 60:
            self.CurrentBPM += 1
        else:
            self.CurrentBPM -= 2
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
    
    def heartalcohol(self):
        self.CurrentBPM -= 50
        return(self.CurrentBPM)
