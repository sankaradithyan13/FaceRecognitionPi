import time
import MySQLdb

def data_entry(label):
    result1 = []
    for i in range(6):
        result1.append(-1)
    db = MySQLdb.connect("localhost", "root", "raspberry", "data")
    curs=db.cursor()
    #try:
    curs.execute("CREATE TABLE IF NOT EXISTS dates (Serial_No INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Id INT(5) NOT NULL , Name VARCHAR(20) NOT NULL, tdate DATE NOT NULL , intime TIME NOT NULL, outtime TIME NULL)")
    curs.execute("SELECT * FROM record WHERE Id=%s" % (label))
    result=curs.fetchone()
    curs.execute("SELECT * FROM dates WHERE Id=%s" % (label))
    result1=curs.fetchall()
    if result1 is ():
        curs.execute ("INSERT INTO dates (Id,Name,tdate,intime) \
        VALUES ('%d', '%s' , '%s' , '%s')" %(result[1],result[2],time.strftime("%Y-%m-%d"),time.strftime("%H:%M:%S")))    
    else:
        if str(result1[len(result1)-1][3]) == time.strftime("%Y-%m-%d"):
            curs.execute("UPDATE dates SET outtime='%s' WHERE id='%s' && tdate='%s'" % (time.strftime("%H:%M:%S"),label,time.strftime("%Y-%m-%d")))
        else:
            curs.execute ("INSERT INTO dates (Id,Name,tdate,intime) \
            VALUES ('%d', '%s' , '%s' , '%s')" %(result[1],result[2],time.strftime("%Y-%m-%d"),time.strftime("%H:%M:%S")))    
                
    db.commit()
    print "Data committed"
    #except:
        #print "DB rollback"
        #db.rollback()
   
