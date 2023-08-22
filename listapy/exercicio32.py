# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

cidadestotal = 5
totalveiculos = 0
totalacidentes = 0
menor_indice = float('inf')
maior_indice = 0
cidademenorindice = ""
cidademaiorindice = ""
cidades_menos_2000_veiculos = 0

for cidade in range(cidadestotal):
    codcidade = int(input(f"Digite o código da cidade {cidade}: "))
    veiculos = int(input(f"Digite o número de veículos de passeio em 1999 na cidade {cidade}: "))
    acidentes = int(input(f"Digite o número de acidentes de trânsito com vítimas em 1999 na cidade {cidade}: "))

    totalveiculos += veiculos
    totalacidentes += acidentes

    if (veiculos < 2000):
            cidades_menos_2000_veiculos += 1
            media_acidentes_menos_2000 = totalacidentes / cidades_menos_2000_veiculos

    indice = acidentes / veiculos

    if indice < menor_indice:
            menor_indice = indice
            cidade_menor_indice = codcidade

    if indice > maior_indice:
            maior_indice = indice
            cidade_maior_indice = codcidade

    media_veiculos = totalveiculos / cidadestotal

    print(f"Maior índice de acidentes: {maior_indice} (Cidade: {cidademaiorindice})")
    print(f"Menor índice de acidentes: {menor_indice} (Cidade: {cidademenorindice})")
    print(f"Média de veículos nas cinco cidades: {media_veiculos}")
    print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes_menos_2000}")