from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase


Config = {
  "apiKey": "AIzaSyAGB8GFQN4N4vI_pFsXDVDrHSdpLYYysvk",
  "authDomain": "meet-example2024.firebaseapp.com",
  "databaseURL": "",
  "projectId": "meet-example2024",
  "storageBucket": "meet-example2024.appspot.com",
  "messagingSenderId": "104511305959",
  "appId": "1:104511305959:web:583cc9dde2b008e9b94a42",
  "measurementId": "G-6JPQ4XNJTT",
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



#main route--> signin 
@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            session['user'] = auth.sign_in_with_email_and_password(email, password)
            return render_template("greetings.html")
        except :
            error = "Authentication failed"
            print(error)
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            session['user'] = auth.create_user_with_email_and_password(email, password)
            print(auth.create_user_with_email_and_password(email, password))
            return redirect(url_for('signin'))
        except :
            error = "Authentication failed"
            print(error)
    return render_template("signup.html")



@app.route('/signout')
def signout():
    # session.pop('user')
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('signin'))


if __name__ == '__main__':
 
    app.run( debug=True)

