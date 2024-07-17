# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variavel

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

# final = numeros + letras

numeros.extend(letras)
print(numeros)