let app = new Vue
(
    {
        el:'#app',
        router:require('./routers/index'),
        template:'<wrapper></wrapper>',
        components:
            {
                wrapper:require('./components/app.vue')
            }
    }
);