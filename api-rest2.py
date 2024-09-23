import requests

# URL de la API de GitHub
url = 'https://api.github.com/users/octocat'

# Hacer una solicitud GET
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')