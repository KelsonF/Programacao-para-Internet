import requests

print("Digite o cep que deseja procurar")
cep = input(str('- '))

link = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(link)
json = response.json()


print(f'Logradouro:',json['logradouro'])
print(f'Cidade:', json['localidade'])
print(f'Estado:', json['uf']) 