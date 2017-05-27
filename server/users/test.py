import mysql.connector

import sqlutil

cnx = mysql.connector.connect(user="ben", password="carrot", host="127.0.0.1")

cursor = cnx.cursor()

sqlutil.connectToDatabase(cnx, cursor, "MWII")

sqlutil.createTableIfNotExists(cursor, """CREATE TABLE IF NOT EXISTS `users` (
        `user_no` int(11) NOT NULL AUTO_INCREMENT,
        `username` varchar(14) NOT NULL,
        `password` varchar(16) NOT NULL,
        PRIMARY KEY (`user_no`)
) ENGINE=InnoDB;""")

cnx.commit()

cursor.close()
cnx.close()
