from bs4 import BeautifulSoup

with open("testfile.xml", "r") as file:
	testfile = BeautifulSoup(file, "xml")

print testfile
