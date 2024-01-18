nome = ''

while nome == '':
    nome = str(input('Olá, qual é o seu nome? '))

msg = str(f"Seja muito bem vindo, {nome}")
msg2 = "Seja muito bem vindo, {}".format(nome)
print(msg)
print(msg2)
