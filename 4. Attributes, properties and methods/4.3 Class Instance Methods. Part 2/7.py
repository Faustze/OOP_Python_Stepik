class Gun:
    def __init__(self):
        self.shots = 0
        self.counts_shots = 0

    def shoot(self):
        print('pif') if self.shots % 2 == 0 else print('paf')
        self.shots += 1

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0


gun1 = Gun()
gun2 = Gun()

gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()
print(gun1.shots_count())
print(gun2.shots_count())
gun1.shots_reset()
print(gun1.shots_count())
print(gun2.shots_count())