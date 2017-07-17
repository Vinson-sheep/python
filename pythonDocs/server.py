from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
	user = request.form['username']
	passw = request.form['password']

	db = pymysql.connect("localhost","root","abc123456","test" )
	cursor = db.cursor()
	sql = "insert into test (username, \
			password) values \
			(%s,%s)" % (user,passw)
	
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
	
	return '<h3>successful</h3>'

if __name__ == '__main__':
    app.run()
	
