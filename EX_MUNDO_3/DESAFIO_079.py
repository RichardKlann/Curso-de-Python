'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista dentro dela, este não será adicionado. No final, serão exibidos todos os valores únicos
digitados em ordem crescente.
'''

valores = []

while True:
    entrada = int(input('\nDigite um número inteiro: '))
    if entrada in valores:
        print(f'Este número já foi digitado. Não será adicionado na lista...\n')
    else:
        valores.append(entrada)
        print(f'O valor {entrada} foi adicionado na lista com sucesso!\n')

    continua = input('Deseja continua [S/N]: ')[0]
    if continua in 'Nn':
        break
    
'''    if valores.count(entrada) > 0:
        print('Este número já foi digitado. Não será adicionado na lista...\n')
    else:
        valores.append(entrada)
        print(f'O valor {entrada} foi adicionado na lista com sucesso...\n')
    continua = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if continua in "N":
        break'''

valores.sort()
print(valores)