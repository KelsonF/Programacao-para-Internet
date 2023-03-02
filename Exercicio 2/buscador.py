from bs4 import BeautifulSoup
import requests_cache
import requests

url = 'https://www.bbc.com/portuguese'
requests_cache.install_cache('search_cache')


def busca_termo(keyword, text):
    for index in range(len(text)):
        if text[index:index+len(keyword)] == keyword:
            inicio = max(0, index)
            fim = min(len(text), index+len(keyword) + 20)
            contexto = text[inicio:fim]
            print('-----------------------------------------------------------------------')
            print(f"Trecho encontrado na página {url}: {contexto}")
            print('-----------------------------------------------------------------------')

def search(url, keyword, depth):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    texto = html.get_text()

    busca_termo(keyword, texto)

    if depth > 0:
        links = html.find_all('a')
        for link in links:
            try:
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

    sorted_pages = sorted(page_rank.items(), key=lambda x: x[1], reverse=True)
    print("Páginas ranqueadas:")
    for page, rank in sorted_pages:
        print(f"{page} - referências: {rank}")
     
search(url, 'brasil', 1)