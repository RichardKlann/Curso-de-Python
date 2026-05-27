'''
Gere um algoritmo que leia a temperatura em graus Celcius e converta para Fahrenheit
1°C = 9/5+32 °F
'''
valor = float(input('Informe a temperatura em graus Celcius: '))
print('A temperatura informada foi {:.2f}°C \nA temperatura convertida para Fahrenheit é: {:.2f}°F'.format(valor, valor*9/5+32))
