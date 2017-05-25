
print "Starting Model World II Server..."

from util.sockets import ServerSocket
import threading

socket = ServerSocket()

threads = []

try:
	while 1:
		sock = socket.getClientObject()
		t = threading.Thread(target=printIncoming, args=(sock,))
		threads.append(t)
		t.start()
finally:
	for thread in threads: thread.join()
	socket.kill()

def printIncoming(sock):
	while 1:
		print socket.readLine()
