from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    mysql = MySQL()
 
# MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Sql@1234'
    app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    # validate the received values  
    if _name and _email and _password:
        cursor.callproc('sp_createUser',(_name,_email,_password))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'html':'User created successfully !'})
        else:
            return json.dumps({'html':str(data[0])})
       # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
     
 
    

