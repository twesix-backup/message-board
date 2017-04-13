import sqlite3


class MyDatabase:
    @staticmethod
    def get_conn():

        try:
            conn = sqlite3.connect("MessageBoard.db")
            return conn
        except ConnectionError:
            error="can't connect the database"
            return error


'''sql="insert into user(uid,account,password)values(,'mzy','123456')"
sql0="select * from message"
sql1="select * from user"
sql2="create table user(uid varchar(20),account varchar(30),password varchar(30))"
sql3="create table message(uid varchar(20),mid varchar(20),message text)"
sql4="insert into  message(uid ,mid,message)values('1491963082632898','1491963082632969','123')"
sql5="insert into user(uid,account,password)values('1491963082632898','21140820','123456')"
cursor.execute(sql0) 
data=cursor.fetchall()
for i in data:
    print(i);
conn.commit()
cursor.close()
conn.close()
print(int(datetime.now().timestamp()*1000000))'''
