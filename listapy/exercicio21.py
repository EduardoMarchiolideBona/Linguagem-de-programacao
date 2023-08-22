# 21) Crie um programa que leia dois valores e mostre na tela um menu :

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("DIgite o segundo número: "))

operacao = int(input("Digite a operação 1 - somar \n"
                                        "2 - multiplicar \n"
                                        "3 - maior \n"
                                        "4 - menor \n"
                                        "5 - sair do programa "))
while True:

    if (operacao == 1):
        print(f'A soma dos dois números é {numero1 + numero2}')

    if (operacao == 2):
        print(f'a multiplicação dos dois números é {numero1 * numero2}')

    if (operacao == 3):
        print(f'o maior numero é {max(numero1, numero2)}')

    if (operacao == 4):
        print(f'o maior numero é {min(numero1, numero2)}')

    if (operacao == 5):
        break