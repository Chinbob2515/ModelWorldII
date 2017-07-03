import util.message as message
import users.main
from sim import entity
from random import randint

__LOG = True

def Log(string, overide=False):
	if __LOG or overide: print string

def __main__(socket, sim):
	message.setSocket(socket)
	users.main.init()
	username = ""
	id = ""
	
	activeDwarf = None
	
	messageLogin = message.get()
	if messageLogin["code"] == 10: # Login
		while username == "":
			Log("Person trying to login with username "+ messageLogin["param"][0]+ ", and password "+ messageLogin["param"][1])
			if (not not messageLogin["param"][1].strip()) and users.main.getUser(messageLogin["param"][0]) == messageLogin["param"][1]: # Correct Login
				message.send(10, 1)
				username = messageLogin["param"][0]
				id = int(users.main.getUserId(username))
			else: # Try again
				Log("Wrong password")
				message.send(10, -1)
				messageLogin = message.get()
	elif messageLogin["code"] == 11: # Register
		while username == "":
			Log("Person trying to register with username "+ messageLogin["param"][0])
			if not users.main.getUser(messageLogin["param"][0]):
				username = messageLogin["param"][0]
				password = users.main.addUser(messageLogin["param"][0])
				id = int(users.main.getUserId(username))
				message.send(11, 1, [password])
				sim.addUser(id)
			else:
				Log("Username already taken")
				message.send(11, -1)
				messageLogin = message.get()
	else:
		print "Wrong code at login, aborting thread management..."
		return False
	
	Log("User "+ str(id) +" "+ username+ " logged in")
	
	while 1:
		messageIn = message.get()
		code = messageIn["code"]
		if code == 20: # Switch active dwarf
			dwarf = users.main.listEntities(id=int(messageIn["param"][0]), owner=id)
			if len(dwarf) != 1:
				message.send(20, -1)
				continue
			else:
				message.send(20, 1)
			activeDwarf = sim.getEntity(dwarf[0][0])
		elif code == 21: # Order dwarf
			if not activeDwarf:
				message.send(21, -1)
				continue
			message.send(21, 1, [activeDwarf._speak(messageIn["param"][0])])
		elif code == 22: # List dwarves
			dwarves = users.main.listEntities(owner=id)
			message.send(22, 1, dwarves)
		elif code == 01: # Exit
			Log("User "+ str(id) +" "+ username+ " exiting")
			return True
