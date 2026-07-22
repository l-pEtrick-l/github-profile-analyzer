from github_api import buscar_usuario, buscar_repositorios
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from collections import Counter
from charts import gerar_grafico
from report import gerar_relatorio

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]GitHub Profile Analyzer[/bold cyan]",
        border_style="blue"
    )
)

usuario = console.input("[bold green]Digite um usuário do GitHub:[/bold green] ")

dados = buscar_usuario(usuario)

if dados:

    tabela = Table(title="GitHub Profile")

    tabela.add_column("Campo", style="cyan", no_wrap=True)
    tabela.add_column("Informação", style="white")

    tabela.add_row("Nome", str(dados["name"]))
    tabela.add_row("Login", str(dados["login"]))
    tabela.add_row("Bio", str(dados["bio"]))
    tabela.add_row("Empresa", str(dados["company"]))
    tabela.add_row("Localização", str(dados["location"]))
    tabela.add_row("Seguidores", str(dados["followers"]))
    tabela.add_row("Seguindo", str(dados["following"]))
    tabela.add_row("Repositórios", str(dados["public_repos"]))
    tabela.add_row("Gists", str(dados["public_gists"]))
    tabela.add_row("Criado em", str(dados["created_at"][:10]))
    tabela.add_row("Atualizado", str(dados["updated_at"][:10]))
    tabela.add_row("Perfil", str(dados["html_url"]))

    console.print(tabela)
    repositorios = buscar_repositorios(usuario)

    tabela_repos = Table(title="Repositórios Públicos")

    tabela_repos.add_column("Nome", style="cyan")
    tabela_repos.add_column("Linguagem", style="green")
    tabela_repos.add_column("⭐ Stars", justify="center")
    tabela_repos.add_column("🍴 Forks", justify="center")

    for repo in repositorios:
        tabela_repos.add_row(
            repo["name"],
            str(repo["language"]),
            str(repo["stargazers_count"]),
            str(repo["forks_count"])
    )

    console.print(tabela_repos)
    # Coleta as linguagens dos repositórios
    linguagens = []

    for repo in repositorios:
        if repo["language"]:
            linguagens.append(repo["language"])

    contador = Counter(linguagens)

    estatisticas = Table(title="Estatísticas das Linguagens")

    estatisticas.add_column("Linguagem", style="cyan")
    estatisticas.add_column("Quantidade", justify="center")

    for linguagem, quantidade in contador.most_common():
        estatisticas.add_row(linguagem, str(quantidade))

    console.print(estatisticas)
    gerar_grafico(contador)
    gerar_relatorio(dados, contador)

    console.print(
        "\n📄 PDF salvo em reports/",
        style="bold green"
    )

    console.print(
        "\n📊 Gráfico salvo em: images/languages_chart.png",
        style="bold green"
    )

    if contador:
        linguagem_principal = contador.most_common(1)[0]

    console.print(
        f"\n🏆 Linguagem mais utilizada: [bold green]{linguagem_principal[0]}[/bold green] "
        f"({linguagem_principal[1]} repositórios)"
    )

else:

    console.print("[bold red]Usuário não encontrado.[/bold red]")