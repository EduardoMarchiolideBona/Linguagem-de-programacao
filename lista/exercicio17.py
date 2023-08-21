# 17) Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde à altura): 

sexo = int(input("Digite seu sexo M (masculino) e F (feminino): "))
altura = float(input("Digite sua altura: "))

if (sexo == "M"):
    peso = (72.7 * altura) - 58
    print(f'O seu peso ideal é {peso}')

elif (sexo == "F"):
    peso = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é {peso}')
