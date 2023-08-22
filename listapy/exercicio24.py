# 24) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite uma nota de 0 a 10: "))

if (nota > 10) or (nota < 0 ):
    print(f'nota invalida')
    nota = int(input("Digite uma nota de 0 a 10: "))

else :
    print(f'a nota {nota} é valida')