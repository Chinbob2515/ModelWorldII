
print "Starting Model World II Server..."

from util.sockets import ServerSocket
import threading, os, handler
from sim.main import Sim

def __main__():
	socket = ServerSocket()
	
	sim = Sim()
	sim.new(4,4,4)
	
	try:
		while 1:
			sock = socket.getClientObject()
			t = threading.Thread(target=handler.__main__, args=(sock,sim))
			t.start()
	except Exception,e:
		print str(e)
	finally:
		print "\n"
		print "Brutually murdering everything..."
		os._exit(1)

__main__()

