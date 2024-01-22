# Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status
# conforme tabela abaixo

# Abaixo de 18.5: Abaixo do peso ideal
# Entre 18.5 e 25: Peso ideal
# Entre 25 até 30: Sobrepeso
# Entre 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = 170
altura = 1.80
imc = peso / (altura ** 2)

print(f'O imc é: {imc:.2f}')

if not 18.5 < imc:
    print('Abaixo do peso ideal')
elif 18.5 <= imc <= 24.99:
    print('Peso ideal')
elif 25 <= imc <= 29.99:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
elif 40 < imc:
    print('Obesidade mórbida')
