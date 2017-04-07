const login = require('../components/login.vue');
const register = require('../components/register.vue');
const add = require('../components/add.vue');
const list = require('../components/list.vue');

const routes =
    [
        {
            path:'/add',
            component: add
        },
        {
            path:'/list',
            component: list
        },
        {
            path:'/login',
            component: login
        },
        {
            path:'/register',
            component: register
        }
    ];

const router = new VueRouter({ routes:routes });

module.exports = router;