import requests

# URL de la API
url = "https://jsonplaceholder.typicode.com/posts"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    posts = response.json()
    
    # Imprimir los primeros 5 posts
    for post in posts[:5]:
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print("Error al hacer la solicitud:", response.status_code)