# 作业：新增一个机器管理页面（增删改查）

* 字段：
    * 主机名 输入框
    * 内存 用小滑块 支持2G到32G之间
    * 过期时间 http://jqueryui.com/datepicker/ 格式是年-月-日  2016-05-21
    * 负责人邮箱 输入框
    * 所有字段都可以修改
    * 支持增删改查 用sweetalert做信息提示
    * 考虑一下左侧页面导航的高亮
    
    
    
    tablename:liuyongzhan.zichan
    id int
    hostname varchar(50)
    cpu varchar(50)
    mem int
    exdate varchar(50)
    author varchar(50)
    note varchar(400)
    
   mysql> create table zichan (id int not null auto_increment primary key,hostname varchar(50) not null,cpu varchar(50) not null,mem int not null,exdate varchar(50) not null,author varchar(50) not null,note varchar(400) not null);

