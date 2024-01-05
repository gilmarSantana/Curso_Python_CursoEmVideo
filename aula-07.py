print(5 + 3 == 8)  # operador de adição
print(5 - 3 == 2)  # operador de subtração
print(5 * 3 == 15)  # operador de multiplicação
print(5 / 2 == 2.5)  # operador de divisão
print(5 ** 2 == 25)  # operador de exponenciação
print(5 // 2 == 2)  # operador de divisão inteira
print(5 % 2 == 1)  # operador de resto da divisão

print(5 + 3 * 2 == 11)
print(3 * 5 + 4 ** 2 == 31)
print(3 * (5 + 4) ** 2 == 243)

print('=' * 30)


n1 = int(input('Um valor: '))
n2 = int(input('Um outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))

print('=' * 30)
