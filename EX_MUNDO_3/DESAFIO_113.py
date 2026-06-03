'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

#Funções
def leiaInt(texto=0):
    """
    -> Aceita a leitura de uma variável tipo INT com validação de dados.\n
    :param texto: Texto que deseja que seja exibido para o usuário
    """
    print('-' * 30)
    while True: 
        try:
           var = int(input(texto).strip())
        except (ValueError, TypeError):
            print('\033[1;31;40mERRO! Digite um número inteiro válido!\033[0m')
        except (TypeError):
            print('\033[1;31;40mEntrada de dados interrompida pelo usuário!\033[0m')
        else:
            break
    return var


def leiaReal(texto=0):
    """
    -> Aceita a leitura de uma variável tipo FLOAT com validação de dados.\n
    :param texto: Texto que deseja que seja exibido para o usuário
    """
    print('-' * 30)
    while True:
        try:
            var = float(input(texto).strip().replace(',','.'))
        except (ValueError, TypeError):
            print('\033[1;31;40mERRO! Digite um número real válido!\033[0m')
        except (TypeError):
            print('\033[1;31;40mEntrada de dados interrompida pelo usuário!\033[0m')
        else:
            break
    return var

#Programa principal
i = leiaInt('Digite um número inteiro: ')
r = leiaReal('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {i} e real {r}'.replace('.', '.'))