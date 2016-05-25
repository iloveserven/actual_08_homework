from flask import Flask,render_template,request,redirect,session
app =Flask(__name__)
app.secret_key='dnaindi2398r2idnao01nidsnoi12ni'
#@app.route('/')
#def index():
#       return redirect('/data')

@app.route('/')
def index():
        if 'user' not in session:
                return redirect('/login')
        user_lst = []
        with open('./user.txt') as f:
                for line in f:
                        tmp =line.split(':')
                        if len(tmp)==2:
                                user_lst.append(tmp)
        return render_template('/indexb.html',res_lst=user_lst,user='admin')

@app.route('/adduser',methods=['post'])
def adduser():
        user= request.form.get('user')
        password = request.form.get('password')
        with open('./user.txt','a') as f:
                f.write('\n'+user+':'+ password)
        return redirect('/')

@app.route('/deleteuser',methods=['post'])
def deleteuser():
        dict_t={}
        user_lst = []
        user=request.form.get('user')
        with open('./user.txt','r') as f:
                for line in f:
                        tmp =line.split(':')
                        if len(tmp)==2:
                                dict_t[tmp[0]] = tmp[1]
                                user_lst.append(tmp[0])
        dict_t.pop(user)
        with open('./user.txt','w') as f:
                for user in user_lst:
                        for key,val in dict_t.items():
                                if user == key:
                                        f.write(key + ':' + val+'\n')
        return redirect('/')

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect('/login')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
        user=request.form.get('user')
        password = request.form.get('password')
        if user == 'admin' and password == 'admin':
                session['user'] = 'admin'
        return redirect('/')

if __name__=='__main__':
        app.run(host='0.0.0.0',port=10001,debug=True)
