#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro numero: '))

#s = n1 + n2

#print("A soma entre {} e {} é {}".format(n1, n2, s))


# Teste de tipo
var1 = int(33)
var2 = float(2.5)
var3 = str('98a')
var4 = 5 > 1

print(type(var1), type(var2), type(var3),type(var4))
print(isinstance(var1, int))
print(isinstance(var2, float))
print(isinstance(var3, str))
print(isinstance(var4, bool))
print(callable(var1))
