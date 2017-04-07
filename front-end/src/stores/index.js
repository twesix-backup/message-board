const store = new Vuex.Store
(
    {
        state:
            {
                account:'未登录',
                uid:''
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