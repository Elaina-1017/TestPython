"""
HelloWorldサンプル
"""
import mysql.connector

RDS_HOST = "xxxx"
NAME = "xxxx"
PASSWORD = "xxxx"
DB_NAME = "xxxx"

CONN = mysql.connector.connect(host=RDS_HOST,
                               port=3306,
                               user=NAME,
                               passwd=PASSWORD,
                               database=DB_NAME)

def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    args = (event['EmpID'], event['Name'])
    cur = CONN.cursor()
    with cur:
        cur.execute("drop table if exists Employee")
        cur.execute("create table Employee ("
                    + "EmpID int NOT NULL,"          #フィールド名「EmpID」定義
                    + "Names varchar(255) NOT NULL," #フィールド名「Names」定義
                    + "PRIMARY KEY (EmpID))")        #プライマリキー定義
        cur.execute('insert into Employee (EmpID, Names) values(%s, %s)', args)
        CONN.commit()

    context['status'] = "OK"

    return context['status']
