from flask import Flask, render_template
import logging
from flask_sqlalchemy import SQLAlchemy
#logging.basicConfig(filename="log1.txt", level=logging.DEBUG,format ="%(astime)s->%(levelname)s->%(message)s" )



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:root@localhost/db3"
db = SQLAlchemy(app) 
@app.errorhandler(404)
def page_notfound(msg):
	return render_template('404.html',msg=msg)

@app.route('/')
def home():
	app.logger.info("render to home")
	return "Hello world"

if __name__ == "__main__":

	handler = logging.FileHandler("log3.txt")
	formater = logging.Formatter("%(asctime)s->%(levelname)s->%(message)s")
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(formater)
	app.logger.addHandler(handler)
	app.run(debug=True)