import web

urls = (
    '/', 'Index',
    '/login','Login'
)

app = web.application(urls, globals())


class Index:
    def GET(self):
        return 'hello index'


class Login:
    def GET(self):
        return 'login'

if __name__ == '__main__': app.run()
