from types import MethodType
from random import randint

properties = {
	"Dwarf": {
		"maxHealth": 10
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
	
	def __init__(self, pos, owner):
		name = self.__class__.__name__
		self._maxHealth = properties[name]["maxHealth"]
		self._health = self._maxHealth
		if len(pos) != 3:
			raise AttributeError("wrong num of coordinates")
		self._pos = pos
		self._stats = [i+_highestRolls(4, 3) for i in _baseStats]
		self.owner = owner
	
	@property
	def health(self):
		return self._health
	
	@property
	def stats(self):
		return self._stats
	
	@property
	def maxHealth(self):
		return self._maxHealth
	
	@property
	def pos(self):
		return pos
	
	def do_thing(self):
		def a(self):
			print "Hi"
		self.user_a = MethodType(a, self, self.__class__)
	
	def assign(self, function_name, code):
		exec(code)
		exec("self.user_%s = MethodType(%s, self, self.__class__)" % (function_name, function_name))

class Dwarf(Entity):
	
	def __init__(self, *args):
		Entity.__init__(self, *args)
	
	def user_speak(self, text):
		text = text.split(" ")
		command = text[0]
		if command.lower() == "d":
			print "I am blind"
		if command.lower() == "s":
			print "My stats are:", self._stats
