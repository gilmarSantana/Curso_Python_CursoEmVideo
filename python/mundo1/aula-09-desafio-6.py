# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o ultimo nome separadamente


nome = "Gilmar Santana Lins"
nome = "Luana Gisele Gonzaga Lins"

nome = nome.split()
first = nome.pop(0)
last = nome.pop(-1)

print(first, last)


