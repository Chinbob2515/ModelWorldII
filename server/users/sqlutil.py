import mysql.connector
from mysql.connector import errorcode

def connectToDatabase(cnx, cursor, dbName):
	try:
		cnx.database = dbName
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			try:
				cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(dbName))
			except mysql.connector.Error as err:
				print "Failed creating database: {}".format(err)
				exit(1)
			cnx.database = dbName
		else:
			print err
			exit(1)

def createTableIfNotExists(cursor, schema):
	try:
		cursor.execute(schema, multi=True)
	except mysql.connector.Error as err:
		print "oops error"
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print "table already exists."
		else:
			print err.msg
