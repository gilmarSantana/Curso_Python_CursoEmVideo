# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

rang = 4
a = [0, 0, 0, 0]

for num in range(rang):
    a[num] = input(f'Digite um numero {num+1}/{rang}:')

b = tuple(a)

print('\nOs números informados são: ', ', '.join(map(str, b)))

# Quantas vezes apareceu o valor 9
print(f"Apareceu o número 9 => {b.count('9')} veze(s)")

# Em que posição foi digitado o primeiro valor 3
if '3' in b:
    print(f"O numero 3 apareceu primeiro na posição {b.index('3')}")
else:
    print('Número 3 não informado')

# Quais foram os números pares
pares = []
for i in b:
    if int(i) % 2 == 0:
        pares.append(i)

print(f"Os números pares foram: {', '.join(map(str, pares))}")


# Teacher resolution

nums = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
)


print(f'Você digitou os seguintes valores: {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
print(f'O valor 3 apareceu na {nums.index(3)} posição')

