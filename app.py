'''
import flask

print flask.__file__
'''
'''
from flask import Flask
app = Flask(__name__)
import json

def home1():
	return "home1"
@app.route("/",methods=['GET','POST'])
def home():
	result = home1()
	return result+"hello world"
@app.route('/users')
def users():

	return json.dumps(['user1','user2','user3'])

if __name__ == "__main__":
	app.run(port=8889, debug=True)

'''
''''
from flask import Flask

app = Flask(__name__)



#app.config.from_object(__name__)
app.config.from_pyfile('config_file.cfg')


if __name__ == "__main__":
	app.run(port=8889)
	'''
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__,static_folder="static1")

@app.route("/users/")
def users():
	data = pd.read_csv('users.csv')
	columns = data.columns.tolist()
	users = data.values.tolist()
	return render_template('home.html',users=users,columns=columns)
	

@app.route("/home")
def home():

	return render_template('home.html')
	return data
	return "<h1>home file</h1>"
if __name__ == "__main__":
	app.run(port=8889,debug=True)
