# Escreva um programa que leia um número inteiro
# qualquer e peça para usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Numero: '))
base = int(input('Base de conversão: '))

if base == 1:
    # Desenvolvido por Prô Terra - MakerZine
    # Para mais detalhes, acesse: https://www.makerzine.com.br

    numero_digitado = numero
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = numero
        lista.insert(0, resto)
        quociente = numero // 2
        numero = quociente

    binario = ''.join([str(item) for item in lista])
    print("O número", numero_digitado, ", quando convertido em binário, vale:", binario)
elif base == 2:
    pass
elif base == 3:
    pass
else:
    pass