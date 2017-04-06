let routes =
    [
        {
            path:'/add',
            component: require('./components/add.vue')
        },
        {
            path:'/list',
            component: require('./components/list.vue')
        },
        {
            path:'/login',
            component: require('./components/login.vue')
        },
        {
            path:'/register',
            component: require('./components/register.vue')
        }
    ];

let router = new VueRouter(routes);

let app = new Vue
(
    {
        el:'#app',
        router:router,
        template:'<wrapper></wrapper>',
        components:
            {
                wrapper:require('./components/app.vue')
            }
    }
);