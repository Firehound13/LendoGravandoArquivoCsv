import csv
import requests
from config import URL
import pandas as pd

# Requisição para o link do arquivo csv
response = requests.get(URL)
print(response.content)

# Criando um arquivo chamado 'covid19.csv' e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    write = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        write.writerow(linha.decode('utf-8').split(','))

# Abrir um arquivo .csv a partir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
        print(linha)
        if linha[2] == 'Brazil':
            print(f"Linha # {leitor_exemplo.line_num} {linha[4]}")

# Usando o módulo pandas pra ler arquivos
arquivo.csv == pd.read_csv(ARQUIVO_CSV, usecols=['location', 'date', 'total_cases, total_deaths']), index_col=='date'

# Mostrando os 10 primeiros
print(arquivo_csv.head(10).to_string())

# Filtrar os dados
print(arquivo_csv.loc[arquiv_csv.location == 'Brazil']) & (arquivo.csv == '2020-06-12')
