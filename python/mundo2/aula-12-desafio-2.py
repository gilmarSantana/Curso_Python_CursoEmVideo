# Escreva um programa que leia um número inteiro
# qualquer e peça para usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Numero: '))
base = int(input('Base de conversão: '))

if base == 1:
    print("O número", numero, ", quando convertido em binário vale:\033[1;36;15m", bin(numero), '\033[m')
elif base == 2:
    print("O número", numero, ", quando convertido em octal vale:\033[1;36;15m", oct(numero), '\033[m')
elif base == 3:
    print("O número", numero, ", quando convertido em hexadecimal vale:\033[1;36;15m", hex(numero), '\033[m')
else:
    pass