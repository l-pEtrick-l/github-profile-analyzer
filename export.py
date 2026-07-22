import json
import os


def exportar_json(dados, repositorios, contador):

    os.makedirs("exports", exist_ok=True)

    resultado = {
        "profile": {
            "name": dados["name"],
            "login": dados["login"],
            "followers": dados["followers"],
            "following": dados["following"],
            "public_repositories": dados["public_repos"],
            "profile_url": dados["html_url"]
        },
        "languages": dict(contador),
        "repositories": [
            {
                "name": repo["name"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"]
            }
            for repo in repositorios
        ]
    }

    with open(
        f"exports/{dados['login']}.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(resultado, arquivo, indent=4, ensure_ascii=False)