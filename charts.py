import matplotlib.pyplot as plt
import os


def gerar_grafico(contador):

    if not contador:
        return

    os.makedirs("images", exist_ok=True)

    linguagens = list(contador.keys())
    quantidade = list(contador.values())

    plt.figure(figsize=(8, 8))

    plt.pie(
        quantidade,
        labels=linguagens,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Programming Languages")

    plt.savefig("images/languages_chart.png")

    plt.close()