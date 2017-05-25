
print "Starting Model World II..."

from util.sockets import ClientSocket

socket = ClientSocket()

socket.sendLine("hi\nhi\nwhoareyou?\n")

socket.close()
