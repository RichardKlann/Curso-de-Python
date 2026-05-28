'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos
'''

ptermo = int(input('Informe o primeiro termo da razão: '))
razao = int(input('Informe a razão da PA: '))
c = 10

while c >= 0:
    if c != 0:
        print(ptermo, end = ' -> ')
        ptermo = ptermo + razao
    else:
        print(ptermo, end = '')
        ptermo = ptermo + razao
    c -= 1

print('\n\nForam mostrados os 10 primeiros termos da PA.')

continua = True
while continua == True:
    escolha = int(input('\nGostaria de receber mais números da sequência? Informe quantos quer ou 0 se não quer: '))
    if escolha == 0:
        print('FIM')
        break
    else:
        c = escolha
        while c >= 0:
            if c != 0:
                print(ptermo, end = ' -> ')
                ptermo = ptermo + razao
            else:
                print(ptermo, end = '')

            c -= 1