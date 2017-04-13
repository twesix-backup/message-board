# 留言板

## 小组成员

组长:孟政元

| 姓名        | 学号      | 教学号    | 工作量百分比 |
|-------------|:--------:|:--------:|:----------:|
| 孟政元       | 21140821 | 53140821 | 20%        |
| 陈良勇       | 21140821 | 53140821 | 20%        |
| 陈靖宇       | 21140821 | 53140821 | 20%        |
| 李锦涛       | 21140821 | 53140821 | 20%        |
| 侍俊杰       | 21140821 | 53140821 | 20%        |

## 简介

该应用为一个简单的留言板小应用,功能如下:

1. 注册
2. 登录
3. 留言
4. 查看留言(包括自己的和别人的)
5. 修改自己的留言
6. 删除自己的留言


## 架构及分工说明

> 后台基于python和web.py框架,前端采用Vue框架,前后端的交互采用ajax

#### 前端(负责人:孟政元)

前端采用静态的html做界面,使用了vue框架来进行数据的渲染和展示,用vue-router来完成
模块之间的路由,用vuex来完成用户登录状态的管理,网页与后台之间的交互采用ajax的形式
数据交互格式为json格式

前端分成4个基本模块,一个导航模块.通过路由在不同的模块之间切换,展现不同的功能

1. 导航模块:
   通过url的hash值来确定当前导航状态,一遍展现不同的功能呢模块

2. 注册模块:
   负责注册功能

3. 登录模块:
   负责登录功能,当用户登录成功时,与登录相关的信息会保存在vuex的store中,从而控制相关的
   行为和功能

4. 留言模块:
   用户发表自己的留言,将相关信息提交到回台服务程序,并由后台程序保存在数据库中

5. 列表模块:
   负责展示所有用户的所有留言
   对于自己的留言,用户可以选择修改或者删除,对于他人的留言,用户只能查看

#### 后台(负责人:分工待定)

#### 架构

架构采用web.py框架,监听在localhost的8080端口上

请求全部采用get方式,参数包含在url里面

返回值全部采用json格式,http状态全部为200,不管是不是出现了错误和失败,错误和失败从返回
值的status来判定

需要实现的功能列表如下:

1. 注册

   //localhost:8080/register?account=user_account&password=user_password

   ```
   {
       status: 'ok'| 'error',
       message: 'error'
   }
   ```

2. 登录

   //localhost:8080/login?account=user_account&password=user_password

   ```
   {
       status: 'ok' | 'error'
       message: 'uid' | 'error'
   }
   ```

3. 发表留言

   //localhost:8080/add?uid=user_id&message=the_message

   ```
   {
       status: 'ok' | 'error'
       message: 'error'
   }
   ```

4. 修改留言

   //localhost:8080/update?uid=user_id&message=the_message&mid=message_id

   ```
   {
       status: 'ok' | 'error'
       message: 'error'
   }
   ```

5. 删除留言

   //localhost:8080/delete?mid=message_id

   ```
   {
       status: 'ok' | 'error'
       message: 'error'
   }
   ```

6. 留言列表

   //localhost:8080/list?uid=user_id

   ```
   [
       {
           message_content: 'lalalala',
           // 这条留言是这个用户发表的,所以有message_id
           message_id: 'message id'
       },
       {
           message_content: 'lalala'
           // 这条留言不是这个用户发表的,他只能看,不能改
       },
       ...
   ]
   ```
