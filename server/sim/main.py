import worldgen, entity

class Sim():
	
	def __init__(self):
		self.world = None
	
	def new(self, width, height, depth):
		self.world = worldgen.World(width, height, depth)
	
	def load(self, file):
		pass
	
	def save(self, file):
		pass
	
	def update(self):
		pass
	
	def addUser(self, id):
		self.world.entities.append(entity.Dwarf(self.world.randpos(), id))

