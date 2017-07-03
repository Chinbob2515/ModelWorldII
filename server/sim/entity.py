from types import MethodType
from random import randint
import users.main

WORLD_ID = 1

properties = {
	"Dwarf": {
		"maxHealth": 10,
		"maxSaturation": 100,
		"hungerRate": -1,
		"fat": 10
		}
	}

_baseStats = [8, 8, 8, 8, 8, 8]

def _statToScore(stat):
	stat -= 10
	stat /= 2
	return stat

def _highestRolls(numRolls, numSelect):
	rolls = [randint(1, 6) for _ in xrange(numRolls)]
	rolls = sorted(rolls)[::-1]
	return sum(rolls[:numSelect])

class Entity:
	
	_customFunctions = {}
	
	def __init__(self, sim, pos, owner, name="Bob"):
		race = self.__class__.__name__
		self._maxHealth = properties[race]["maxHealth"]
		self._health = self._maxHealth
		self._maxSaturation = properties[race]["maxSaturation"]
		self._saturation = self._maxSaturation
		self._hungerRate = properties[race]["hungerRate"]
		self._fat = properties[race]["fat"]
		if len(pos) != 3:
			raise AttributeError("wrong num of coordinates")
		self._pos = pos
		self._stats = [_highestRolls(4, 3) for _ in _baseStats]
		self._name = name
		self._owner = owner
		users.main.addEntity(owner, race, "", name)
		self._id = users.main.getLastEntityId()
		self._sim = sim
		self._dead = False
	
	def _update(self):
		self._saturation += self.hungerRate
		if self._saturation < 0:
			if self._fat > 0:
				self._fat -= 1
				self._saturation += self._maxSaturation
			self._health -= 1
		if self.health < 0:
			self._dead = True
			self._owner = WORLD_ID
	
	def __getattr__(self, name):
		privateVariable = "_"+name
		if privateVariable in self.__dict__:
			return self.__dict__[privateVariable]
		raise AttributeError("No such value in this entity")
	
	def _move(self, vector):
		if type(vector) != tuple:
			raise TypeError("move instruction takes a tuple")
		if sum(vector) != 1:
			raise ValueError("vector modulus must be 1 for moving")
		
	
#	def do_thing(self):
#		def a(self):
#			print "Hi"
#		self.user_a = MethodType(a, self, self.__class__)
	
	def assign(self, function_name, code):
		exec(code)
		self.customFunctions[function_name] = eval(function_name)
#		exec(code)
#		exec("self.user_%s = MethodType(%s, self, self.__class__)" % (function_name, function_name))
	
	def _speak(self, text):
		if self._dead:
			return "Creature is dead. Cannot speak."
		else:
			return self.user_speak(text)
	
	def user_speak(self, text):
		return "uhhhhg"
	
	def custom_function(self, name):
		self.customFunctions[name]()

class Dwarf(Entity):
	
	def __init__(self, *args):
		Entity.__init__(self, *args)
	
	def user_speak(self, text):
		text = text.split(" ")
		command = text[0].lower()
		answer = "I don't understand."
		if command == "d":
			x = self._pos[0]
			y = self._pos[1]
			z = self._pos[2]
			#print x, y, z, [[[str(z) for z in y] for y in x] for x in self._sim.world.world]
			answer = str(self._sim.world.world[x][y][z])
		if command == "s":
			answer =  "My stats are: %s" % (self._stats,)
		if command == "p":
			answer = self._pos
		if command == "q":
			answer = self.__dict__
		return answer
