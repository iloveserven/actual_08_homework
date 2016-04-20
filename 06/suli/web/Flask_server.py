#!/usr/bin/env python
# -*- coding:utf-8 -*-

# other: suli
# time: 20160418 16:21
# Flask server

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key = "dffwao3n4"
login_name = []
session = {}


# 从文件中获取users
def get_user_file(file_name):
    users = {}
    try:
        with open(file_name, "rU") as f:
            while True:
                tmp = f.readline()
                if tmp == "":
                    break
                if tmp == "\n":
                    continue
                tmp = tmp.split(":")
                users[tmp[0]] = tmp[1]
    except IOError:
        print "File [ %s ] Not Found" % file_name
    return users


# 将users写入文件
def add_user_file(file_name, user):
    users = get_user_file(file_name)
    tmp = users.keys()
    if user[0] in tmp:
            print "name %s is already exist" % user
            return 2
    try:
        with open(file_name, "ab+") as f:
            tmp = "%s:%s\n" % (user[0], user[1])
            f.write(tmp)
    except IOError:
        print "File [ %s ] Not Found" % file_name
        return 1
    else:
        return 0


# 将匹配的user从文件中删除
def del_user_file(file_name, uname):
    # 先从文件中读取出账户
    users = get_user_file(file_name)

    # 删掉匹配的用户
    if users.get(uname):
        users.pop(uname)

    # 再讲结果写入文件
    try:
        with open(file_name, "wb") as f:
            for k, v in users.items():
                tmp = "%s:%s\n" % (k, v)
                f.write(tmp)
    except IOError:
        print "File [ %s ] Not Found" % file_name
        return 1
    else:
        return 0


# -------------------------------------------------------------------------
# 主页
# -------------------------------------------------------------------------
@app.route("/")
@app.route("/index")
def index():
    """
    主页
    :return:
    """
    return render_template("/index.html")


# -------------------------------------------------------------------------
# 登录
# -------------------------------------------------------------------------
@app.route("/login")
def login():
    """
    登录
    :return:
    """
    if len(session) > 0:
        global login_name
        return render_template("/index.html", name=login_name)
    else:
        return render_template("/login.html")


# -------------------------------------------------------------------------
# 登录操作
# -------------------------------------------------------------------------
@app.route("/login_action", methods=["post"])
def login_action():
    """
    登录操作
    :return:
    """
    name = request.form.get("name")
    global login_name
    login_name = [name]
    pwd = request.form.get("pwd")
    users = get_user_file("user.txt")
    if users.get(name) == pwd+"\n":
        session['user'] = 'admin'
        return render_template("/index.html", name=login_name)
    else:
        return redirect("/index")


# -------------------------------------------------------------------------
# 显示用户
# -------------------------------------------------------------------------
@app.route("/show_users")
def show_users():
    """
    显示用户
    :return:
    """
    if session.get('user') == 'admin':
        return render_template("/show_users.html", users=get_user_file("user.txt"))
    else:
        return redirect("/login")


# -------------------------------------------------------------------------
# 添加用户
# -------------------------------------------------------------------------
@app.route("/add_user")
def add_user():
    """
    添加用户
    :return:
    """
    return render_template("/add_user.html")


# -------------------------------------------------------------------------
# 添加用户操作
# -------------------------------------------------------------------------
@app.route("/add_user_action", methods=["post"])
def add_user_action():
    """
    添加用户操作
    :return:
    """
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    if name == "" or pwd == "":
        status = 3
    else:
        user = [name, pwd]
        status = add_user_file("user.txt", user)
    return render_template("/add_user.html", status=status)


# -------------------------------------------------------------------------
# 退出登录
# -------------------------------------------------------------------------
@app.route("/logout")
def logout():
    if len(session) > 0:
        session.pop('user')
        return """
        <script type="text/javascript">
            alert("logout!")
            window.location.href="/index"
        </script>
        """
    return redirect("/index")


# -------------------------------------------------------------------------
# 删除用户
# -------------------------------------------------------------------------
@app.route("/del_user", methods=["post"])
def del_user():

    del_user_file("user.txt", request.form.get("name"))
    return redirect("/show_users")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)




