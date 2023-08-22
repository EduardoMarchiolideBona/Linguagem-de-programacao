# 14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.

listaa = ["cafe", "miojo", "pao"]
v = input(f'que item vc quer verificar: ')
for i in listaa:
    
    if v in listaa:
        print(f'o item está na lista')
        listaa.index(v)
        break
    else:
        listaa.append(v)