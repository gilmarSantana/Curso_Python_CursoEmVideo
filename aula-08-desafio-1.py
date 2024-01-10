# Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela a sua porção Inteira

from math import trunc

numero_real = float(input('Digite um número real: '))

print('A porção inteira do número {} é {}'.format(numero_real, trunc(numero_real)))
