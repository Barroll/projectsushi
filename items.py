 class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
 class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 class Pole(Weapon):
    def __init__(self):
        super().__init__(name="Pole",
                         description="Likely a plumbing pipe, suitable for bludgeoning.",
                         value=0,
                         damage=5)
 
 class Shank(Weapon):
    def __init__(self):
        super().__init__(name="Shank",
                         description="A small crude shank with some rust, and tape. Somewhat more dangerous than a pipe.",
                         value=10,
                         damage=10)
 class Credit(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Credit",
                         description="Credits, the universal currency.".format(str(self.amt)),
                         value=self.amt)
