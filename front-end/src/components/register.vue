<template>
    <div>
        <h3>注册账号</h3>
        <hr>
        <form class="form">
            <div class="form-group">
                <label for="account">账户</label>
                <input type="text" v-model="acount" id="account" class="form-control">
            </div>
            <div class="form-group">
                <label for="password">账户</label>
                <input type="text" v-model="password" id="password" class="form-control">
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
                    account: '账户',
                    password:'密码'
                };
            },
            methods:
                {
                    submit: function()
                    {

                    }
                }
        }
</script>