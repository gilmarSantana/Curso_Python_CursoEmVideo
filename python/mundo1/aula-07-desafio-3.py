# Desenvolva um programa que leia as duas notas de um aluno, calcule
# e mostre a sua média

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

print('O aluno teve sua primeira nota {} e a segunda {},'
      ' com isso sua média é {}'.format(n1, n2, media))

