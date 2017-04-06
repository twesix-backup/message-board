<template>
    <div>
        <ul>
            <router-link to="/register" tag="li">注册</router-link>
            <router-link to="/login" tag="li">登录</router-link>
            <router-link to="/add" tag="li">发表留言</router-link>
            <router-link to="/list" tag="li">查看留言</router-link>
        </ul>
        <router-view></router-view>
    </div>
</template>
<script>
    module.exports =
        {
            data: function()
            {
                return {

                };
            }
        }
</script>