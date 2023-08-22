# ) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
contcand1 = 0
contcand2 = 0
contcand3 = 0
contcand4 = 0
contbranco = 0
contnulo = 0

votos_qntd = int(input(f'Digite a quantidade total de votos: '))

for i in range(votos_qntd):
    voto = int(input("digite seu voto : 1 - josé \n"
                     "2 - joão \n"
                     "3 - pedro \n"
                     "4 - maria \n"
                     "5 - em branco \n"
                     "6 - nulo "))
    
    if (voto == 1):
        contcand1 += 1
    
    elif (voto == 2):
        contcand2 += 1

    elif (voto == 3):
        contcand3 += 1
    
    elif (voto == 4):
        contcand4 += 1
    elif (voto == 5):
        contbranco += 1
    elif (voto == 6):
        contnulo += 1
    
    print(f'candidato 1 {contcand1}')
    print(f'candidato 2 {contcand2}')
    print(f'candidato 3 {contcand3}')
    print(f'candidato 4 {contcand4}')
    print(f'em branco {contbranco}')
    print(f'nulo {contnulo}')
    print(f'porcentagem de nulo {(contnulo * 100) / votos_qntd}')
    print(f'porcentagem de votos em branco {(contbranco * 100) / votos_qntd}')
    
