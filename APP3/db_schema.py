from app import db

class Users(db.Model):
	__table__ = "users_table"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String,unique=True)
	address = db.Column(db.String)

	def __init__(self,username, address):
		self.username = username
		self.address = address
class Posts(db.Model):
	desc = db.Column(db.String)
	user_id = db.Column(db.db.ForeignKey('users_table.id'))

if __name__ == "__main__":
	db.create_all()
