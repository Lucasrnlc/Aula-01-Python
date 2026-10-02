# Crie um algoritimo que leia 3 valores referente (lados de um triangulo)
# Determine se formam um triângulo, e se formar verifique
# se é um equilátero, isósceles ou escaleno

lado1 = float(input("digite o valor do lado 1: "))
lado2 = float(input("digite o valor do lado 2: "))
lado3 = float(input("digite o valor do lado 3: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):

    if (lado1 == lado2) and (lado2 == lado3):
        print("é um triângulo equilátero")

    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("é um triângulo isóceles:")

    else:
        print ("é um triângulo escaleno")    

        
else:
    print ("não é um triângulo")        