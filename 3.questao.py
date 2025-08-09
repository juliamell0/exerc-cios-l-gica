import os
os.system("clear || clear")

a= int(input("Digite o valor de A: "))
b= int(input("Digite o valor de B: "))

if a == b:
    c = a+b
    print(f"A e B são iguais, a soma é {c}")
else:
    c= a*b
    print(f"A e B são diferentes, o produto é {c}")

