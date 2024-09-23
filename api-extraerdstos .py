import requests
import json 

# URL de la API de GitHub
url = 'https://api.github.com/users/octocat'

def mostrar():
    # Hacer una solicitud GET
    response = requests.get(url)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        data = response.json()
        
        # Extraer datos específicos
        nombre = data.get('name')
        biografia = data.get('bio')
        repos_publicos = data.get('public_repos')
        seguidores = data.get('followers')
        siguiendo = data.get('following')
        blog = data.get('blog')
        
        # Mostrar datos formateados
        print(f"Nombre: {nombre}")
        print(f"Biografía: {biografia}")
        print(f"Repositorios Públicos: {repos_publicos}")
        print(f"Seguidores: {seguidores}")
        print(f"Siguiendo: {siguiendo}")
        print(f"Blog: {blog}")
    else:
        print(f'Error: {response.status_code}')

mostrar()