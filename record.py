import MySQLdb

db = MySQLdb.connect("localhost", "root", "raspberry", "data")
curs=db.cursor()
try:
        curs.execute("CREATE TABLE IF NOT EXISTS record (Serial_No INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Id INT(5) NOT NULL , Name VARCHAR(20) NOT NULL, Folder_Name VARCHAR(20) NOT NULL)")
        #curs.execute ("INSERT INTO record (Id,Name) \
        #        VALUES ('%d', '%s')"%(0,'Shubham'))
        curs.execute ("INSERT INTO record (Id,Name)values(0,'Shubham')")
        curs.execute ("INSERT INTO record (Id,Name)values(1,'Sankar')")
        curs.execute ("INSERT INTO record (Id,Name)values(2,'Apurv')")
        curs.execute ("INSERT INTO record (Id,Name)values(3,'Rahul')")
        curs.execute ("INSERT INTO record (Id,Name)values(4,'Kittu')")
        print "Data committed"
        db.commit()
except:
        print "Data Rollback"
        db.rollback()


