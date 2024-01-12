frase = "  É sempre bom ouvir atentamente.  "

# [É][][s][e][m][p][r][e][ ][b][o][m][ ][o][u][v][i][r][ ][a][t][e][n][t][a][m][e][n][t][e][.]
#  0  1 2 3  4  5  6  7  8  9  10  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

# FATIAMENTO DE STRING
print(frase[9])  # b
print(frase[9:13])  # bom
print(frase[9:31])  # bom ouvir atentamente. Nesse caso ele não dá erro, pois o python sempre pega -1 posição,
# no caso a 30
print(frase[2:31:2])  # smr o ui tnaet. Aqui ele fatia pulando a cada dois
print(frase[:5])  # Nesse caso, quando se omite o início, ele pega da posição 0 da string
print(frase[10:])  # Nesse caso, quando se omite o final, ele pega até o final
print(frase[9::3])  # Nesse caso, ele inicia na 9 e vai até o final pulando a cada 3

print('=' * 100)

# ANÁLISE DE STRING

print(len(frase))  # Retorna o tamanho da string, função len() de length
print(frase.count('o'))  # Conta quantas vezes aparece a letra o
print(frase.count('o', 0, 14))  # Conta quantas vezes aparece a letra no intervalo de 0 a 13 (lembrando que o último
# valor é ignorado)
print(frase.find('bom'))  # Retorna em qual posição o texto de teste inicia
print(frase.find('bankai'))  # Quando o texto de teste não existe na string a função retorna -1
print('ouv' in frase)  # Retorna se True ou False se o texto de teste existe na string

print('=' * 100)

# TRANSFORMAÇÃO

print(frase.replace('ouvir', 'ouvir e entender'))  # Substitui um texto por outro dentro da string
print(frase.upper())  # Torna a string em Uppercase
print(frase.lower())  # Torna a string em Lowercase
print(frase.capitalize())  # Torna a primeira letra da string em uppercase
print(frase.title())  # Torna a primeira letra de cada palavra para uppercase
print(frase.strip())  # Remove os espaços em branco do início e final da string
print(frase.rstrip())  # Remove os espaços em branco do final da string
print(frase.lstrip())  # Remove os espaços em branco do início da string

texto = "O-senhor-dos-anéis-e-As-crônicas-de-Nárnia. \nOs filmes estão \n na sua lista \n para assistir mais tarde."

print(texto.split('-'))  # Separa/divide a string usando um delimitador (espaços é o padrão) e coloca as divisões
# numa lista
print(texto.split('-', 2))  # Limita quantas divisões serão feitas
print(texto.split('\n'))  # Dividindo por quebra de linha


# JUNÇÃO

texto2 = "É muito bom viajar para Porto de Galinhas em Ipojuca"
texto2 = texto2.split()
feira = ['maçã', 'banana', 'morango', 'abacate']
paragrafos = ['Para1', 'Para2', 'Para3', 'Para4']
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('-'.join(texto2))
print('Fui na feira e comprei', ', '.join(feira))
print('\n'.join(paragrafos))
print(''.join(map(str, numeros)))

print('=' * 100)


