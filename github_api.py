import requests

BASE_URL = "https://api.github.com/users"

def buscar_usuario(usuario):
    resposta = requests.get(f"{BASE_URL}/{usuario}")

    if resposta.status_code == 200:
        return resposta.json()

    return None