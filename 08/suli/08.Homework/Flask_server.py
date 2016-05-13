#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Other: suli
# Time: 2016.04.25 15:24

from flask import request
from flask import redirect
from flask import render_template
from flask import Flask
from flask import session
import operation_dbs
import user
import readlog

app = Flask(__name__)
app.secret_key = "231245"


@app.route("/")
@app.route("/index")
def index():
    # -------------------------------------
    # 判断是否需要初始化数据库
    # -------------------------------------
    status = "init_db"
    sql = "show databases"
    # 是否有 day7 数据库
    db = operation_dbs.execute_mysql(sql)
    # print "db:%s" % db
    # 查询出错,或者有day7数据库则不需要初始化.
    if db != 1:
        for i in db:
            if i[0] == "day7":
                status = ""

    return render_template("/index.html", status=status)


# 显示日志
@app.route("/show")
def show():
    # -------------------------------------
    # 判断session
    # -------------------------------------
    # print len(session)

    # -------------------------------------
    # 分页
    # -------------------------------------
    # 获取总页数
    sql = "select count(*) from day7_homework"
    total = operation_dbs.execute_mysql(sql)
    total_page = int(total[0][0])/10 + 1

    # 获取当前页面
    page = request.args.get("page")
    # 如果当前页面为空,设置为0, 如果不为空,转换为int类型
    if not page:
        page = 0
    else:
        page = int(page)

    # 获取跳转页
    page_go = request.args.get("page_go")
    if page_go:
        page = int(page_go) - 1

    # 判断点的上一页,还是下一页按钮
    Last = request.args.get("last")
    Next = request.args.get("next")
    if Last:
        # 上一页 当前页数-1
        page -= 1
        if page < 0:
            page = 0
    if Next:
        # 下一页, 当前页数+1
        page += 1
        if page >= total_page:
            page = total_page

    # 使用limit 进行分页
    sql = "select * from day7_homework order by num desc limit %s, %s" % (page*10, 10)
    log = operation_dbs.execute_mysql(sql)

    # print "page:%s, last:%s, next:%s" % (page, Last, Next)
    # 把log传给前端, 由前端负责分页显示
    return render_template("/show.html", log=log, page=page, total_page=total_page)


# 初始化数据库
@app.route("/init_db", methods=["post"])
def init_db():
    ip = request.form.get("ip")
    port = int(request.form.get("port"))
    dbuser = request.form.get("dbuser")
    dbpwd = request.form.get("dbpwd")
    u_pwd = request.form.get("u_pwd")

    if ip != "" or port != "" or dbuser != "" or dbpwd != "":
        operation_dbs.init_var(ip, port, dbuser, dbpwd)
        operation_dbs.test()
        print "Init DB"
        operation_dbs.init_db(u_pwd)
        print "Write DB"
        readlog.write_db()
    return redirect("/index")


# 注册
@app.route("/register", methods=['post'])
def register():
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    user.create_user(username, pwd)
    return redirect("/index")


# 登录
@app.route("/login", methods=['post'])
def login():
    # 获取用户名密码
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    u = user.get_user(username)
    # print u
    # print u[0][1]

    if u != ():
        if pwd == u[0][2] and username == "admin":
            session["user"] = "admin"
        if pwd == u[0][2]:
            session["user"] = username
        print "session:%s" % session.get("user")

    return render_template("/index.html", session=session)


# 注销
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/index")


# 用户管理页面
@app.route("/user_mgr")
def user_mgr():
    if session.get("user") == "admin":
        users = user.get_user()
        # print users
        return render_template("/user_mgr.html", users=users)
    else:
        return redirect("/index")


# 修改用户
@app.route("/update_user", methods=['post'])
def update_user():
    u_id = request.form.get("u_id")
    pwd = request.form.get("pwd")

    if u_id != "" and pwd != "":
        user.update_user(u_id, pwd)
    # print "user:%s, pwd:%s" % (u_id, pwd)
    return redirect("/user_mgr")


# 删除用户
@app.route("/del_user", methods=['post'])
def del_user():
    u_id = request.form.get("u_id")
    if u_id != "":
        user.del_user(u_id)
    # print "user:%s" % u_id
    return redirect("/user_mgr")


# 添加用户
@app.route("/add_user", methods=['post'])
def add_user():
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    old_user = user.get_user(username)
    if old_user:
        return redirect("/user_mgr")
    # if username == pwd:
    #     return redirect("/user_mgr")
    if username != "" and pwd != "":
        user.create_user(username, pwd)
    return redirect("/user_mgr")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)











