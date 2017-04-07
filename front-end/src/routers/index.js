const login = { template: '<login></login>' };
const register = { template: '<register></register>' };
const add = { template: '<add></add>' };
const list = { template: '<list></list>' };

const routes =
    [
        {
            path:'/add',
            component: Vue.extend(require('../components/add.vue'))
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

const router = new VueRouter(routes);

module.exports = router;