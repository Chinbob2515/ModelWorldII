from bs4 import BeautifulSoup

__path__ = '/'.join(__file__.split('/')[:-1]+[""]) # Who cares if the slash is wrong?

tiles = None

with open(__path__+"tiles.xml", "r") as file:
	tiles = BeautifulSoup(file, "xml")

def getSoup():
	return tiles

def getTiles():
	return tiles.tiles.find_all("tile")
