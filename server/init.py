
print "Starting Model World II Server..."

from util.sockets import ServerSocket
import threading, os

def __main__():
	socket = ServerSocket()
	
	threads = []
	
	try:
		while 1:
			sock = socket.getClientObject()
			t = threading.Thread(target=printIncoming, args=(sock,))
			threads.append(t)
			t.start()
	finally:
		print "Joining with threads before dying..."
		os._exit(1)
		for thread in threads: thread.join()

def printIncoming(sock):
	while 1:
		if sock.alive:
			print sock.readLine()
		else:
			return

__main__()

