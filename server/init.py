
print "Starting Model World II Server..."

from util.sockets import ServerSocket
import threading, os, handler
from sim.main import Sim

saveFile = "saveFile.MWIIsave"

def __main__():
	socket = ServerSocket()
	
	sim = Sim()
	if os.path.isfile(saveFile):
		print "Loading save..."
		sim.load(saveFile)
	else:
		print "Generating new simulation..."
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
		print "Brutually murdering everything... (and perhaps doing some saving)"
		sim.save(saveFile)
		os._exit(1)

__main__()

