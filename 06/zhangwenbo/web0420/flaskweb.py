#encoding=utf-8

from flask import Flask,render_template,request,redirect,session 
app = Flask(__name__) 
app.secret_key='sddddfrg4thdnaindi2398r2idnao01nidsnoi12ni' 
 
@app.route('/') 
def index(): 
        username = 'admin' 
        return render_template('index.html',username=username) 
 
@app.route('/data') 
def user_01(): 
        if 'user' not in session: 
            return redirect('/login') 
        userlist = [] 
        with open('./user.txt') as f: 
            for line in f: 
                tmp = line.split(':') 
                if len(tmp) ==2: 
                    userlist.append(tmp) 
        return render_template('data.html',userlist=userlist) 
 
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
 
@app.route('/adduser',methods=['post']) 
def adduser(): 
        user = request.form.get('user') 
        password = request.form.get('password') 
        with open('./user.txt','a') as f: 
            f.write('\n'+user+':'+password) 
        return redirect('/data') 

@app.route('/delete',methods=['post'])
def delete():
	user = request.form.get('user')
	with open('./user.txt','r') as f:
            arr=[]
	    arr1=[]
	    d=f.readlines()
	    for i in d:
		c = i.split(':')
		if len(c) ==2:
		    arr.append(c[0])
		    arr1.append(c[1])
	    dict_f = dict(zip(arr,arr1))
 	    del dict_f[user]
	with open('./user.txt','w') as f:
	    for k,v in dict_f.items():
		f.write(k+':'+v)
	return redirect('/data')
 
if __name__ == '__main__': 
        app.run(host='0.0.0.0',port=10000,debug=True)
