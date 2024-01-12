# Faça um programa que leia o comprimento de cateto
# oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

# A medida da hipotenusa de um triângulo retângulo
# depende das medidas dos catetos, lados que forman 90 graus

# Para calcular a medida da hipotenusa:
# 1. Elevamos as medidas dos catetos ao quadrado
# 2. Somamos os resultados
# 3. Extraímos a raiz quadrada

# O cálculo da hipotenusa é enunciado pelo Teorema de pitágoras, que diz:
# A hipotenusa é igual a raiz quadrada da soma dos catetos ao quadrado

import math

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))

sqrt_cat_opos = math.pow(cateto_adjacente, 2)  # cateto_oposto ** 2
sqrt_cat_adja = math.pow(cateto_oposto, 2)  # cateto_adjacente ** 2

sum_catetos = sqrt_cat_opos + sqrt_cat_adja

hipotenusa = math.sqrt(sum_catetos)
hipontenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa é {}'.format(hipotenusa))
print('A hipontenusa é {}'.format(hipontenusa))
print('=====' * 100)

print(math.sqrt((cateto_adjacente ** 2) + (cateto_oposto ** 2)))
print(math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)))

print('=====' * 100)

# Em um triângulo retângulo, os catetos medem 5 cm e 12 cm. Determine a medida da hipotenusa.
co = 5
ca = 12

p1 = math.pow(co, 2) + math.pow(ca, 2)
final = math.sqrt(p1)
print(final)





