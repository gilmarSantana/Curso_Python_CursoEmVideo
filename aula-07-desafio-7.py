# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2mt quadrados.

larg = float(input('Informe a largura: '))
altu = float(input('Informe a altura: '))

area = larg * altu

litros_tinta_necessaria = area // 2

print('Para pintar uma área de {} metros você precisa'
      ' de {} litros de tinta'
      .format(area, litros_tinta_necessaria))


