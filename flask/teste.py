import requests

res = requests.get("http://127.0.0.1:5000/api")
print(res.status_code)
print(res.json())

res = requests.post("http://127.0.0.1:5000/api")
print(res.status_code)
print(res.json())

res = requests.put("http://127.0.0.1:5000/api")
print(res.status_code)
print(res.json())

res = requests.delete("http://127.0.0.1:5000/api")
print(res.status_code)
print(res.json())
