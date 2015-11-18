import items, enemies

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()

class StartingRoom(MapTile):
	def intro_text(self):
		return"""
		You awaken to a loud noise outside your flat! After rubbing your eyes you see your tv, computer, couch, and two doors.
		"""
		# yes i am a fan of the oxford comma!
	def modify_player(self, player):
		# Room has no action on player
		pass
class street(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		self.add_loot(player)
class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)
		def modify_player(self, the_player):
			if self.enemy.is_alive():
				print("Enemy does {} damage. You have {} HP Remaining.".format(self.enemy.damage, the_player.hp))
