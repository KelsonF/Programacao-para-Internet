import requests
from bs4 import BeautifulSoup

print('Digite as palavras chaves da sua pesquisa: ')
keywords = input('- ')
url = f'https://www.google.com/search?q={keywords}'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for phrases in links:
    formated_text = phrases.getText('href')
    print(formated_text)
