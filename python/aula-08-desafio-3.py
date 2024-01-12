# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente de ângulo
import math

angulo = int(input('Qual o ângulo? '))


# O seno é a razão entre a medida do cateto oposto ao ângulo agudo e a medida da hipotenusa de um triângulo retângulo.
# Formula: sen = cateto_oposto / hipotenusa
seno = math.sin(math.radians(angulo))
print(seno)

# O Cosseno é a razão entre a medida do cateto adjacente ao ângulo agudo e a medida da hipotenusa de um triângulo retângulo.
# Formula: cos = cateto_adjacente / hipotenusa
cosseno = math.cos(math.radians(angulo))
print(cosseno)


# A tangente é a razão entre a medida do cateto oposto e a medida do cateto adjacente ao ângulo agudo de um triângulo retângulo.
tangente = math.tan(math.radians(angulo))
print(tangente)
