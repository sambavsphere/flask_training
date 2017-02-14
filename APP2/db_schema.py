import sqlite3
def connect():
	con  =sqlite3.connect('db1.db')
	cur = con.cursor()
	return con,cur
def insert_users(data):
	"""
	param: data, type= dict
	desc: 
	"""
	err=""
	inserted  = ""
	con,cur = connect()
	try:
		query = "insert into users values('%(username)s','%(password)s','%(address)s')"%data
		cur.execute(query)
		inserted = True
	except Exception as err:
		pass
	finally:
		con.commit()
		cur.close()
		con.close()
	if inserted:
		return True
	else:
		return err
def browse_users(data):
	result = []
	try:
		query = "select * from users where username='%(username)s' and password='%(password)s'"%data
		con,cur  =connect()
		cur.execute(query)
		result = cur.fetchall()
	except Exception as err:
		pass
	finally:
		cur.close()
		con.close()
	return result





if __name__ == "__main__":
	con,cur = connect()
	query = "create table users(username varchar(50),password varchar(50), address varchar(220))"
	cur.execute(query)

