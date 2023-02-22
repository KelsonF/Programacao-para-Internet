import requests
from bs4 import BeautifulSoup

url = 'https://openai.com/blog/chatgpt/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
    texto = link.getText('href')
    print('-', texto)
