from github_api import buscar_usuario

usuario = input("Digite um usuário do GitHub: ")

dados = buscar_usuario(usuario)

if dados:
    print(f"Nome: {dados['name']}")
    print(f"Login: {dados['login']}")
    print(f"Seguidores: {dados['followers']}")
    print(f"Repositórios: {dados['public_repos']}")
else:
    print("Usuário não encontrado.")