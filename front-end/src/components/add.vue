<template>
    <div>
        <h3>发表留言</h3>
        <hr>
        <form class="form" @submit.prevent="submit()">
            <div class="form-group">
                <label for="message">留言内容</label>
                <textarea rows="10" v-model="message" id="message" class="form-control"></textarea>
            </div>
            <br>
            <button type="submit" class="btn btn-default">提交</button>
        </form>
    </div>
</template>
<script>
    module.exports =
        {
            data: function()
            {
                return {
                    message: '输入你的留言...'
                };
            },
            methods:
                {
                    submit: function()
                    {
                        if(this.$store.state.uid)
                        {
                            let url = `//localhost:8080/add?uid=${this.$store.state.uid}&message=${this.message}`;
                            console.log(url);
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
                        }
                        else
                        {
                            alert('您没有登录');
                        }
                    }
                }
        }
</script>