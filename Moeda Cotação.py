import requests

# Link que será usado para pegar a cotação atual

url = 'http://economia.awesomeapi.com.br/all/USD-BRL'
url2 = 'http://economia.awesomeapi.com.br/all/BRL-USD'

# Buscar os Dados na API
response = requests.get(url)
response2 = requests.get(url2)

# Verificar se a busca na API funcionou
if response.status_code and response2.status_code == 200:
    dolar_value = response.json()['USD']['low']
    dolar_value2 = response2.json()['BRL']['low']
    print(f'O valor do Dólar atualmente é R${dolar_value}.')
    print(f'O valor do Real está U${dolar_value2}.')
else:
    print('Erro ao buscar o valor do Dólar na API.')