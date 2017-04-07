<template>
    <div>
        <h3>注册账号</h3>
        <hr>
        <form class="form" @submit.prvent="submit()">
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
                        console.log(url);
                    }
                }
        }
</script>