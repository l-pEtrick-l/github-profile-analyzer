from github_api import buscar_usuario

usuario = input("Digite um usuário do GitHub: ")

dados = buscar_usuario(usuario)

if dados:

    print("=" * 50)
    print("        GITHUB PROFILE ANALYZER")
    print("=" * 50)

    print(f"Nome: {dados['name']}")
    print(f"Login: {dados['login']}")
    print(f"Bio: {dados['bio']}")
    print(f"Empresa: {dados['company']}")
    print(f"Localização: {dados['location']}")
    print(f"Blog/Site: {dados['blog']}")
    print(f"Email Público: {dados['email']}")
    print(f"Twitter: {dados['twitter_username']}")
    print(f"Seguidores: {dados['followers']}")
    print(f"Seguindo: {dados['following']}")
    print(f"Repositórios Públicos: {dados['public_repos']}")
    print(f"Gists Públicos: {dados['public_gists']}")
    print(f"Criado em: {dados['created_at']}")
    print(f"Última atualização: {dados['updated_at']}")
    print(f"Avatar: {dados['avatar_url']}")
    print(f"Perfil: {dados['html_url']}")

    print("=" * 50)

else:
    print("Usuário não encontrado.")