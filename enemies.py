class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0
class Thug(Enemy): 
	def __init__(self):
		super().__init__(name="Thug", hp=10, damage=2)
class Script kiddie(Enemy):
	def __init__(self):
		super().__init__(name="Script kiddie", hp=30, damage=15)