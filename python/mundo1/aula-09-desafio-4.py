# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = 'Gilmar Santana Lins'

teste = 'silva' in nome.lower()

if teste:
    print('Tem Silva')
else:
    print('Não tem Silva')