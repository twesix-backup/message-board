let app = new Vue
(
    {
        el:'#app',
        router:require('./routers/index'),
        store: require('./stores/index'),
        template:'<wrapper></wrapper>',
        components:
            {
                wrapper:require('./components/app.vue')
            }
    }
);