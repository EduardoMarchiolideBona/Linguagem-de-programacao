# 28) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0
cand = int(input("Digite o número de candidatos: "))
for i in range(cand):
    voto = int(input("Digte um numero de 1 a 3 (representando seu candidato): "))
    if voto == 1:
        candato1 =+ 1
    if voto == 2:
        candato2 =+ 1
    if voto == 3:
        candato3 =+ 1

print(f'o numero de votos de cada candidato respectivamente foi {candidato1, candidato2, candidato3} ')

