
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

class TileTypes():
	
	def __init__(self, types):
		self.types = types
	
	def __getattr__(self, name):
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
	
	def __init__(self, x, y, z, type, world):
		self.world = world
		self.x = x
		self.y = y
		self.z = z
		self.type = type

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
			tileType = TileType(tiledatum.attrs, id)
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
	
	def randpos(self):
		return [random.randint(0, self.width), random.randint(0, self.height), random.randint(0, self.depth)]
