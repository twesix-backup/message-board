const store = new Vuex.Store
(
    {
        state:
            {
                account:'278227739@qq.com',
                uid:'1492236936832'
            },
        mutations:
            {
                login: function(state,payload)
                {
                    state.account = payload.account;
                    state.uid = payload.uid;
                },
                logout: function(state)
                {
                    state.account = '未登录';
                    state.uid = '';
                }
            }
    }
);

module.exports = store;