<template>
    <div>
        <h3>留言列表</h3>
        <hr>
        <div v-for="message in messages">
            <div class="content">
                <textarea class="form-control" :id="message.message_id" title="留言内容" rows="5"
                          :value="message.message_content" :disabled="!message.message_id">
                </textarea>
            </div>
            <br>
            <div class="actions" v-if="message.message_id">
                <button @click="update(message.message_id)" class="btn btn-default">保存修改</button>
                <button @click="remove(message.message_id)" class="btn btn-danger">删除留言</button>
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
                    messages: []
                };
            },
            methods:
                {
                    update: function(mid)
                    {
                        let self = this;

                        let url = `//localhost:8080/update?mid=${mid}&message=${document.getElementById(mid).value}`;
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
                                            alert('保存成功');
                                            self.list();
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
                    },
                    remove: function(mid)
                    {
                        if(!confirm('确认要删除这条留言'))
                        {
                            return ;
                        }
                        let self = this;

                        let url = `//localhost:8080/delete?mid=${mid}`;
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
                                        self.list();
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
                    },
                    list:function()
                    {
                        let self = this;

                        let url = `//localhost:8080/list?uid=${this.$store.state.uid}` ;
                        console.log(url);

                        window.fetch(url)
                            .then(function(res)
                            {
                                console.log(res);
                                if(res.ok)
                                {
                                    res.json().then(function(res)
                                    {
                                        self.messages = [];
                                        res.forEach(function(e)
                                        {
                                            self.messages.push(e);
                                        })
                                    })
                                }
                                else
                                {
                                    alert('网络错误');
                                }
                            });
                    }
                },
            mounted:function()
            {
                this.list();
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