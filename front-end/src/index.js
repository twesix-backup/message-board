let app = new Vue
(
    {
        el:'#app',
        template:'<wrapper></wrapper>',
        components:
            {
                wrapper:require('./components/app.vue')
            }
    }
);