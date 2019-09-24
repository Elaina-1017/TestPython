'''
Test Mysql
'''
import mysql.connector

RDSHOST = "xxxx.xxxx.com"
NAME = "dbuser"
PASSWORD = "xxxx"
DBNAME = "xxxx"

CONN = mysql.connector.connect(host=RDSHOST, port=3306, user=NAME, passwd=PASSWORD, database=DBNAME)

MYCURSOR = CONN.cursor()
MYCURSOR.execute("drop table if exists Employee")
MYCURSOR.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL,"
                 + " PRIMARY KEY (EmpID))")

SQL = 'insert into Employee (EmpID, Name) values(%s, %s)'
VAL = [(100, "www.google.com"),
       (101, "www.microsoft.com"),
       (102, "www.facebook.com"),
       (103, "www.stackoverflow.com")]

MYCURSOR.executemany(SQL, VAL)
CONN.commit()

print("Insert Successful。", "Data Count：【", MYCURSOR.rowcount, "】")
