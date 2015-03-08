class Item():
    """The base class for all items"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "=====\n{}\n=====\n{}\n".format(self.name, self.description)


class Consumables(Item):
    def __init__(self, name, description, uses):
        self.name = name
        self.description = description
        self.uses = uses

        super().__init__(name, description)
    def __str__(self):
        return "=====\n{}\n=====\n{}\nUses: []\n".format(self.name, self.description, self.uses)

class FirstAid(Consumables):
    def __init__(self, name, description, uses, healing, stamina):
        self.healing = healing
        self.stamina = stamina

        super().__init__(name, description, uses)
    def __str__(self):
        return "=====\n{}\n=====\n{}\nUses: {}\nHP regained: {}\nStamina regained: {}\n".format(self.name, self.description, self.uses, self.healing, self.stamina)

class FirstAidKit(FirstAid):
    def __init__(self):
        super().__init__(name="A First Aid kit.",
                         description="A small first aid kit.",
                         uses=5,
                         healing=30,
                         stamina=10)

class ProPlus(FirstAid):
    def __init__(self):
        super().__init__(name="Pro-Plus.",
                         description="A box containing some Pro-Plus tablets.",
                         uses=10,
                         healing=0,
                         stamina=30)

class Weapon(Item):
    def __init__(self, name, description, stamina, dmg1, dmg2):
        self.stamina = stamina
        self.dmg1 = dmg1
        self.dmg2 = dmg2

        super().__init__(name, description)
    def __str__(self):
        return "=====\n{}\n=====\n{}\nStamina cost: {}\nLow Damage: {}\nHigh Damage: {}\n".format(self.name, self.description, self.stamina, self.dmg1, self.dmg2)


class Crowbar(Weapon):
    def __init__(self):
        super().__init__(name="Crowbar",
                         description="A small crowbar, suitable for prising open doors, as well as bludgeoning enemies.",
                         stamina=5,
                         dmg1=3,
                         dmg2=7)


class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                         description="A hand axe. Harder to swing than a crowbar, but much better at chopping up stuff.",
                         stamina=10,
                         dmg1=6,
                         dmg2=12)


class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                         description="A large kitchen knife. Easy to swing, but doesn't do much against the living dead.",
                         stamina=3,
                         dmg1=2,
                         dmg2=4)
