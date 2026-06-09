import csv

nome = str(input('NOME: ')).upper()
idade = int(input('IDADE: '))
    
with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='', mode='x') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([nome, idade])
    print('BANCO DE DADOS CRIADO!')