# Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são:

idade = int(input("digite sua idade: "))
temp_servico = int(input("Digite seu tempo de serviço: "))

if (idade >= 65):
    print("você pode se aposentar")

elif (temp_servico >= 30):
    print("você pode se aposentar")

elif (idade >= 60) and (temp_servico >= 25):
    print("você pode se aposentar")
    
