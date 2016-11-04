from flask import Flask,render_template,request,redirect,session


app = Flask(__name__)
app.secret_key='aksdf324234lkjlasdkjf234jkljslkjlk'


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/auth',methods=['post'])
def auth():
    name = request.form.get('name')
    passwd = request.form.get('passwd')
    if name == 'admin' and passwd =='admin':
        session['name'] = 'admin'
    return redirect('/userlist')

@app.route('/userlist')
def userlist():
    if 'name' not in session:
        return redirect('/')
    userlist = []
    with open('user.txt','r') as f:
        for i in f:
           tmp = i.split(":")
           userlist.append(tmp)
        return render_template('userlist.html',userlist=userlist)


@app.route('/userdel',methods=['post'])
def userdel():
    if 'name' not in session:
        return redirect('/')
    name = request.form.get('name')
    print name
    userlist =[]
    with open('user.txt','r') as f:
        tmp = f.readlines()
    with open('user.txt','w') as f:
        for i in tmp:
                
                if name == i.split(':')[0]:
                    continue
                else:
                    f.write('%s' %i)
    return redirect('/userlist') 

            


@app.route('/useradd',methods=['post'])
def useradd():
    if 'name' not in session:
        return redirect('/')
    name = request.form.get('name')
    passwd = request.form.get('password')
    if name == '' or passwd == '':
        return redirect('/userlist')
    else:
        with open('user.txt','a') as f:
            f.write('%s:%s\n'%(name,passwd) )
        return redirect('/userlist')

@app.route('/logout')
def logout():
    session.pop('name')
    return redirect('/')

            

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
