import requests

url='http://wttr.in/Belo+Horizonte'

response= requests.get(url)
data=response.text
print(data)
