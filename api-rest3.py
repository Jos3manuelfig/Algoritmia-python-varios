import requests

def get_user_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error: {response.status_code}')
        return None

user_info = get_user_info('google')
if user_info:
    # Mostrar solo algunos registros
    print("Nombre:", user_info['name'])
    print("Empresa:", user_info['company'])
    print("Biografía:", user_info['bio'])