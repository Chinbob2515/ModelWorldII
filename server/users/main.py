
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
		cursor.execute("INSERT INTO users (id, username, password) VALUES (0, %s, %s);", (username, password))
		cnx.commit()
		return password
	else:
		return ""

def getRace(race):
	cursor.execute("SELECT id FROM races WHERE name=%s", (race,))
	for id in cursor: return id[0]

def addEntity(owner, race, code, name):
	cursor.execute("INSERT INTO entities (id, owner, race, code, name) VALUES (0, %s, %s, %s, %s)", (owner, getRace(race), code, name))
	cnx.commit()

def listEntities(owner=None, race=None, name=None, id=None):
	query = "SELECT * FROM entities WHERE "
	conditions = []
	args = []
	if not owner and not race and not name and not id:
		raise TypeError("listEntities requires at least one argument")
	if owner:
		conditions.append("owner=%s")
		args.append(owner)
	if race:
		conditions.append("race=%s")
		args.append(race)
	if name:
		conditions.append("name=%s")
		args.append(name)
	if id:
		conditions.append("id=%s")
		args.append(id)
	condition = ' AND '.join(conditions)
	query = query + condition + ";"
	args = tuple(args)
	cursor.execute(query, args)
	answer = []
	for i in cursor: answer.append(i)
	return answer

def getUser(username):
	cursor.execute("SELECT password FROM users WHERE username=%s;", (username,))
	for username in cursor: return username[0]
	return None

def getUserId(username):
	cursor.execute("SELECT id FROM users WHERE username=%s;", (username,))
	for username in cursor: return username[0]
	return None

def generatePassword():
	words = []
	with open(__path__+"sortedwords.txt", "r") as file: words = file.read().strip().split("\n")
	return '_'.join([random.choice(words) for _ in xrange(4)])

def getLastEntityId():
	cursor.execute("SELECT LAST_INSERT_ID();")
	for id in cursor: return int(id[0])

def purge():
	print " -- WARNING -- DROPPING MAIN DATABASE -- "
	cursor.execute("DROP DATABASE MWII;")

def reset():
	init()
	purge()
	init()

def close():
	cursor.close()
	cnx.close()
