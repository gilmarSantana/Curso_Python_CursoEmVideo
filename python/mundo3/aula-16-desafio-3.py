# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
# Depois disse mostre a listagem de numeros gerado e tambem indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = tuple(randint(1, 9999) for _ in range(5))

print('Numeros gerados:', ', '.join(map(str, numeros)))

print('O maior número da lista é: ', max(numeros))
print('O menor número da lista é: ', min(numeros))

print('-=' * 50)

if numeros:
    menor = maior = numeros[0]
    for num in numeros:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num

    print('O maior número da lista é: ', maior)
    print('O menor número da lista é: ', menor)

