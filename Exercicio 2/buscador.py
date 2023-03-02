from bs4 import BeautifulSoup
import re
import requests_cache
import requests

keyword = str(input('Digite a palavra que deseja: '))
url = 'https://www.bbc.com/portuguese'
requests_cache.install_cache('search_cache')


def busca_termo(text):
    for termo in text:
        texto = termo.get_text()
        if texto != '':
            print('-------------------------------------')
            print(f'Frase: {texto} --> Url: {url}')
            print('-------------------------------------')

def search(url, keyword, depth):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    texto =  html.find_all(string=re.compile(keyword))

    busca_termo(texto)
    page_rank = {}

    links = html.find_all('a')
    for link in links:
        if 'href' in link.attrs:
            next_url = link.attrs['href']
            if next_url.startswith('http'):
                if next_url in page_rank:
                    page_rank[next_url] += 1
                else:
                    page_rank[next_url] = 1
                    

    while depth > 0:
        links = html.find_all('a')
        for link in links:
            try:
                if link not in page_rank:
                    url_ = link.get('href')
                    if url != None:
                        if url.startswith('http'):
                            search(url_, keyword, depth-1)
                        else:
                            search(url+url_, keyword, depth-1)
            except requests.exceptions.MissingSchema:
                continue
            except requests.exceptions.InvalidSchema:
                continue

        depth = depth-1

    sorted_pages = sorted(page_rank.items(), key=lambda x: x[1], reverse=True)
    print("Páginas ranqueadas:")
    for page, rank in sorted_pages:
        print(f"{page} - referências: {rank}")
     
search(url, keyword, 1)