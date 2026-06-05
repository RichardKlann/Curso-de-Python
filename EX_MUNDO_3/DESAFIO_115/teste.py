import csv

while True:
    try:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(row)
    except FileNotFoundError:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='', mode='x') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['NOME', 'IDADE'])
        print('Novo arquivo de dados criado com sucesso!')
    else:
        break