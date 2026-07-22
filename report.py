from fpdf import FPDF
import os


def gerar_relatorio(dados, contador):

    os.makedirs("reports", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, "GitHub Profile Report", ln=True)

    pdf.ln(5)

    pdf.set_font("Helvetica", "", 12)

    pdf.cell(0, 8, f"Name: {dados['name']}", ln=True)
    pdf.cell(0, 8, f"Login: {dados['login']}", ln=True)
    pdf.cell(0, 8, f"Followers: {dados['followers']}", ln=True)
    pdf.cell(0, 8, f"Following: {dados['following']}", ln=True)
    pdf.cell(0, 8, f"Public Repositories: {dados['public_repos']}", ln=True)

    pdf.ln(8)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Languages", ln=True)

    pdf.set_font("Helvetica", "", 12)

    for linguagem, quantidade in contador.items():
        pdf.cell(0, 8, f"{linguagem}: {quantidade}", ln=True)

    pdf.ln(8)

    pdf.cell(0, 8, f"Profile: {dados['html_url']}", ln=True)

    pdf.output(f"reports/{dados['login']}_report.pdf")