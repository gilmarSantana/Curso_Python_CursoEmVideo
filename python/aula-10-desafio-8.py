# Desenvolva um programa que leia o comprimento das três retas e diga
# ao usuário se elas podem ou não formar um triângulo.


r1 = 90
r2 = 99
r3 = 9

t1 = r1 + r2 > r3
t2 = r2 + r3 > r1
t3 = r3 + r1 > r2

if t1 and t2 and t3:
    print("Os comprimentos podem formar um triângulo.")
else:
    print("Os comprimentos não podem formar um triângulo.")
