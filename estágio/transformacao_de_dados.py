import requests
import os
import zipfile
import pdfplumber
import pandas as pd
# Definições iniciais
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
PDF= "download/anexo_I.pdf"
CSV = "download/Rol_de_Procedimentos.csv"
ZIP = "download/Teste_Jonanthan.zip"
os.makedirs("download", exist_ok=True)
# Baixar o PDF do Anexo I
response = requests.get(URL, stream=True)
with open(PDF, "wb") as f:
    for chunk in response.iter_content(1024):
        f.write(chunk)
print("PDF baixado com sucesso!")
# Abrindo o PDF e extraindo tabela
tabelas = []
with pdfplumber.open(PDF) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tabelas.extend(table)
# Convertendo a lista de tabelas em um DataFrame exclindo possíveis cabeçalhos duplicados e substituindo as abreviações
df = pd.DataFrame(tabelas)
df = df.drop_duplicates()
substituicoes = {
    "OD": "Procedimentos Odontológicos",
    "AMB": "Procedimentos Ambulatoriais"
}
df.replace(substituicoes, inplace=True)
# Salvar a tabela extraída em CSV
df.to_csv(CSV, index=False, encoding="utf-8-sig")
print("Dados extraídos e salvos em CSV!")
# Compactar o CSV em um arquivo zip
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(CSV, os.path.basename(CSV))
print(f"Arquivo compactado com sucesso: {ZIP}")

if zipfile.ZipExtFile(zip):
    print('tranalhando mais')
else:
    print('rtrabalho concluido')


