# 18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

nota1 = float(input("digigite a nota da prova1 (0 a 5): "))
nota2 = float(input("digigite a nota da prova2 (0 a 5): "))
nota3 = float(input("digigite a nota da prova3 (0 a 10): "))

if (nota1 > 5) or (nota1 < 0):
    print(f'nota 1 invalida')
    nota1 = float(input("digigite a nota da prova1 (0 a 5): "))

if (nota2 > 5) or (nota2 < 0):
    print(f'nota 2 invalida')
    nota2 = float(input("digigite a nota da prova2 (0 a 5): "))

if (nota3 > 10) or (nota3 < 0):
    print(f'nota 3 invalida')
    nota3 = float(input("digigite a nota da prova3 (0 a 10): "))


media = (nota1 + nota2 + nota3) / 3

print(f'sua média é {media}')

if (media >= 6):
    print(f'você foi aprovado')

else:
    print(f'você foi reprovado')