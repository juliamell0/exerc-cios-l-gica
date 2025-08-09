import os
os.system("clear || cls")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (m/f): ").upper()
estado = input("""
Casado(a) \t Solteiro(a) \t Divórciado(a) \t Viúvo(a)

Digite seu estado civil: """)

if sexo == 'F' and estado== 'casada':
    anos = int(input("Digite quantos anos você está casada: "))
else:
    anos = None

os.system("clear || cls")

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado}")

if anos is not None:
    print(f"Anos de Casamento: {anos}")

#None serve para indicar que a variável anos não foi definida, caso a usuária não seja do sexo feminino e casada.
#Se não colocasse o None, o programa tentaria imprimir a variável anos mesmo que ela não tenha sido definida, o que causaria um erro.
#is not none indica que deverá imprimir os anos se realmente foi informado.