import requests

def file_download(url, path):
    res = requests.get(url)

    try:
        with open(path, 'wb') as new_file:
            new_file.write(res.content)
            print(f'File save in {path}')
    except:
        print("Erro ao baixar a imagem")

print('Digite a URL da imagem que deseja baixar')
url = input(str('- '))

file_download(url, 'Exercicio 1/imagem.jpg')