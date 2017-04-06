## 架构及分工说明

> 该应用为一个简单的留言板小应用,后台基于python和web.py框架
  前端采用Vue框架,前后端的交互采用ajax

### 前端(负责人:孟政元)

### 后台(负责人:分工待定)

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
