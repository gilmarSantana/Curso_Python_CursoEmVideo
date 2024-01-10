# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random

i = 1
nomes = []
random = random.randint(1, 4)

while i <= 4:
    nome = input('Nome do aluno {}: '.format(i))
    nomes.append(nome)
    i = i + 1

print("O sorteado dentre a lista é {}".format(nomes[random]))
