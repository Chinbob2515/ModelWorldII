import worldgen, entity, pickle

# Maybe consider changing pickle to cpickle, and choosing the byte stream mode, to increase save/load speed?

class Sim():
	
	def __init__(self):
		self.world = None
	
	def new(self, width, height, depth):
		self.world = worldgen.World(width, height, depth)
	
	def load(self, fileName):
		tmp_dict = {}
		with open(fileName, "r") as file:
			tmp_dict = pickle.load(file)
		self.__dict__.update(tmp_dict)
	
	def save(self, fileName):
		with open(fileName, "w") as file:
			pickle.dump(self.__dict__, file)
	
	def update(self):
		pass
	
	def addUser(self, id):
		self.world.entities.append(entity.Dwarf(self.world.randpos(), id))
	
	def getEntity(self, id):
		for entity in self.world.entities:
			if entity._id == id:
				return entity

