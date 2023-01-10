import requests

r = requests.get("https://raw.githubusercontent.com/shehraj123/cmput404-lab1/main/request_ver.py")
print(r.text)
