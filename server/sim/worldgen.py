
__path__ = '/'.join(__file__.split('/')[:-1]+[""]) # Who cares if the slash is wrong?

import sim.data.tiles, random

class TileType():
	
	def __init__(self, attrs, id):
		for key in attrs:
			try:
				attrs[key] = eval(attrs[key])
			except:
				pass
		self.__dict__ = attrs
		self.id = id
	
	def __str__(self):
		return "Type[%s]" % self.__dict__

class TileTypes():
	
	def __init__(self, types):
		self.types = types
	
	def __getattr__(self, name):
		if name == "types":
			raise AttributeError("No such value.")
		value = self.name(name)
		if value == None:
			raise AttributeError("No such value")
		return value
	
	def name(self, name):
		for type in self.types:
			if type.name == name:
				return type
		return None

class Tile:
	
	OPIUM_REGEN_RATE = 1.0/10
	
	def __init__(self, x, y, z, type, world):
		self.world = world
		self.x = x
		self.y = y
		self.z = z
		self.type = type
		self.opium = type.maxopium
	
	def update(self):
		if self.opium != self.type.maxopium:
			self.opium += self.type.maxopium * OPIUM_REGEN_RATE
	
	def __str__(self):
		return "Tile[x: %s; y: %s; z: %s; opium: %s; type: %s]" % (self.x, self.y, self.z, self.opium, str(self.type))

class World():
	
	def __init__(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth
		self.world = [[[None for _ in xrange(height)] for _ in xrange(width)] for _ in xrange(depth)]
		
		self.tileTypes = []
		tiledata = sim.data.tiles.getTiles()
		for tiledatumn in xrange(len(tiledata)):
			tiledatum = tiledata[tiledatumn]
			tileType = TileType(tiledatum.attrs, tiledatumn)
			self.tileTypes.append(tileType)
		self.tileTypes = TileTypes(self.tileTypes)
		
		self.entities = []
	
	def gen(self):
		# This is an alpha gen, with no texture whatsoever
		for x in xrange(self.width):
			for y in xrange(self.height):
				self.world[x][y][0] = Tile(x, y, 0, random.choice([self.tileTypes.air, self.tileTypes.grass]), self)
		
		for x in xrange(self.width):
			for y in xrange(self.height):
				for z in xrange(self.depth-1):
					self.world[x][y][z+1] = Tile(x, y, z, self.tileTypes.stone, self)
	
	def update(self):
		for y in self.world:
			for z in y:
				for tile in z:
					tile.update()
		for entity in self.entities:
			entity._update()
	
	def randpos(self):
		return [random.randint(0, self.width-1), random.randint(0, self.height-1), random.randint(0, self.depth-1)]
