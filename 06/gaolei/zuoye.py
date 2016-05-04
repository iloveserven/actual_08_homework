from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)
app.secret_key='nicaibuchulai'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
    name = request.form.get('name')
    passwd = request.form.get('passwd')
    if name.strip() == 'admin' and passwd.strip() == 'admin':
        session['admin'] = 'admin'
    return redirect('/data')

@app.route('/logout')
def logout():
    session.pop('admin')
    return redirect('/index')

@app.route('/data')
def data():
    if 'admin' not in session:
        return redirect('/login')
    datalist = []
    with open('user.txt') as f:
        for i in f.readlines():
            tmplist = i.split(':')
            if len(tmplist) == 2:
                datalist.append(tmplist)
    return render_template('data.html',datalist=datalist)

@app.route('/to_adduser',methods=['post'])
def to_adduser():
    to_adduser = request.form.get('to_adduser')
    if to_adduser:
        return redirect('/adduser')
    
@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

@app.route('/adduseroper',methods=['post'])
def adduseroper():
    name = request.form.get('username')
    passwd = request.form.get('passwd')
    with open('user.txt','a') as f:
        f.write('\n%s:%s' % (name,passwd))
    return redirect('/ok')

@app.route('/ok')
def ok():
    return render_template('ok.html')

@app.route('/okoper',methods=['post'])
def okoper():
    answer = request.form.get('answer')
    if answer == 'yes':
        return redirect('/adduser')
    else:
        return redirect('/data')

@app.route('/deluser',methods = ['post'])
def deluser():
    deluser = request.form.get('deluser')
    with open('user.txt') as f:
        tmplist = f.readlines()
        print tmplist
        for i in tmplist:
            if i.strip('\n') == deluser:
                tmplist.remove(i)
                break
    with open('user.txt','w') as f:
        for i in tmplist:
            if i.strip('\n'):
                f.write('%s' % i)
    return redirect('/data')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9023,debug=True)
