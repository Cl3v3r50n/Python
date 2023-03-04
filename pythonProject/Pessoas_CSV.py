import csv

# Dados a serem gravados no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Sexo'],
    ['Cleverson', 40, 'M'],
    ['Drika', 31, 'F'],
    ['Maria Clara', 2, 'F'],
    ['Sofhia', 1, 'F']
]

# Nome do arquivo CSV que será criado
nome_arquivo = 'pessoas.csv'

# Abre o arquivo CSV em modo de escrita
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    # Cria um objeto para escrever no arquivo CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escreve os dados no arquivo CSV
    for linha in dados:
        escritor_csv.writerow(linha)

print(f'O arquivo CSV {nome_arquivo} foi gerado com sucesso!')
