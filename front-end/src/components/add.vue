<template>
    <div>
        <h3>发表留言</h3>
        <hr>
        <form class="form">
            <div class="form-group">
                <label for="message">留言内容</label>
                <textarea v-model="message" id="message" class="form-control"></textarea>
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

                    }
                }
        }
</script>