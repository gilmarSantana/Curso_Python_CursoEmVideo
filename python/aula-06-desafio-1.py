n1 = ''
n2 = ''

while n1 == '':
    n1 = int(input('Digite um número: '))

while n2 == '':
    n2 = int(input('Digite outro número: '))

print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
