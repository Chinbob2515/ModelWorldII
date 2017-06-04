
__path__ = '/'.join(__file__.split('/')[:-1]+[""]) # Who cares if the slash is wrong?

import mysql.connector, random
import users.sqlutil as sqlutil

cnx = cursor = 0

def init():
	global cnx, cursor
	user = ""
	password = ""
	with open(__path__+"password.secret", "r") as file: user, password = file.read().split("\n")[0:2]
	
	cnx = mysql.connector.connect(user=user, password=password, host='127.0.0.1')
	cursor = cnx.cursor()
	
	sqlutil.connectToDatabase(cnx, cursor, "MWII")
	
	schema = ""
	with open(__path__+"schema.sql", "r") as file: schema = file.read()
	
	sqlutil.createTableIfNotExists(cursor, schema)
	
	cnx.commit()

def addUser(username):
	if not getUser(username):
		password = generatePassword()
		cursor.execute("INSERT INTO users (username, password) VALUES ('%s', '%s');" % (username, password))
		cnx.commit()
		return password
	else:
		return ""

def getUser(username):
	cursor.execute("SELECT password FROM users WHERE username='%s';" % (username,))
	for username in cursor: return username[0]
	return None

def getUserId(username):
	cursor.execute("SELECT id FROM users WHERE username='%s';" % (username,))
	for username in cursor: return username[0]
	return None

def generatePassword():
	words = []
	with open(__path__+"sortedwords.txt", "r") as file: words = file.read().strip().split("\n")
	return '_'.join([random.choice(words) for _ in xrange(4)])

def purge():
	print " -- WARNING -- DROPPING MAIN DATABASE -- "
	cursor.execute("DROP DATABASE MWII;")

def close():
	cursor.close()
	cnx.close()
