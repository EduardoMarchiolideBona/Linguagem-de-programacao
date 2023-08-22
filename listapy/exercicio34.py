# Faça 4 listas: A. Filmes B. Jogos C. Livros D. Esporte a. Adicione no mínimo 2 itens em cada lista. b. Crie uma lista das 4 listas criadas acima. c. Acesse (mostrar) algum item da lista livros. d. Remova um item da lista esporte.

filmes = []
jogos = []
livros = []
esporte = []

filmes.append("Senhor dos aneis", "Carros")
jogos.append("Elden ring", "Forza")
livros.append("Senhor dos aneis", "Harry potter")
esporte.append("basquete ", "volei")

todas = [filmes, jogos, livros, esporte]

print(f'um item da lista livro é {livros[1]}')

esporte.remove("basquete")
