<template>
    <div>
        <h3>登录</h3>
        <hr>
        <form class="form" @submit.prevent="submit()">
            <div class="form-group">
                <label for="account">账户</label>
                <input type="text" v-model="account" id="account" class="form-control">
            </div>
            <div class="form-group">
                <label for="password">账户</label>
                <input type="password" v-model="password" id="password" class="form-control">
            </div>
            <br>
            <button type="submit" class="btn btn-default">登录</button>
        </form>
    </div>
</template>
<script>
    module.exports =
        {
            data: function()
            {
                return {
                    account: '',
                    password:''
                };
            },
            methods:
                {
                    submit: function()
                    {
                        let self = this;

                        let url = `//localhost:8080/login?account=${this.account}&password=${this.password}`;
                        console.log(url);

                        window.fetch(url)
                            .then(function(res)
                            {
                                console.log(res);
                                if(res.ok)
                                {
                                    res.json().then(function(res)
                                    {
                                        console.log(res);
                                        if(res.status == 'ok')
                                        {
                                            self.$store.commit(
                                                'login',
                                                {
                                                    account: self.account,
                                                    uid: res.message
                                                });
                                        }
                                        else
                                        {
                                            alert(res.message);
                                        }
                                    })
                                }
                                else
                                {
                                    alert('网络错误');
                                }
                            });
                    }
                }
        }
</script>