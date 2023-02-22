import requests
from bs4 import BeautifulSoup

url = 'https://openai.com/blog/chatgpt/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

print("Qual tag voce deseja procurar ?")
tecla = input("Resposta: ")

links = soup.find_all(tecla)
for link in links:
    texto = link.getText()
    print('-', texto)
