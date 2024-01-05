# Escreva um programa que
# leia um valor em metros e o exiba convertido
# em centímetros e milímetros

metros = float(input('Digite quantos metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('Em {:.0f} metros tem {:.0f} centímetros e {:.0f} milímetros'.format(metros, centimetros, milimetros))
