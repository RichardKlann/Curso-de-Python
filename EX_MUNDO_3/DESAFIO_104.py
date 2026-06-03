'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python, só que fazendo validação para aceitar apenas um valor numérico.

ex: 
n = leiaInt('Digite um n')
'''
#Funções
def leiaInt(texto):
    """
    -> Aceita a leitura de uma variável tipo INT com validação de dados.\n
    :param texto: Texto que deseja que seja exibido para o usuário
    """
    print('-' * 30)
    while True: 
        var = input(texto).strip()
        if var.isnumeric():
            var = int(var)
            break
        else:
            print('\033[1;31;40mERRO! Digite um número inteiro válido!\033[0m')
    return var


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')