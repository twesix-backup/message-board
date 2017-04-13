import sqlite3

sql0 = "select * from message"
sql1 = "select * from user"
sql4="insert into  message(uid ,mid,message)values('1491963082632898','1491963082632969','123')"

conn = sqlite3.connect("MessageBoard.db")
cursor = conn.cursor()
cursor.execute(sql0)
data = cursor.fetchall()
for i in data:
    print(i);
conn.commit()
cursor.close()
conn.close()
