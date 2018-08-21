# mysite
Django 2.0.5
mysql 8.0.11
当启动django自带的服务器时，报错2059：
> _mysql_exceptions.OperationalError: (2059, )
> django.db.utils.OperationalError: (2059, )
启动方式为如下：
> python manage.py runserver 0.0.0.0:8000
经过一番查询，调试，最终发现了问题所在。主要就是mysql8.0的问题。
目前最新的mysql8.0对用户密码的加密方式为caching_sha2_password, django暂时还不支持这种新增的加密方式。只需要将用户加密方式改为老的加密方式即可。
解决步骤：
1.登录mysql，连接用户为root。
> mysql -u root -p
2.执行命令查看加密方式
> use mysql;
> select user,plugin from user where user='root';
3.执行命令修改加密方式
> alter user 'root'@'localhost' identified with mysql_native_password by 'yourpassword'
4.属性权限使配置生效
> flush privileges

重设mysql8.0的加密方式后，再次启动django服务器就没有任何问题了。



password_reset 这个模块是单独装的，要修改源文件里的urls加上 app_name='pwd_reset'
