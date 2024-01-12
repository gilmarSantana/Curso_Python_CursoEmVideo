# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trablahos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

i = 1
a = []

while i <= 4:
    n = input('Nome da pessoa {}: '.format(i))
    a.append(n)
    i = i + 1

random.shuffle(a)
print(a)
