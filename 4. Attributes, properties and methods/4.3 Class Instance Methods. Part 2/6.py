class Gun:
    def __init__(self):
        self.shots = 0

    def shoot(self):
        print('pif') if self.shots % 2 == 0 else print('paf')        
        self.shots += 1
