import os
os.system("clear || cls")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que a A + B é maior que C.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a + b < c:
    print(f"A soma dos valores é {a + b}")
    print("A + B é menor que C")
else:
    print("A + B é maior que C")
