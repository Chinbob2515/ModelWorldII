socket = None

LOG = True

def setSocket(sock):
	global socket
	socket = sock

def encode(code, subcode, param):
	param = [str(i) for i in param]
	return str(code)+":"+str(subcode)+":"+';'.join(param)

def decode(message):
	info = {"code": None, "subcode": None, "param": []}
	parts = message.split(":")
	info["code"] = int(parts[0])
	info["subcode"] = int(parts[1])
	info["param"] = parts[2].split(";")
	return info

def get():
	return decode(socket.readLine())

def send(code, subcode, param=[]):
	socket.sendLine(encode(code, subcode, param))
