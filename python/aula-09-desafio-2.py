# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitosseparados

from numpy import isin, arange

numero = str(input('Digite um número inteiro de 0 a 9999: '))
template = None

templates = [
    {
        'unidade': '', 'dezena': '', 'centena': '', 'milhar': ''
    },
    {
        'unidade': '', 'dezena': '', 'centena': ''
    },
    {
        'unidade': '', 'dezena': ''
    },
    {
        'unidade': ''
    }
]

intervalos = [
    [0, 9],
    [10, 99],
    [100, 999],
    [1000, 9999]
]

# Fiz esse if para treinar a questão da lista e do uso de módulos
if isin(int(numero), arange(intervalos[3][0], intervalos[3][1])):
    template = templates[0]
    template['unidade'] = numero[3]
    template['dezena'] = numero[2]
    template['centena'] = numero[1]
    template['milhar'] = numero[0]
elif 100 <= int(numero) <= 999:
    template = templates[1]
    template['unidade'] = numero[2]
    template['dezena'] = numero[1]
    template['centena'] = numero[0]
elif 10 <= int(numero) <= 99:
    template = templates[2]
    template['unidade'] = numero[1]
    template['dezena'] = numero[0]
else:
    template = templates[3]
    template['unidade'] = numero[0]

print(template)
