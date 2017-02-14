from flask import Flask, render_template, request, session, redirect, url_for
from flask.ext.api import status
app = Flask(__name__)
app.secret_key = "abcdf"
import os
from db_schema import insert_users, browse_users

@app.route("/", methods=['GET','POST'])
def home():
	message=""
	if request.method == "POST":
		data = request.form
		result = insert_users(data)
		if result:
			profilepic = request.files['profilepic']
			static_folder_path = app.static_folder
			filename = profilepic.filename
			path = os.path.join(static_folder_path,'images',filename)
			profilepic.save(path)
			message = "user inserted successfully"
	return render_template("home.html", message=message)

@app.route("/login", methods=['GET','POST'])
def login():
	message=""
	if request.method=="POST":
		data = request.form
		users = browse_users(data)
		if users:
			message="Login successfully"
			session['user'] = users
			return render_template("index.html",message=message)
		else:
			message="Login failed"
	return render_template("login.html", message=message)

@app.route("/index",methods=['POST','GET'])
def index():

	if "user" in session:
		return render_template('index.html')
	else:
		login_url = url_for('login')
		return redirect(login_url)
		#return redirect('/login')
		#return render_template("login.html")
@app.route("/logout")
def logout():
	session.pop('user')
	return redirect("/login")
@app.route("/createusers",methods=['POST'])
def user_create():
	data = request.json
	result = insert_users(data)
	if result:
		return "user created successfully",status.HTTP_201_CREATED
	else:
		return "user not created",status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":

	app.run(debug=True)