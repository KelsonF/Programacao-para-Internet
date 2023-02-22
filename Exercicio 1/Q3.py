import requests
from bs4 import BeautifulSoup

url = 'https://www.flamengo.com.br/'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
text = soup.getText()

print("Qual termo voce deseja procurar ?")
termo = input(str("- "))


