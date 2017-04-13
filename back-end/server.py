import web
from dbUtil import MyDatabase
from datetime import datetime

urls = (
    '/register', 'Register',
    '/login', 'Login',
    '/add', 'Add',
    '/update', 'Update',
    '/delete', 'Delete',
    '/list','List'
)

app = web.application(urls, globals())


class Register:
    def GET(self):
        i = web.input()
        account = i.account
        password = i.password
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from user where account='%s'" % account)
            data = cursor.fetchall()
            id = int(datetime.now().timestamp() * 1000000)
            if data.__len__() > 0:
                respond = "{\"status\":\"error\",\"message\":\"the account already exists\"}"
            else:
                cursor.execute("insert into user(uid,account,password)values('%s','%s','%s')" % (id, account, password))
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond


class Login:
    def GET(self):
        i = web.input()
        account = i.account
        password = i.password
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from user where account='%s' and password='%s'" % (account, password))
            data = cursor.fetchall()
            if data.__len__() <= 0:
                respond = "{\"status\":\"error\",\"message\":\"account or password is incorrect\"}"
            else:
                respond = "{\"status\":\"ok\",\"message\":\"%s\"}" % data[0][0]
            conn.commit()
            cursor.close()
            conn.close()
        return respond


class Add:
    def GET(self):
        i = web.input()
        uid = i.uid
        message = i.message
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from user where uid='%s'" % uid)
            data = cursor.fetchall()
            if data.__len__() <= 0:
                respond = "{\"status\":\"error\",\"message\":\"uid is incorrect\"}"
            else:
                id = int(datetime.now().timestamp() * 1000000)
                cursor.execute("insert into message (uid,mid,message)values('%s','%s','%s')" % (uid, id, message))
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond


class Update:
    def GET(self):
        i = web.input()
        uid = i.uid
        mid = i.mid
        message = i.message
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from message where uid='%s' and mid='%s'" % (uid, mid))
            data = cursor.fetchall()
            if data.__len__() <= 0:
                respond = "{\"status\":\"error\",\"message\":\"message doesn't exist\"}"
            else:
                cursor.execute("update message set message='%s' where uid='%s' and mid='%s'" % (message, uid, mid))
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond

class Delete:
    def GET(self):
        i=web.input()
        mid=i.mid
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from message where mid='%s'" % mid)
            data = cursor.fetchall()
            if data.__len__() <= 0:
                respond = "{\"status\":\"error\",\"message\":\"message doesn't exist\"}"
            else:
                cursor.execute("delete from message where  mid='%s'" % mid)
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond

class List:
    def GET(self):
        i=web.input()
        uid=i.uid
        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from message where uid='%s'" % uid)
            data = cursor.fetchall()
            if data.__len__() <= 0:
                respond = "{\"status\":\"error\",\"message\":\"uid is incorrect\"}"
            else:
                cursor.execute("select * from message")
                data=cursor.fetchall()
                respond="["
                j=0
                for i in data:
                    j+=1
                    if i[0]==uid:
                        respond+="{\"message_content\":\"%s\",\"message_id\":\"%s\"}"%(i[2],i[1])
                    else:
                        respond += "{\"message_content\":\"%s\"}" % i[2]
                    if j<data.__len__():
                        respond+=","
                respond+="]"
            conn.commit()
            cursor.close()
            conn.close()
        return respond


if __name__ == '__main__': app.run()
