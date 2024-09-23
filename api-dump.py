import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

def mostrar():
    
        peticion = requests.get(url)
        peticion.raise_for_status()
        productos = peticion.json()
        print(json.dumps(productos, indent=2))  # Indentación de 2 espacios
    

mostrar()