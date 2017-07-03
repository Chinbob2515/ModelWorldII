import worldgen, entity, pickle, threading, time

# Maybe consider changing pickle to cpickle, and choosing the byte stream mode, to increase save/load speed?

CYCLE_LENGTH = 0.5 # Length in seconds of game cycle

class Sim():
	
	def __init__(self):
		self.world = None
	
	def new(self, width, height, depth):
		self.world = worldgen.World(width, height, depth)
		self.world.gen()
	
	def load(self, fileName):
		tmp_dict = {}
		with open(fileName, "r") as file:
			tmp_dict = pickle.load(file)
		self.__dict__.update(tmp_dict)
	
	def save(self, fileName):
		with open(fileName, "w") as file:
			pickle.dump(self.__dict__, file)
	
	def start(self):
		t = threading.Thread(target=self.run)
		t.start()
	
	def run(self):
		while True:
			time.sleep(CYCLE_LENGTH)
			self.update()
	
	def update(self):
		self.world.update()
	
	def addUser(self, id):
		self.world.entities.append(entity.Dwarf(self, self.world.randpos(), id))
	
	def getEntity(self, id):
		for entity in self.world.entities:
			if entity._id == id:
				return entity

