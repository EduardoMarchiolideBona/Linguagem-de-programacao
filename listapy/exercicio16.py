# 16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.

temp = input("digite a temperatura q deseja converter: ")
conv = int(input(f' 1 - Farenheit p/ celsius \n'
                  ' 2 - Celsius p/ Farenheit'))


if (conv == 1):
    (temp - 32) / 1.8
    print(f'a temperatura de F em C é {temp}')

elif (conv == 2):
    (temp * 1.8) + 32
    print(f'a temperatura de C em F é {temp}')