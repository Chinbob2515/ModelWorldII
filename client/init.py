
print "Starting Model World II..."

from util.sockets import ClientSocket
from util.input import *
import util.message as message

socket = ClientSocket()
message.setSocket(socket)

answer = getInput("Would you like to (L)ogin or (R)egister?", ["L", "R"])
if answer == 0:
	verified = False
	while not verified:
		username = raw_input("Username: ")
		password = raw_input("Password: ")
		message.send(10, 0, [username, password])
		messageLogin = message.get()
		if messageLogin["code"] != 10:
			print "wrong code response on login?"
			continue
		if messageLogin["subcode"] == -1:
			print "Username or password wrong. Try again"
		elif messageLogin["subcode"] == 1:
			print "Welcome %s." % (username,)
			verified = True
else:
	verified = False
	while not verified:
		username = raw_input("Enter a username: ")
		message.send(11, 0, [username])
		messageRegister = message.get()
		if messageRegister["code"] != 11:
			print "wrong code response on register?"
			continue
		if messageRegister["subcode"] == -1:
			print "Username taken. Try another"
		elif messageRegister["subcode"] == 1:
			print "Register sucessful!"
			print "Your password (you don't get a choice), is:", messageRegister["param"][0]
			verified = True

print "The game starts here: please read manual.txt if you do not know what to type."

RUNNING = True
while RUNNING:
	userInput = raw_input()
	if userInput.startswith("\\"): # Game command
		userInput = userInput.strip("\\").split(" ")
		command = userInput[0]
		if command == "switch":
			print "Attempting to switch dwarf ID %s..." % (userInput[1],)
			message.send(20, 0, userInput[1:])
			success = message.get()["subcode"]
			if success == 1:
				print "Dwarf switched."
			elif success == -1:
				print "ID is wrong somehow."
		elif command == "list":
			print "Listing dwarves..."
			message.send(22, 0)
			response = message.get()
			dwarves = [eval(i) for i in response["param"]]
			for dwarf in dwarves:
				print "ID: %s ; Name : %s ;" % dwarf[0:2]
		elif command == "exit":
			print "Exiting..."
			message.send(01, 0)
			RUNNING = False
	else: # User talking to active dwarf
		message.send(21, 0, [userInput])
		response = message.get()
		print response["param"][0]

print "The game ends here."

socket.close()
