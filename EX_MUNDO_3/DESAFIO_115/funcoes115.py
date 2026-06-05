from time import sleep
from os import system

def titulo(msg):
    """
    Cria uma mensagem em forma de título
    :param msg: mensagem que deseja colocar no meio do título
    """
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)

def showMenu():
    titulo('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')

def execOption1():
    titulo('OPÇÃO 1')


def execOption2():
    titulo('OPÇÃO 2')


def execOption3():
    titulo('Saindo do sistema... Até logo!')


def userEnterOption():
    while True:
        try:
            option = int(input('Sua Sua Opção: '))
        except:
            print()
            print('OPÇÃO DIGITADA INVÁLIDA!')
            sleep(1)
            system('cls')
            showMenu()
        else:
            if option <= 0 or option > 3:
                print()
                print('OPÇÃO NÃO EXISTE... TENTE NOVAMENTE')
                sleep(1)
                system('cls')
                showMenu()
            else:
                if option == 1:
                    execOption1()
                    break
                elif option == 2:
                    execOption2()
                    break
                elif option == 3:
                    execOption3()
                    break