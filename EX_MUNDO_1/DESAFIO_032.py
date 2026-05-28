'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto

explicação: 
se for divisível por 4, exceto para anos terminados em "00" (centenários), que só são bissextos se 
divisíveis por 400. Exemplos: 2024, 2028 e 2032 são bissextos (divisíveis por 4); 1900 não foi, mas 
2000 foi (divisível por 400)
'''
from datetime import date

anoInformadoInt = int(input('Informe um ano para que lhe retorno se este ano é bissexto, ou digite 0 para verificar o ano atual: '))

if anoInformadoInt == 0:
    anoInformadoInt = date.today().year
    anoInformadoStr = str(anoInformadoInt)
    listaAnoInformado = anoInformadoStr.split()
else:
    anoInformadoStr = str(anoInformadoInt)
    listaAnoInformado = anoInformadoStr.split()
    print(listaAnoInformado) #

if listaAnoInformado[0][len(listaAnoInformado[0])-1] == '0' and listaAnoInformado[0][len(listaAnoInformado[0])-2] == '0': #Se os dois últimos números forem 00 executa o teste de divisao por 400
    testeRest400 = anoInformadoInt % 400
    if testeRest400 == 0: #se for divisivel por 400 é bissexto, caso contrário não é bissexto
        print('O ano {} é bissexto!'.format(anoInformadoInt))
    else:
        print('o ano {} não é bissexto!'.format(anoInformadoInt))
else:
    testeRest4 = anoInformadoInt % 4
    if testeRest4 == 0:
        print('O ano {} é bissexto!'.format(anoInformadoInt))
    else:
        print('O ano {} não é bissexto'.format(anoInformadoInt))