import requests
import os
import zipfile
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
ANEXOS =  ['anexo']
EXTENSOES = ('.pdf', '.zip', '.docx')
#criando diretório para download
os.makedirs('download', exist_ok=True)
#acessando html da página
resposta = requests.get(URL)
soup = BeautifulSoup(resposta.text, 'html.parser')
#buscando anexos
links_encontrados = []
for link in soup.find_all('a', href=True):
    url_arq = urljoin(URL, link['href'])
    nome_arq = url_arq.split('/')[-1].lower()
    if any(anexo in nome_arq for anexo in ANEXOS) and url_arq.endswith(EXTENSOES):
        links_encontrados.append(url_arq)
print('Links encontrados: {}'.format(links_encontrados))
#baixando arquivos
for url in links_encontrados:
    nome_arq = url.split('/')[-1]
    arquivo = requests.get(url, stream=True)
    with open(f'download/{nome_arq}', 'wb') as f:
        for chunk in arquivo.iter_content(1024):
            f.write(chunk)
print('download concluído')
#compactando arquivos
zip_filename = 'anexos.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for url in links_encontrados:
        nome_arq = url.split('/')[-1]
        arquivo_path = f'download/{nome_arq}'
        zipf.write(arquivo_path, os.path.basename(arquivo_path))
print('Arquivos compactados em {}'.format(zip_filename))
