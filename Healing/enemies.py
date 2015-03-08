class Enemy:
    def __init__(self, name, hp, dmg1, dmg2):
        self.name = name
        self.hp = hp
        self.dmg1 = dmg1
        self.dmg2 = dmg2

    def is_alive(self):
        return self.hp > 0


class Walker(Enemy):
    def __init__(self):
        super().__init__(name="Walker", hp=30, dmg1=5, dmg2=10)