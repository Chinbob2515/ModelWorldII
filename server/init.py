
print "Starting Model World II Server..."

from util.sockets import ServerSocket
import threading, os
import handler

def __main__():
	socket = ServerSocket()
	
	try:
		while 1:
			sock = socket.getClientObject()
			t = threading.Thread(target=handler.__main__, args=(sock,))
			t.start()
	except Exception,e:
		print str(e)
	finally:
		print "Brutually murdering everything..."
		os._exit(1)

__main__()

