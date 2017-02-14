import requests
resp = requests.post("http://localhost:5000/createusers",
json={'username':"name1",'password':"passsword1","address":"ad2"})
print resp.status_code
