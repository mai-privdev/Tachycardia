class Heart:
    def __init__(self,RestBPM,MaxBPM):
        self.RestBPM = RestBPM
        self.MaxBPM = MaxBPM
        self.CurrentBPM = self.RestBPM

    def heartmove(self):
        self.CurrentBPM += 5
        return(self.CurrentBPM)

    def heartscare(self):
        self.CurrentBPM += 10
        return(self.CurrentBPM)
