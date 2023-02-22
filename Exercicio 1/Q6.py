import requests
from bs4 import BeautifulSoup

url = 'https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
tabela = soup.find_all('table')

print(tabela)