<template>
    <div>
        <div class="container-fluid">
            <br>
            <h1>留言板</h1>
            <h4 class="text-right">{{account}}</h4>
            <div class="text-right">
                <button class="btn btn-danger" @click="logout()" v-show="$store.state.uid">退出登录</button>
            </div>
            <hr>
            <div class="row">
                <div class="col-sm-3">
                    <ul class="list-group">
                        <router-link to="/register" tag="li" class="list-group-item">注册</router-link>
                        <router-link to="/login" tag="li" class="list-group-item">登录</router-link>
                        <router-link to="/add" tag="li" class="list-group-item">发表留言</router-link>
                        <router-link to="/list" tag="li" class="list-group-item">查看留言</router-link>
                    </ul>
                </div>
                <div class="col-sm-9">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    module.exports =
        {
            data: function()
            {
                return {

                };
            },
            components:
                {
                    login:require('./login.vue'),
                    register:require('./register.vue'),
                    add:require('./add.vue'),
                    list:require('./list.vue')
                },
            computed:
                {
                    account: function()
                    {
                        return this.$store.state.account;
                    },
                    logout: function()
                    {
                        this.$store.commit('logout');
                    }
                }
        }
</script>
<style scoped>
    .list-group-item
    {
        cursor: pointer;
    }
    .router-link-active
    {
        color: #fff;
        background-color: #337ab7;
        border-color: #337ab7;
    }
    .text-right
    {
        text-align: right;
    }
</style>