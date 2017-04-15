<template>
    <div>
        <h3>留言列表</h3>
        <hr>
        <div v-for="message in messages">
            <h4>{{ message.account }}</h4>
            <div class="content">
                <textarea class="form-control" :id="message.mid" title="留言内容" rows="5"
                          :value="message.message" :disabled="!message.mid">
                </textarea>
            </div>
            <br>
            <div class="actions" v-if="message.mid">
                <button @click="update(message.mid)" class="btn btn-default">保存修改</button>
                <button @click="remove(message.mid)" class="btn btn-danger">删除留言</button>
            </div>
            <hr>
        </div>
    </div>
</template>
<script>
    module.exports =
        {
            data:function()
            {
                return {
                    messages:
                        [
                            {
                                message: '简介：赛车手阿浪（邓超 饰）一直对父亲（彭于晏 饰）反对自己的赛车事业耿耿于怀，' +
                                '在向父亲证明自己的过程中，阿浪却意外卷入了一场奇妙的冒险。他在这段经历中结识了一群兄弟' +
                                '好友，一同闯过许多奇幻的经历，也对自己的身世有了更多的了解。',
                                mid: 'message_1',
                                account: 'twesix'
                            },
                            {
                                message: '简介：《熊出没·奇幻空间》则继续围绕“森林”做题目，讲述熊大、熊二和光头强与' +
                                '金鹿角守护者——鹿族女孩协力保护金鹿角，击垮反派，最终让森林复苏的故事。',
//                                mid: 'message_2',
                                account: 'unknown'
                            }
                        ]
                };
            },
            methods:
                {
                    update: function(mid)
                    {
                        let url = `//localhost:8080/update?mid=${mid}&message=${document.getElementById(mid).value}`;
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
                    },
                    remove: function(mid)
                    {
                        let url = `//localhost:8080/delete?mid=${mid}`;
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
<style>
    .actions
    {
        text-align: right;
        margin-right:20px;
    }
</style>