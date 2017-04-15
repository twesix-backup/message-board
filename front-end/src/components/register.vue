<template>
    <div>
        <h3>注册账号</h3>
        <hr>
        <form class="form" @submit.prevent="submit()">
            <div class="form-group">
                <label for="account">账户</label>
                <input type="text" v-model="account" id="account" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="password">账户</label>
                <input type="password" v-model="password" id="password" class="form-control" required>
            </div>
            <br>
            <button type="submit" class="btn btn-default">注册</button>
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
                    password: ''
                };
            },
            methods:
                {
                    submit: function()
                    {
                        let url = `//localhost:8080/register?account=${this.account}&password=${this.password}`;
                        window.fetch(url)
                            .then(function(res)
                            {
                                console.log(res);
//                                if(res.status === 'ok')
//                                {
//                                    alert('注册成功');
//                                }
                            },function(err)
                            {
                                console.log(err);
                                alert('网络错误');
                            });
                        console.log(url);
                    }
                }
        }
</script>