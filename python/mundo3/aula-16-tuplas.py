# Tupla é uma variável composta
# As tuplas são imutáveis


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-' * 100)

for count in range(0, len(lanche)):
    print(lanche[count])

print('-' * 100)


for pos, comida in enumerate(lanche):
    print(pos, comida)

print('-' * 100)

print(sorted(lanche))

print('-' * 100)

a = (1,2,3,3,2,1)
b = (4,5,6,6,5,4)
c = a + b
d = b + a

print(a, b, c, d)

print('-' * 100)

print(c.count(5))

print('-' * 100)

print(c.index(6))
print(c.index(6, 9))

print('-' * 100)

pessoa = ('Gilmar', 26, 'M', 70.00)
print(pessoa)
del pessoa
print(pessoa)












