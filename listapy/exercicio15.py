# 15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temperatura = float(input("DIgite a temperatura: "))

if (temperatura <= 15):
    print(f'está frio')

if (temperatura > 15) and (temperatura <= 26):
    print(f'confortável')

elif (temperatura > 26):
    print(f'está quente')