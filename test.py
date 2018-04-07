import time
import MySQLdb


if __name__ == '__main__':
    label = 0
    db = MySQLdb.connect("localhost", "root", "raspberry", "data")
    curs=db.cursor()

    curs.execute("CREATE TABLE IF NOT EXISTS dates (Serial_No INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Id INT(5) NOT NULL , Name VARCHAR(20) NOT NULL, tdate DATE NOT NULL , intime TIME NOT NULL, outtime TIME NULL)")
    curs.execute("SELECT * FROM record WHERE Id=%s" % (label))
    result=curs.fetchall()
    print result
    curs.execute("SELECT * FROM dates WHERE Id=%s" % (label))
    result1=curs.fetchall()
    print result1
    print len(result1)
    print result1[1][3]
    print result1[0][3]
    
