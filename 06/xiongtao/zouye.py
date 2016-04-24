from flask import Flask,render_template,request,redirect,session
import aadat
app = Flask(__name__)
aadat.update_data()
app.secret_key='dnaindi2398r2idnao01nidsnoi12ni'

@app.route('/login')
def login():
        if 'user' in session:
                return redirect('/')
        else:
                return render_template('login.html')

@app.route('/loginaction',methods=['post'])
def loginaction():
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        if user=='admin'and passwd=='admin':
                session['user'] = 'admin'
                return redirect('/')
        else:
                return 'not alloweb'

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect('/login')

@app.route('/')
def index():
        if 'user' not in session:
                return redirect('/login')
        return render_template('data.html',userlist=aadat.file_data.items())
@app.route('/adduser',methods=['post'])
def adduser():
        user = request.form.get('user')
        password = request.form.get('password')
        print 'user is %s and passw is %s'%(user,password)
        if user in aadat.file_data:
                return 'user alrredy eists'
        else:
                aadat.file_data[user]=password
                aadat.update_file()
                return redirect('/')

@app.route('/Deuser')
def Deuser():
        print request.args
        user=request.args.get('user')
        print user
        print aadat.file_data
        if user in aadat.file_data:
                aadat.file_data.pop(user)
                print aadat.file_data
                aadat.update_file()

        return redirect('/')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9999,debug=True)
