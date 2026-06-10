from time import sleep
from os import system
import csv

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
    try:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                print(f'{row[0]:<10}', end='')
                print(' ' * 15, end='')
                print(f'{row[1]:>3}')

    except FileNotFoundError:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='', mode='x') as csvfile:
            writer = csv.writer(csvfile)
            writer = writer.writerow(['NOME', 'IDADE'])
            print('BANCO DE DADOS CRIADO COM SUCESSO...')


def execOption2():
    titulo('OPÇÃO 2')
    nome = str(input('NOME: ')).upper()
    while True:
        try:
            idade = int(input('IDADE: '))
        except ValueError:
            print('Digite um número válido...')
        else:
            break
    try:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='', mode='a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([nome, idade])
            titulo('NOVO REGISTRO')
            print()
    except FileNotFoundError:
        with open('EX_MUNDO_3\DESAFIO_115\database.csv', newline='', mode='x') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['NOME', 'IDADE'])
            writer.writerow([nome, idade])
            print('BANCO DE DADOS CRIADO!')


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
                    return False
                    