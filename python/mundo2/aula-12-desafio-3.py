# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

n1 = 34
n2 = 34

if n1 == n2:
    print('Não há maior nem menor, são iguais.')
elif n1 > n2:
    print(f'O primeiro valor {n1} é maior que o segundo valor {n2}.')
elif n2 > n1:
    print(f'O segundo valor {n2} é maior que o primeiro {n1}.')