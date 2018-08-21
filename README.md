# mysite
test_django
mysql作为Django web项目的数据库，昨天晚上进行了mysql升级，升级到了8.0。数据都没啥问题但是等用Django连接数据库的时候出现报错：

django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: NO)")”
1
这就很神奇了，setting.py文件中的数据库配置没有变过，mysql数据库手动也能登录，库news_db也在。怎么就会报password：no了呢。百撕不得骑姐~ 
赶紧上网查一下原因。看到mysql升级到8.0之后的新特性有一条是更新了密码的加密方式。如果要用原来的Django连接mysql8.0就得将mysql的加密方式转变为原来的方式。 
解决方法如下： 
登录到mysql，并执行如下两条命令

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';  
FLUSH PRIVILEGES;
1
2
同时将setting.py中的password字段改成新设置的newpassword。

password_reset 这个模块是单独装的，要修改源文件里的urls加上 app_name='pwd_reset'