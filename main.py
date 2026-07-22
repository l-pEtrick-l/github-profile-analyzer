import requests

usuario = input("Digite um usuário do GitHub: ")

url = f"https://api.github.com/users/{usuario}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    print(f"Nome: {dados['name']}")
    print(f"Login: {dados['login']}")
    print(f"Seguidores: {dados['followers']}")
    print(f"Repositórios: {dados['public_repos']}")
else:
    print("Usuário não encontrado.")