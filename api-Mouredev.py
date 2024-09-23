import requests
import json

url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response = requests.get(url)

data= response.json()

#print(json.dumps(data, indent=4))



for index, pokemon in enumerate(response.json()["results"]):
    pokemon_name = pokemon["name"]
    print(f"#{index + 1} {pokemon_name}")
    