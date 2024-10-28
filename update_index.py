import requests

try:
    response = requests.get('http://localhost:3000/indexImages')
    print(response.text)
except:
    raise Exception("Failed to update index")
