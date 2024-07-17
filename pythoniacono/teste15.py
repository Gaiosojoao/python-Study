# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variavel

cidade1 = 'Rio de Janeiro' 
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#              0                 1            2           3

# cidades.append('Santa Catarina') -> acaba adicionando no final da lista
# cidades.remove('Salvador') -> remove
# cidades.insert(1, 'Santa Catarina') -> add na posição que quiser
# cidades.pop(0) -> retira da posição escolhida
cidades.sort() # -> organiza em ordem alfabética

print(cidades)