from app import db

class users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String,unique=True)
	address = db.Column(db.String)

	def __init__(self,username, address):
		self.username = username
		self.address = address

if __name__ == "__main__":
	db.create_all()
