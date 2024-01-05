# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número para saber seu sucessor e seu antecessor: '))

sucessor = n + 1
antecessor = n - 1

print('O antecessor de {} é {} e o sucessor de {} é {}'.format(n, antecessor, n, sucessor))
