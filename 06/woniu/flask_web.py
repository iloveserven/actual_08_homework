

from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key='/sad/ikhkj?jklhd-908182903jk43-42348038401'

@app.route('/')
def index():
    username = 'admin'
    return render_template('index.html',username=username)
    #return '<input type="text" value="123">'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/loginaction',methods=['post'])
def loginaction():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    if user=='admin' and passwd=='admin':
        session['user'] = 'admin'
    return redirect('/data')


@app.route('/data')
def data():
    if 'user' not in  session:
        return redirect('/login')
#    name = request.args.get('name')
#    age = request.args.get('age')
#    return 'hello '+name+age
#    html_str = '<table border="1">'
    userlist = []
    with open('user.txt') as f:
        for line in f:
            tmp = line.split(':')
            if len(tmp)==2:
                userlist.append(tmp)
#        for line in f:
#            tmp = line.split(':')
#            if len(tmp)==2:
#                html_str+='<tr><td>%s</td><td>%s</td></tr>'%(tmp[0],tmp[1])
#    html_str+='</table>'
    return render_template('data.html',userlist=userlist)

@app.route('/adduser',methods=['post'])
def adduser():
    print request.args
    user = request.form.get('user')
    password = request.form.get('password')
    print 'user is %s and paswd is %s'%(user,password)
    with open('user.txt','a') as f:
        f.write('\n'+user+':'+password)
    return redirect('/data')
@app.route('/test/<username>')
def test(username):
    return 'hello'+username



if __name__=='__main__':
    app.run(host='0.0.0.0',port=9093,debug=True)



