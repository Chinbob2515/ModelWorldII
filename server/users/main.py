
__path__ = '/'.join(__file__.split('/')[:-1]+[""]) # Who cares if the slash is wrong?

import mysql.connector

user = ""
password = ""
with open("password.secret", "r") as file: user, password = file.read().split("\n")[0:2]

cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='MWII')

cnx.close()
