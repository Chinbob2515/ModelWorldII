import util.message as message
import users.main

def __main__(socket):
	message.setSocket(socket)
	users.main.init()
	username = ""
	
	messageLogin = message.get()
	if messageLogin["code"] == 10: # Login
		while username == "":
			#print "User trying to login with details:", messageLogin
			#print "Matching password should be:", users.main.getUser(messageLogin["param"][0])
			if users.main.getUser(messageLogin["param"][0]) == messageLogin["param"][1]:
				message.send(10, 1)
				username = messageLogin["param"][0]
			else:
				message.send(10, -1)
				messageLogin = message.get()
	elif messageLogin["code"] == 11: # Register
		while username == "":
			if not users.main.getUser(messageLogin["param"][0]):
				password = users.main.addUser(messageLogin["param"][0])
				message.send(11, 1, [password])
			else:
				message.send(11, -1)
	else:
		print "Wrong code at login, aborting thread management..."
		return False
