# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome_completo = str(input('Digite seu nome completo: '))

# O nome com todas as letras maiúsculas
print(nome_completo.title())

# O nome com todas as letras minúsculas
print(nome_completo.lower())

# Quantas letras ao to do (sem considerar espaços)
letras = 0
for parte in nome_completo.split():
    letras = letras + len(parte)

print('O nome tem {} letras'.format(letras))

# Quantas letras tem o primeiro nome
nome_completo = nome_completo.split()
print('O primeiro nome tem', len(nome_completo[0]), 'letras.')


