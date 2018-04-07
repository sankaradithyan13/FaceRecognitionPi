import time
import MySQLdb

result1 = []
for i in range(6):
    result1.append(-1)
db = MySQLdb.connect("localhost", "root", "raspberry", "data")
curs=db.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS leaves (Serial_No INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Id INT(5) NOT NULL , Leaves_assigned INT(5) NOT NULL, Leaves_taken INT(5) NOT NULL, Leaves_Remaining INT(5) NOT NULL)")
curs.execute("SELECT * FROM dates WHERE tdate='%s'" % (time.strftime("%Y-%m-%d")))
result1=curs.fetchall()
for i in range(len(result1)):
    print result1[i][1]

 #if str(result1[len(result1)-1][1])
db.commit()
print "Data committed"
