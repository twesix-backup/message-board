import web
from dbUtil import MyDatabase
import time

urls = (
    '/register', 'Register',
    '/login', 'Login',
    '/add', 'Add',
    '/update', 'Update',
    '/delete', 'Delete',
    '/list', 'List',
    '/', 'Index'
)

app = web.application(urls, globals())


class Index:
    def __init__(self):
        pass

    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        return '/'


class Register:
    def __init__(self):
        pass

    def GET(self):

        web.header("Access-Control-Allow-Origin", "*")

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
            if data.__len__() > 0:
                respond = "{\"status\":\"error\",\"message\":\"the account already exists\"}"
            else:
                uid = int(time.time() * 1000)
                cursor.execute("insert into user(uid,account,password) values('%s','%s','%s')" % (uid, account, password))
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond


class Login:
    def GET(self):

        web.header("Access-Control-Allow-Origin", "*")

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

        web.header("Access-Control-Allow-Origin", "*")

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
                mid = int(time.time() * 1000)
                cursor.execute("insert into message (uid,mid,message)values('%s','%s','%s')" % (uid, mid, message))
                respond = "{\"status\":\"ok\",\"message\":\"\"}"
            conn.commit()
            cursor.close()
            conn.close()
        return respond


class Update:
    def GET(self):

        web.header("Access-Control-Allow-Origin", "*")

        i = web.input()
        mid = i.mid
        message = i.message

        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()

            cursor.execute("update message set message='%s' where mid='%s'" % (message, mid))
            respond = "{\"status\":\"ok\",\"message\":\"\"}"

            conn.commit()
            cursor.close()
            conn.close()
        return respond

class Delete:
    def GET(self):

        web.header("Access-Control-Allow-Origin", "*")

        i = web.input()
        mid = i.mid

        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()

            cursor.execute("delete from message where  mid='%s'" % mid)
            respond = "{\"status\":\"ok\",\"message\":\"\"}"

            conn.commit()
            cursor.close()
            conn.close()
        return respond


class List:
    def GET(self):

        web.header("Access-Control-Allow-Origin", "*")

        i = web.input()
        uid = i.uid

        conn = MyDatabase.get_conn()
        if conn == "can't connect the database":
            respond = "{\"status\":\"error\",\"message\":\"can't connect the database\"}"
        else:
            cursor = conn.cursor()
            cursor.execute("select * from message")
            data = cursor.fetchall()
            respond = "["
            j = 0
            for i in data:
                j += 1
                if i[0] == uid:
                    respond += "{\"message_content\":\"%s\",\"message_id\":\"%s\"}" % (i[2], i[1])
                else:
                    respond += "{\"message_content\":\"%s\"}" % i[2]
                if j < data.__len__():
                    respond += ","
            respond += "]"

            conn.commit()
            cursor.close()
            conn.close()
        return respond


if __name__ == '__main__':
    app.run()
